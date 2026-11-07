/* Read the local site in Chrome/Edge; never submit forms or change site files. */
const http = require('node:http');
const fs = require('node:fs');
const path = require('node:path');
const os = require('node:os');
const { spawn } = require('node:child_process');

const [root, output, browser] = process.argv.slice(2);
if (!root || !output || !browser) throw new Error('Usage: node capture-site.cjs ROOT OUTPUT BROWSER');
const types = { '.html':'text/html; charset=utf-8', '.css':'text/css', '.js':'application/javascript', '.webp':'image/webp', '.png':'image/png', '.jpg':'image/jpeg', '.woff2':'font/woff2', '.pdf':'application/pdf', '.mp4':'video/mp4' };
const server = http.createServer((req, res) => {
  const requested = path.resolve(root, '.' + decodeURIComponent(new URL(req.url, 'http://localhost').pathname));
  if (!requested.startsWith(path.resolve(root) + path.sep)) { res.writeHead(403); res.end(); return; }
  fs.stat(requested, (error, stat) => {
    if (error || !stat.isFile()) { res.writeHead(404); res.end('Not found'); return; }
    const headers = { 'Content-Type': types[path.extname(requested)] || 'application/octet-stream', 'Accept-Ranges': 'bytes' };
    let start = 0, end = stat.size - 1, status = 200;
    if (req.headers.range) {
      const range = /^bytes=(\d*)-(\d*)$/.exec(req.headers.range);
      if (!range || (!range[1] && !range[2])) { res.writeHead(416, {'Content-Range':`bytes */${stat.size}`}); res.end(); return; }
      if (!range[1]) start = Math.max(0, stat.size - Number(range[2]));
      else {
        start = Number(range[1]);
        if (range[2]) end = Math.min(end, Number(range[2]));
      }
      if (start > end || start >= stat.size) { res.writeHead(416, {'Content-Range':`bytes */${stat.size}`}); res.end(); return; }
      status = 206;
      headers['Content-Range'] = `bytes ${start}-${end}/${stat.size}`;
    }
    headers['Content-Length'] = Math.max(0, end - start + 1);
    res.writeHead(status, headers);
    if (req.method === 'HEAD' || stat.size === 0) { res.end(); return; }
    fs.createReadStream(requested, {start, end}).pipe(res);
  });
});
let child, socket;
const result = [];
const preferred = ['index.html','about.html','resume.html','certifications.html','services.html','portfolio.html','portfolio-details.html','pulmotrack-details.html','testpilot-details.html','aura-1-details.html','digital-gallery.html','contact.html','starter-page.html'];
const pages = [...preferred.filter(p => fs.existsSync(path.join(root,p))), ...fs.readdirSync(root).filter(p => p.endsWith('.html') && !preferred.includes(p)).sort()];
const profile = fs.mkdtempSync(path.join(os.tmpdir(), 'portfolio-documentation-'));
const timeout = setTimeout(() => { console.error('Browser capture timed out.'); if (child) child.kill(); process.exit(1); }, 90000);

(async () => {
  await new Promise(r => server.listen(0, '127.0.0.1', r));
  const base = `http://127.0.0.1:${server.address().port}`;
  child = spawn(browser, ['--headless=new','--disable-gpu','--no-first-run','--no-default-browser-check','--remote-debugging-port=0',`--user-data-dir=${profile}`,'about:blank'], {windowsHide:true,stdio:['ignore','ignore','pipe']});
  const endpoint = await new Promise((resolve, reject) => {
    let log='';
    child.stderr.on('data', b => { log += b; const match=log.match(/DevTools listening on (ws:\/\/[^\s]+)/); if (match) resolve(match[1]); });
    child.on('error', reject);
    child.on('exit', code => { if (code) reject(new Error('Browser exited: '+code)); });
  });
  const targets = await (await fetch(endpoint.replace('ws:','http:').replace(/\/devtools\/browser\/.*/, '/json/list'))).json();
  socket = new WebSocket(targets.find(t => t.type==='page').webSocketDebuggerUrl);
  await new Promise((resolve,reject) => { socket.onopen=resolve; socket.onerror=reject; });
  let id=0;
  const pending=new Map();
  socket.onmessage = event => { const message=JSON.parse(event.data); if(message.id) { const entry=pending.get(message.id); pending.delete(message.id); if(entry) message.error?entry.reject(new Error(JSON.stringify(message.error))):entry.resolve(message.result); } };
  const send=(method,params={}) => new Promise((resolve,reject) => { const seq=++id; pending.set(seq,{resolve,reject}); socket.send(JSON.stringify({id:seq,method,params})); });
  await send('Page.enable');
  await send('Runtime.enable');
  await send('Network.enable');
  await send('Network.setBlockedURLs',{urls:['https://*','http://www.*']});
  await send('Emulation.setDeviceMetricsOverride',{width:1440,height:1000,deviceScaleFactor:1,mobile:false});
  for (const file of pages) {
    const response=await fetch(base+'/'+file);
    if(response.status!==200) throw new Error('Cannot read '+file);
    await send('Page.navigate',{url:base+'/'+file});
    await new Promise(r => setTimeout(r,750));
    const captured=await send('Runtime.evaluate',{returnByValue:true,expression:`(() => {
      document.querySelectorAll('[data-aos]').forEach(e => e.classList.add('aos-animate'));
      const typewriter=document.querySelector('.js-typewriter');
      if(typewriter) typewriter.textContent=JSON.parse(typewriter.dataset.words)[0] || '';
      const elements=[...document.querySelectorAll('main,header,footer')];
      const text=elements.map(e=>({region:e.tagName.toLowerCase(),text:e.innerText}));
      return {html:document.documentElement.outerHTML, renderedText:text, title:document.title};
    })()`});
    if(captured.exceptionDetails) throw new Error('Capture failed for '+file);
    result.push({file,...captured.result.value});
    console.log('Captured '+file);
  }
  fs.writeFileSync(output, JSON.stringify(result,null,2));
})().catch(error => {console.error(error);process.exitCode=1;}).finally(() => {clearTimeout(timeout);if(socket)socket.close();if(child)child.kill();server.close();});
