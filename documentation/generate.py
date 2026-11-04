"""Regenerate portfolio documentation from the local website, without editing it.

Requires Python 3.10+, Node.js 22+, Chrome/Edge, and PyMuPDF.
Run: python documentation/generate.py
"""
from __future__ import annotations

import argparse
import hashlib
import html
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
from datetime import datetime
from zoneinfo import ZoneInfo
from zipfile import ZipFile, ZIP_DEFLATED
from urllib.parse import urlsplit, unquote
from xml.sax.saxutils import escape as xml_escape

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
STEM = 'Farah_Sayari_Portfolio_Documentation'
VOID = {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}


def normalize(value):
    return re.sub(r'\s+', ' ', value).strip()


class Node:
    def __init__(self, tag, attrs=(), parent=None):
        self.tag, self.attrs, self.parent = tag, dict(attrs), parent
        self.children = []

    def has(self, cls):
        return cls in self.attrs.get('class','').split()

    def walk(self):
        yield self
        for child in self.children:
            if isinstance(child, Node):
                yield from child.walk()

    def find(self, tag=None, cls=None, id=None):
        return next((n for n in self.walk() if (not tag or n.tag == tag) and (not cls or n.has(cls)) and (not id or n.attrs.get('id') == id)), None)

    def raw_text(self):
        if self.tag in {'script','style','svg'}:
            return ''
        return ''.join(c.raw_text() if isinstance(c, Node) else c for c in self.children)

    def text(self):
        if self.tag == 'table':
            return ' '.join(n.text() for n in self.walk() if n.tag in {'th','td'})
        # The language chips have a CSS gap between adjacent inline elements.
        if self.tag == 'li' and self.parent and self.parent.has('resume-languages'):
            return ' '.join(c.text() for c in self.children if isinstance(c, Node))
        return normalize(self.raw_text())

    def ancestors(self):
        p = self.parent
        while p:
            yield p
            p = p.parent


class Tree(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.root = Node('document')
        self.current = self.root
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        node = Node(tag, attrs, self.current)
        self.current.children.append(node)
        if tag not in VOID:
            self.current = node

    def handle_endtag(self, tag):
        node = self.current
        while node.parent:
            if node.tag == tag:
                self.current = node.parent
                return
            node = node.parent

    def handle_data(self, data):
        self.current.children.append(data)


def hidden(node):
    return any('hidden' in n.attrs or n.has('d-none') or any(n.has(c) for c in ['loading','error-message','sent-message']) for n in [node, *node.ancestors()])


def link_row(node):
    label = node.text() or node.attrs.get('aria-label') or node.attrs.get('title')
    if not label:
        icons = [n.attrs.get('class','') for n in node.walk() if n.tag == 'i']
        label = 'Icon: ' + ', '.join(icons) if icons else '(no text label)'
    return [label, node.attrs.get('href',''), node.attrs.get('download','')]


def transcript(main):
    tags = {'h1','h2','h3','h4','h5','h6','p','li','dt','dd','label','button','a','figcaption','table'}
    blocks = []
    for node in main.walk():
        if node.tag not in tags or hidden(node) or not node.text():
            continue
        if any(a.tag in tags for a in node.ancestors() if a is not main):
            continue
        block={'tag':node.tag, 'text':node.text()}
        if node.tag=='table':
            rows=[[c.text() for c in row.walk() if c.tag in {'th','td'}] for row in node.walk() if row.tag=='tr']
            block.update(headers=rows[0] if rows else [],rows=rows[1:])
        blocks.append(block)
    return blocks


def build_inventory(captures):
    pages = []
    for capture in captures:
        root = Tree(capture['html']).root
        main = root.find('main')
        header, footer = root.find('header'), root.find('footer')
        nav = header.find('nav') if header else None
        social = header.find(cls='header-social-links') if header else None
        footer_social = footer.find(cls='social-links') if footer else None
        copyright = footer.find(cls='copyright') if footer else None
        credits = footer.find(cls='credits') if footer else None
        metadata = {n.attrs.get('name'):n.attrs.get('content','') for n in root.walk() if n.tag=='meta' and n.attrs.get('name')}
        page = {
            'file':capture['file'], 'title':capture['title'], 'language':root.find('html').attrs.get('lang',''),
            'metadata':metadata, 'sections':[[n.tag,n.attrs.get('id','')] for n in main.walk() if n.tag=='section'],
            'copy':transcript(main),
            'navigation':[[n.text(),n.attrs.get('href',''), 'active' if n.has('active') else ''] for n in nav.walk() if n.tag=='a'] if nav else [],
            'brand':header.find(cls='sitename').text() if header and header.find(cls='sitename') else '',
            'header_social':[link_row(n)[:2] for n in social.walk() if n.tag=='a'] if social else [],
            'footer': {'copyright':copyright.text() if copyright else '', 'credits':credits.text() if credits else '', 'social':[link_row(n)[:2] for n in footer_social.walk() if n.tag=='a'] if footer_social else [], 'credit_links':[link_row(n)[:2] for n in credits.walk() if n.tag=='a'] if credits else []},
            'links':[link_row(n) for n in main.walk() if n.tag=='a'],
            'images':[[n.attrs.get('src',''),n.attrs.get('alt',''),n.attrs.get('role','')] for n in main.walk() if n.tag=='img'],
            'embeds':[[n.attrs.get('title',''),n.attrs.get('src','')] for n in main.walk() if n.tag=='iframe'],
            'forms':[], 'dynamic':[], 'projects':[],
            'stylesheets':[n.attrs.get('href','') for n in root.walk() if n.tag=='link' and n.attrs.get('rel')=='stylesheet'],
            'scripts':[n.attrs['src'] for n in root.walk() if n.tag=='script' and n.attrs.get('src')],
            'icons':[[n.attrs.get('rel',''),n.attrs.get('href','')] for n in root.walk() if n.tag=='link' and 'icon' in n.attrs.get('rel','')],
            'rendered_text':capture['renderedText'],
        }
        for node in main.walk():
            if node.attrs.get('data-words'):
                words = json.loads(node.attrs['data-words'])
                page['dynamic'].append({'type':'typewriter','values':words})
            if node.has('about-image-loop'):
                page['dynamic'].append({'type':'photo-loop','values':[n.attrs['src'] for n in node.walk() if n.tag=='img']})
            if node.has('project-gallery') and node.has('carousel'):
                page['dynamic'].append({'type':'image-carousel','values':[n.attrs['src'] for n in node.walk() if n.tag=='img']})
            if node.has('portfolio-item'):
                heading = next((n for n in node.walk() if n.tag in {'h3','h4'}),None)
                description = node.find('p')
                page['projects'].append({'name':heading.text() if heading else '', 'description':description.text() if description else '', 'categories':[c for c in node.attrs.get('class','').split() if c.startswith('filter-')], 'links':[link_row(n)[:2] for n in node.walk() if n.tag=='a'], 'image':node.find('img').attrs.get('src','') if node.find('img') else ''})
            if node.tag=='form':
                controls = []
                for field in node.walk():
                    if field.tag not in {'input','textarea','select'}:
                        continue
                    label = next((n.text() for n in node.walk() if n.tag=='label' and n.attrs.get('for')==field.attrs.get('id')), '')
                    controls.append([label, field.attrs.get('name',''), field.attrs.get('type',field.tag), field.attrs.get('placeholder',''), field.attrs.get('value',''), 'yes' if 'required' in field.attrs else 'no', 'hidden' if hidden(field) or field.attrs.get('type')=='hidden' else 'visible'])
                inline_js = '\n'.join(n.raw_text() if n.tag!='script' else ''.join(c for c in n.children if isinstance(c,str)) for n in root.walk() if n.tag=='script' and not n.attrs.get('src'))
                messages = [n.text() for n in node.walk() if any(n.has(c) for c in ['loading','error-message','sent-message']) and n.text()]
                messages += re.findall(r"(?:showMessage\(\s*'[^']+'\s*,\s*|new Error\(\s*|error\.message\s*\|\|\s*)'([^']+)'",inline_js)
                page['forms'].append({'action':node.attrs.get('action',''), 'method':node.attrs.get('method','GET'), 'id':node.attrs.get('id',''), 'controls':controls, 'messages':list(dict.fromkeys(messages))})
        pages.append(page)
    return pages


class Report:
    def __init__(self):
        self.items=[]

    def add(self, kind, text='', **kwargs):
        self.items.append({'kind':kind,'text':text,**kwargs})

    def table(self, headers, rows):
        if rows:
            self.add('table',headers=headers,rows=rows)


def make_report(pages, date, notes):
    report=Report()
    add=report.add
    add('cover','Farah Sayari',subtitle='Portfolio content reference',date=date.strftime('%d %B %Y'))
    add('p','An exact content record of the local portfolio: every HTML page, its text, navigation, project entries, links, images, form fields, and dynamic text states.')
    add('p',f'Snapshot: {date.isoformat()} · Africa/Tunis · {len(pages)} HTML pages. The source files are the authority for this record.')
    add('h1','Document guide')
    add('p','Website wording is reproduced without rewriting. HTML entities are decoded and layout whitespace is normalized; line wrapping, bullets, and font treatment follow this document. Content follows HTML source order, so a two-column page is read column by column. Hover text and animated alternatives are recorded explicitly.')
    add('p','This is a content reference rather than a screenshot reproduction. Explanatory notes, inventories, and update instructions are separate from the sections marked “Exact page content.” External websites, the map service, and contact delivery were not verified; the contact form was not submitted.')
    add('h2','Pages covered')
    labels={'index.html':'Home','about.html':'About','resume.html':'Resume','certifications.html':'Certifications','digital-gallery.html':'Digital Gallery','services.html':'Services','portfolio.html':'Portfolio','portfolio-details.html':'LollyBooks project details','pulmotrack-details.html':'PulmoTrack project details','contact.html':'Contact','starter-page.html':'Starter template'}
    report.table(['No.','Page','Source file','Entry point'],[[str(i),labels.get(p['file'],p['title']),p['file'],'Portfolio detail link' if p['file'].endswith('-details.html') else 'Retained template; absent from the main navigation' if p['file']=='starter-page.html' else 'Main navigation'] for i,p in enumerate(pages,1)])
    add('h2','How to update this record')
    for text in [
        'To update the website and its documentation: edit the relevant HTML, CSS, JavaScript, image, or CV file, then run the regeneration command below from the portfolio folder.',
        'python documentation/generate.py',
        'On Windows, you can also double-click documentation/Refresh Documentation.cmd. The script reads the current website and refreshes the PDF, editable Word file, HTML, Markdown, JSON inventory, and source snapshot archive.',
        'For a documentation-only revision, open the .docx file in Word or LibreOffice and save/export it as PDF. This does not change the website. Regeneration replaces generated outputs, so preserve manual Word edits under a different filename.',
        'Keep ongoing commentary or planned work in documentation/notes.json. Those notes survive regeneration and are labeled separately from current website content.',
    ]:
        add('code' if text.startswith('python ') else 'p',text)
    add('h2','Where to make common changes')
    report.table(['Change','Edit these sources'],[
        ['Home introduction / animated job titles','index.html; animation timing in assets/js/main.js'],
        ['Biography / contact profile / rotating photos','about.html; assets/img/me11.png, me22.png, me33.png'],
        ['Resume text / downloadable CV','resume.html; assets/docs/Farah_Sayari_CV2026.pdf'],
        ['Service titles and descriptions','services.html'],
        ['Digital drawings / gallery introduction','digital-gallery.html; assets/css/collections.css'],
        ['Course certificates / credential links','certifications.html; assets/css/collections.css'],
        ['Project list / filters / thumbnails','portfolio.html; assets/img/portfolio/ and assets/img/masonry-portfolio/'],
        ['LollyBooks case study','portfolio-details.html; assets/img/portfolio/lollybooks/library-art.webp'],
        ['PulmoTrack case study / scientific paper','pulmotrack-details.html; assets/docs/PulmoTrackPaper.pdf; assets/img/portfolio/pulmotrack/paper-preview.png'],
        ['Contact text / form fields / delivery endpoint','contact.html, including its inline JavaScript'],
        ['Global header / footer','Repeated in each HTML file; update each affected page'],
        ['Shared visual styles / page-specific styles','assets/css/main.css; assets/css/resume.css; assets/css/portfolio.css; assets/css/collections.css'],
        ['Shared navigation / animations / filtering','assets/js/main.js'],
    ])

    # Store repeated site chrome once and map every page to its exact variant.
    nav_variants, social_variants, footer_variants = [], [], []
    def variant(value, collection):
        if value not in collection:
            collection.append(value)
        return collection.index(value)+1
    refs=[]
    for p in pages:
        nav=[[row[0],row[1]] for row in p['navigation']]
        refs.append([p['file'],p['brand'],f'N{variant(nav,nav_variants)}',f'S{variant(p["header_social"],social_variants)}',f'F{variant(p["footer"],footer_variants)}',', '.join(row[0] for row in p['navigation'] if row[2]) or '(none)'])
    add('h1','Shared header, navigation, and footer')
    add('p','Use the table below with the exact variants that follow. Each page’s visible brand, navigation labels, social destinations, footer text, and active navigation item are included.')
    report.table(['Page','Brand','Navigation','Header social','Footer','Active item'],refs)
    for i,rows in enumerate(nav_variants,1):
        add('h2',f'Navigation N{i}')
        report.table(['Exact label (in source order)','Destination'],rows)
    for i,rows in enumerate(social_variants,1):
        add('h2',f'Header social links S{i}')
        report.table(['Label / icon class','Exact destination'],rows)
    for i,footer in enumerate(footer_variants,1):
        add('h2',f'Footer F{i}')
        add('copy',footer['copyright'])
        add('copy',footer['credits'])
        report.table(['Social label / icon class','Exact destination'],footer['social'])
        report.table(['Attribution label','Exact destination'],footer['credit_links'])
    add('p','An empty destination is shown as “(empty)”; a destination of # is a fragment placeholder. The starter template contains a malformed ThemeWagon anchor in its source. Its browser-parsed label and destination above are recorded as they currently resolve.')
    add('h2','Shared interactions and appearance')
    add('p','The site has a sticky header, a mobile navigation toggle, an initial preloader, a scroll-to-top icon, and animation-on-scroll effects. These elements have no additional visible body copy. The scroll-to-top icon uses href="#" and is activated after scrolling past 100 pixels in the current shared script.')
    css=(ROOT/'assets/css/main.css').read_text(encoding='utf-8')
    report.table(['Style token','Current value'],[[name, re.search(r'--'+name+r'\s*:\s*([^;]+)',css).group(1)] for name in ['default-font','heading-font','nav-font','background-color','default-color','heading-color','accent-color']])

    for number,page in enumerate(pages,1):
        add('h1',f'{number:02d} · {labels.get(page["file"],page["title"])}')
        report.table(['Page attribute','Exact value'],[
            ['Source file',page['file']],['Browser title',page['title']],['Language',page['language']],
            ['Description meta tag',page['metadata'].get('description','(absent)')],['Keywords meta tag',page['metadata'].get('keywords','(absent)')],
            ['Main section IDs',', '.join(s[1] for s in page['sections'])],
        ])
        if page['file']=='starter-page.html':
            add('p','Retained template file. It is not linked from the main navigation or the current project list. Its template copy is reproduced below as part of the complete file inventory.')
        if page['projects']:
            add('p','The portfolio uses a masonry grid with project labels in hover overlays. The image inventory below records the current thumbnails. Entries with no description or detail links are recorded as placeholders.')
        if page['file']=='resume.html':
            add('p','The source has two columns: summary, education, skills, languages, and activities first; professional experience and projects second. The text below follows that source order. The downloadable CV is a separate PDF and is appended to the final PDF reference unchanged.')
        add('h2','Exact page content')
        for block in page['copy']:
            tag,text=block['tag'],block['text']
            if tag=='table':
                report.table(block['headers'],block['rows'])
            else:
                add('copy-heading' if re.fullmatch('h[1-6]',tag) or tag=='dt' else 'copy-bullet' if tag=='li' else 'copy',text,source_tag=tag)
        if page['dynamic']:
            add('h2','Animated content and alternate states')
            for dynamic in page['dynamic']:
                if dynamic['type']=='typewriter':
                    add('p','The fixed introduction is “I\'m a”. The animated span cycles through these exact titles; the cursor displays “|”. The first complete title is used in the transcript above.')
                    for word in dynamic['values']:
                        add('copy',word)
                    js=(ROOT/'assets/js/main.js').read_text(encoding='utf-8')
                    timings=[]
                    for key in ['typingSpeed','deletingSpeed','pauseAfterTyping','pauseAfterDeleting']:
                        match=re.search(r'const\s+'+key+r'\s*=\s*(\d+)',js)
                        if match:
                            timings.append([key,match.group(1)+' ms'])
                    report.table(['Animation parameter','Current value'],timings)
                elif dynamic['type']=='photo-loop':
                    js=(ROOT/'assets/js/main.js').read_text(encoding='utf-8')
                    timing=re.search(r'window\.setInterval\([\s\S]*?\},\s*(\d+)\)',js)
                    interval=timing.group(1)+' ms' if timing else '(see shared JavaScript)'
                    add('p',f'The {len(dynamic["values"])} profile images alternate in a continuous loop. Current switch interval: {interval}. Image paths and exact alternate text are in the image inventory below.')
                elif dynamic['type']=='image-carousel':
                    add('p',f'The project image card contains {len(dynamic["values"])} manually switchable images. Previous/next buttons, slide indicators, keyboard navigation, and touch swipes select the project artwork or team photo. Automatic rotation is disabled; the project artwork is initially selected.')
                    report.table(['Slide','Image path'],[[str(i),value] for i,value in enumerate(dynamic['values'],1)])
        if page['projects']:
            add('h2','Project entries and filter membership')
            report.table(['Project','Description','Filters','Detail destination'],[[p['name'],p['description'] or '(empty)',', '.join(c.replace('filter-app','App').replace('filter-branding','Web') for c in p['categories']),next((l[1] for l in p['links'] if l[1].endswith('.html')),'(none)')] for p in page['projects']])
            add('p','The default filter is All. Filter membership and every existing detail destination are listed in the table above. Project image preview links open the lightbox. Entries without detail links remain unlinked. The filter controls also support Enter and Space in the current inline script.')
        if page['links']:
            add('h2','Main-content links and downloads')
            report.table(['Exact label / accessible label','Exact destination','Download filename'],page['links'])
        if page['images']:
            add('h2','Main-content images')
            report.table(['Image path','Exact alternate text','Role'],page['images'])
        if page['embeds']:
            add('h2','Embedded content')
            report.table(['Exact title','Exact embed URL'],page['embeds'])
        for form in page['forms']:
            add('h2','Contact form configuration and field copy')
            report.table(['Attribute','Value'],[['Form ID',form['id']],['Method',form['method']],['Action',form['action']]])
            for control in form['controls']:
                label,name,kind,placeholder,value,required,visibility=control
                add('h3',label or name)
                report.table(['Field attribute','Exact value'],[['HTML name',name],['Type',kind],['Placeholder',placeholder],['Default / hidden value',value],['Required',required],['Visibility',visibility]])
            add('h3','Conditional interface messages')
            for message in form['messages']:
                add('copy',message)
            add('p','The browser validates required fields and the email format. On submission the inline script posts FormData to the configured action with Accept: application/json, shows a loading state, and disables the submit button. A successful response resets the form and shows the success message. An invalid form or unsuccessful request shows the corresponding message above. The _gotcha field is the hidden honeypot; the _subject field supplies the notification subject.')

    add('h1','Source inventory and current content differences')
    add('h2','Current differences retained in this record')
    add('p','The document records the website as it exists. These items are observations for future editing; the website was not changed while preparing this reference.')
    observations=[]
    emails={}
    for page in pages:
        for _,destination in page['header_social']+page['footer']['social']:
            if destination.startswith('mailto:'):
                emails.setdefault(destination[7:],set()).add(page['file'])
    observations.append(['Header/footer email destinations','; '.join(email+': '+', '.join(sorted(files)) for email,files in emails.items())])
    dropdowns=[page['file'] for page in pages if any(row[1]=='#' for row in page['navigation'])]
    if dropdowns:
        observations.append(['Placeholder navigation links',', '.join(dropdowns)+'. Exact labels and destinations are in the shared navigation inventory.'])
    placeholders=[p['name'] for page in pages for p in page['projects'] if not p['description'] and not p['links']]
    if placeholders:
        observations.append(['Project entries without descriptions or links',', '.join(placeholders)])
    project_names=[p['name'] for page in pages for p in page['projects']]
    resume=next((p for p in pages if p['file']=='resume.html'),None)
    if resume and any(b['text']=='Aura' for b in resume['copy']) and 'AI Agent Recruiter' in project_names:
        observations.append(['Different project naming','The resume calls its career assistant Aura; the portfolio entry is titled AI Agent Recruiter. This reference does not assume that they are the same project.'])
    starter=next((p for p in pages if p['file']=='starter-page.html'),None)
    if starter:
        observations.append(['Retained starter page','starter-page.html. Current brand: '+starter['brand']+'. Its exact content and links are recorded in its section.'])
    legacy=ROOT/'forms/contact.php'
    if legacy.exists():
        source=legacy.read_text(encoding='utf-8')
        match=re.search(r"\$receiving_email_address\s*=\s*'([^']*)'",source)
        actions=[f['action'] for p in pages for f in p['forms']]
        observations.append(['Residual contact template backend','forms/contact.php remains present. Configured receiving address: '+(match.group(1) if match else '(not detected)')+'. Current HTML form actions: '+', '.join(actions)])
    report.table(['Observation','Pages / current value'],observations)
    add('h2','Stylesheet and script references')
    references={}
    for p in pages:
        for asset in p['stylesheets']+p['scripts']:
            references.setdefault(asset,[]).append(p['file'])
    report.table(['Reference','Used by'],[[asset,', '.join(files)] for asset,files in references.items()])
    add('h2','Favicons')
    report.table(['Page','Link relation','Path'],[[p['file'],*icon] for p in pages for icon in p['icons']])
    add('h2','Downloadable documents')
    pdfs=linked_pdfs(pages)
    report.table(['Local PDF file','Referenced by'],[[path.relative_to(ROOT).as_posix(),', '.join(p['file'] for p in pages if any(unquote(urlsplit(row[1]).path)==path.relative_to(ROOT).as_posix() for row in p['links']))] for path in pdfs])
    add('p','Each original linked PDF is preserved in Content_Source_Snapshot.zip. Its unmodified pages are appended to the PDF version of this reference; the Word/HTML/Markdown versions identify the documents rather than rewriting them. View and download labels and requested filenames appear in the page-specific link tables.')
    add('h2','Source snapshot and verification')
    add('p','Content_Source_Snapshot.zip contains the captured HTML files, custom CSS and JavaScript, referenced local images and PDF documents, and the residual form/readme files. Source_Manifest.json records SHA-256 checksums. Content_Inventory.json contains the structured page inventory; Browser_Capture.json preserves the browser-parsed DOM and text. Vendor libraries are identified by reference rather than copied into the source archive.')
    add('p','The page transcripts are checked against every non-hidden text fragment inside each main element. Source hashes are checked before and after generation to confirm the website files remain unchanged. The generated PDF is checked for text coverage and readable page bounds.')
    add('h1','Owner notes and future updates')
    add('p','These notes are editable in documentation/notes.json. They are not current website copy and are kept separately from the exact page transcripts.')
    for note in notes.get('general',[]):
        add('p',note)
    for file,values in notes.get('pages',{}).items():
        if values:
            add('h2',file)
            for note in values:
                add('p',note)
    if not notes.get('general') and not any(notes.get('pages',{}).values()):
        add('p','No owner notes have been added yet.')
    return report


CSS = '''
@page { size: A4; margin: 19mm 17mm 19mm;
  @top-left { content: "FARAH SAYARI / PORTFOLIO REFERENCE"; font: 8pt Arial; color: #52716d; }
  @bottom-left { content: "Local source content record"; font: 8pt Arial; color: #63706e; }
  @bottom-right { content: counter(page); font: 8pt Arial; color: #63706e; }
}
* { box-sizing: border-box; }
body { color:#263634; font:10pt/1.55 Arial, sans-serif; margin:0 auto; max-width:180mm; }
.cover { padding:35mm 0 18mm; border-bottom:3px solid #34b7a7; }
.eyebrow { letter-spacing:2px; color:#247569; font-size:10pt; }
.cover h1 { font-size:34pt; letter-spacing:-1px; margin:12px 0; color:#173e38; }
.subtitle { font-size:23pt; margin:0 0 18px; }
.date { color:#53726c; }
h1.chapter { break-before:page; font-size:23pt; line-height:1.2; color:#173e38; border-bottom:2px solid #34b7a7; padding-bottom:12px; margin:0 0 20px; }
h2 { font-size:14pt; color:#216c60; margin:24px 0 10px; }
h3 { font-size:11pt; margin:20px 0 8px; color:#173e38; }
h1,h2,h3 { break-after:avoid; }
p { margin:0 0 10px; orphans:3; widows:3; }
.copy { border-left:2px solid #c4e6df; padding-left:12px; color:#1e2927; }
.copy-heading { font-size:11pt; font-weight:bold; margin:16px 0 8px; break-after:avoid; }
.copy-bullet { padding-left:18px; text-indent:-10px; }
.copy-bullet::before { content:"• "; color:#248477; }
.code { font:10pt Consolas, monospace; padding:12px; background:#eff7f4; border:1px solid #c4e6df; }
table { border-collapse:collapse; width:100%; table-layout:fixed; font-size:8.4pt; margin:10px 0 18px; }
th,td { padding:7px 8px; border:1px solid #d3dfdc; vertical-align:top; overflow-wrap:anywhere; }
th { background:#e8f5f1; color:#204e45; text-align:left; }
thead { display:table-header-group; }
tr { break-inside:avoid; }
@media screen { body { padding:35px; max-width:1000px; } }
'''


def write_html(report, output):
    parts=['<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Farah Sayari — Portfolio Documentation</title><style>'+CSS+'</style></head><body>']
    for item in report.items:
        kind=item['kind']; text=html.escape(item['text'])
        if kind=='cover':
            parts.append(f'<div class="cover"><p class="eyebrow">WEBSITE DOCUMENTATION</p><h1>{text}</h1><p class="subtitle">{html.escape(item["subtitle"])}</p><p class="date">{item["date"]} · Africa/Tunis</p></div>')
        elif kind=='table':
            header=''.join('<th>'+html.escape(str(cell) or '(empty)')+'</th>' for cell in item['headers'])
            rows=''.join('<tr>'+''.join('<td>'+html.escape(str(cell) or '(empty)')+'</td>' for cell in row)+'</tr>' for row in item['rows'])
            parts.append(f'<table><thead><tr>{header}</tr></thead><tbody>{rows}</tbody></table>')
        elif kind in {'h1','h2','h3'}:
            parts.append(f'<{kind} class="{"chapter" if kind=="h1" else ""}">{text}</{kind}>')
        else:
            parts.append(f'<p class="{kind}">{text}</p>')
    parts.append('</body></html>')
    output.write_text('\n'.join(parts),encoding='utf-8')


def write_markdown(report, output):
    parts=[]
    for item in report.items:
        kind,text=item['kind'],item['text']
        if kind=='cover':
            parts += ['# '+text, item['subtitle'],item['date']+' · Africa/Tunis']
        elif kind=='table':
            def row(cells):
                return '| '+' | '.join((str(c) or '(empty)').replace('|','\\|').replace('\n',' ') for c in cells)+' |'
            parts += [row(item['headers']),row(['---']*len(item['headers'])),*[row(r) for r in item['rows']]]
        elif kind in {'h1','h2','h3'}:
            parts.append('#'*(int(kind[1])+1)+' '+text)
        elif kind=='code':
            parts.append('```text\n'+text+'\n```')
        elif kind=='copy-heading':
            parts.append('**'+text+'**')
        elif kind=='copy-bullet':
            parts.append('> • '+text)
        elif kind=='copy':
            parts.append('> '+text)
        else:
            parts.append(text)
        parts.append('')
    output.write_text('\n'.join(parts),encoding='utf-8')


def write_docx(report, output, date):
    # Office Open XML, using only Python's standard library.
    ns='http://schemas.openxmlformats.org/wordprocessingml/2006/main'
    def paragraph(text,style='Normal'):
        return f'<w:p><w:pPr><w:pStyle w:val="{style}"/></w:pPr><w:r><w:t xml:space="preserve">{xml_escape(str(text))}</w:t></w:r></w:p>'
    body=[]
    for item in report.items:
        kind,text=item['kind'],item['text']
        if kind=='cover':
            body += [paragraph(text,'Title'),paragraph(item['subtitle'],'Subtitle'),paragraph(item['date']+' · Africa/Tunis')]
        elif kind=='table':
            rows=[]
            count=len(item['headers'])
            widths=[int(10100/count)]*count
            for i,row in enumerate([item['headers'],*item['rows']]):
                cells=''.join(f'<w:tc><w:tcPr><w:tcW w:w="{widths[j]}" w:type="dxa"/>'+('<w:shd w:fill="E8F5F1"/>' if i==0 else '')+'</w:tcPr>'+paragraph(cell or '(empty)','TableText')+'</w:tc>' for j,cell in enumerate(row))
                rows.append('<w:tr><w:trPr><w:cantSplit/>'+('<w:tblHeader/>' if i==0 else '')+'</w:trPr>'+cells+'</w:tr>')
            body.append('<w:tbl><w:tblPr><w:tblW w:w="10100" w:type="dxa"/><w:tblBorders>'+''.join(f'<w:{edge} w:val="single" w:sz="4" w:color="D3DFDC"/>' for edge in ['top','left','bottom','right','insideH','insideV'])+'</w:tblBorders></w:tblPr><w:tblGrid>'+''.join(f'<w:gridCol w:w="{w}"/>' for w in widths)+'</w:tblGrid>'+''.join(rows)+'</w:tbl>')
        else:
            style={'h1':'Heading1','h2':'Heading2','h3':'Heading3','copy-heading':'CopyHeading','copy':'Copy','copy-bullet':'Copy','code':'Code'}.get(kind,'Normal')
            body.append(paragraph(('• ' if kind=='copy-bullet' else '')+text,style))
    section='<w:sectPr><w:footerReference w:type="default" r:id="rIdFooter"/><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1077" w:right="963" w:bottom="1077" w:left="963" w:header="500" w:footer="500"/></w:sectPr>'
    document=f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:document xmlns:w="{ns}" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><w:body>'+''.join(body)+section+'</w:body></w:document>'
    styles=f'''<?xml version="1.0" encoding="UTF-8"?><w:styles xmlns:w="{ns}">
      <w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="20"/><w:color w:val="263634"/></w:rPr></w:rPrDefault><w:pPrDefault><w:pPr><w:spacing w:after="140" w:line="290" w:lineRule="auto"/></w:pPr></w:pPrDefault></w:docDefaults>
      <w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/></w:style>
      <w:style w:type="paragraph" w:styleId="Title"><w:name w:val="Title"/><w:pPr><w:spacing w:before="1800" w:after="300"/></w:pPr><w:rPr><w:b/><w:sz w:val="64"/><w:color w:val="173E38"/></w:rPr></w:style>
      <w:style w:type="paragraph" w:styleId="Subtitle"><w:name w:val="Subtitle"/><w:rPr><w:sz w:val="40"/><w:color w:val="216C60"/></w:rPr></w:style>
      <w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:pPr><w:keepNext/><w:pageBreakBefore/><w:outlineLvl w:val="0"/><w:spacing w:after="300"/></w:pPr><w:rPr><w:b/><w:sz w:val="42"/><w:color w:val="173E38"/></w:rPr></w:style>
      <w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/><w:pPr><w:keepNext/><w:outlineLvl w:val="1"/><w:spacing w:before="280" w:after="140"/></w:pPr><w:rPr><w:b/><w:sz w:val="28"/><w:color w:val="216C60"/></w:rPr></w:style>
      <w:style w:type="paragraph" w:styleId="Heading3"><w:name w:val="heading 3"/><w:pPr><w:keepNext/><w:outlineLvl w:val="2"/></w:pPr><w:rPr><w:b/><w:sz w:val="22"/></w:rPr></w:style>
      <w:style w:type="paragraph" w:styleId="CopyHeading"><w:name w:val="Website heading"/><w:pPr><w:keepNext/><w:spacing w:before="240"/></w:pPr><w:rPr><w:b/><w:sz w:val="22"/></w:rPr></w:style>
      <w:style w:type="paragraph" w:styleId="Copy"><w:name w:val="Website copy"/><w:pPr><w:ind w:left="160"/></w:pPr></w:style>
      <w:style w:type="paragraph" w:styleId="TableText"><w:name w:val="Table text"/><w:pPr><w:spacing w:before="80" w:after="80"/></w:pPr><w:rPr><w:sz w:val="17"/></w:rPr></w:style>
      <w:style w:type="paragraph" w:styleId="Code"><w:name w:val="Command"/><w:rPr><w:rFonts w:ascii="Consolas" w:hAnsi="Consolas"/></w:rPr></w:style>
    </w:styles>'''
    relationships='<?xml version="1.0" encoding="UTF-8"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rIdStyles" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/><Relationship Id="rIdFooter" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer1.xml"/></Relationships>'
    footer=f'<w:ftr xmlns:w="{ns}"><w:p><w:pPr><w:jc w:val="right"/></w:pPr><w:r><w:t>Farah Sayari · Portfolio reference | </w:t></w:r><w:r><w:fldChar w:fldCharType="begin"/></w:r><w:r><w:instrText> PAGE </w:instrText></w:r><w:r><w:fldChar w:fldCharType="end"/></w:r></w:p></w:ftr>'
    content_types='<?xml version="1.0" encoding="UTF-8"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/><Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/><Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/><Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/></Types>'
    package_rels='<?xml version="1.0" encoding="UTF-8"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rIdDocument" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/><Relationship Id="rIdCore" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/></Relationships>'
    core=f'<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:title>Farah Sayari — Portfolio Documentation</dc:title><dc:creator>Farah Sayari</dc:creator><dc:description>Local portfolio content reference, {date.isoformat()}</dc:description></cp:coreProperties>'
    with ZipFile(output,'w',ZIP_DEFLATED) as package:
        for name,data in {'[Content_Types].xml':content_types,'_rels/.rels':package_rels,'word/document.xml':document,'word/styles.xml':styles,'word/_rels/document.xml.rels':relationships,'word/footer1.xml':footer,'docProps/core.xml':core}.items():
            package.writestr(name,data.encode('utf-8'))


def browser_path(explicit=None):
    candidates=[explicit,os.environ.get('PORTFOLIO_BROWSER'),shutil.which('google-chrome'),shutil.which('chromium'),shutil.which('msedge'),
        'C:/Program Files/Google/Chrome/Application/chrome.exe','C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe']
    return next((str(p) for p in candidates if p and Path(p).is_file()),None)


def linked_pdfs(pages):
    paths=[]
    for page in pages:
        for row in page['links']:
            uri=urlsplit(row[1])
            if not uri.scheme and not uri.netloc and uri.path.lower().endswith('.pdf'):
                path=(ROOT/unquote(uri.path)).resolve()
                if path.is_relative_to(ROOT) and path.is_file() and path not in paths:
                    paths.append(path)
    return paths


def collect_source_files(pages=None):
    paths=set(ROOT.glob('*.html'))
    for relative in ['assets/css','assets/js','forms']:
        paths.update(p for p in (ROOT/relative).rglob('*') if p.is_file())
    paths.update(p for p in [ROOT/'Readme.txt'] if p.exists())
    paths.update(p for p in (ROOT/'assets/docs').rglob('*') if p.is_file())
    if pages:
        for page in pages:
            paths.update(ROOT/unquote(urlsplit(row[0]).path) for row in page['images'])
            paths.update(ROOT/unquote(urlsplit(row[1]).path) for row in page['icons'])
    else:
        paths.update(p for p in (ROOT/'assets/img').rglob('*') if p.is_file())
    return sorted(p for p in paths if p.is_file())


def hashes(files):
    return {p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}


def verify_copy(pages):
    for page in pages:
        dom=Tree(page['_html']).root.find('main')
        combined=' '.join(b['text'] for b in page['copy'])
        for node in dom.walk():
            if hidden(node) or node.tag in {'script','style','svg'} or any(a.tag in {'script','style','svg'} for a in node.ancestors()):
                continue
            for child in node.children:
                if isinstance(child,str) and normalize(child):
                    assert normalize(child) in combined, (page['file'],normalize(child))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--date',help='Snapshot date, YYYY-MM-DD; defaults to today in Africa/Tunis')
    parser.add_argument('--browser',help='Path to Chrome or Edge')
    parser.add_argument('--no-pdf',action='store_true',help='Generate editable outputs only')
    args=parser.parse_args()
    date=datetime.strptime(args.date,'%Y-%m-%d').date() if args.date else datetime.now(ZoneInfo('Africa/Tunis')).date()
    browser=browser_path(args.browser)
    if not browser:
        raise SystemExit('Chrome or Edge was not found. Supply --browser PATH.')
    if not shutil.which('node'):
        raise SystemExit('Node.js 22 or later is required for browser capture.')
    baseline=hashes(collect_source_files())
    capture_path=HERE/'Browser_Capture.json'
    subprocess.run(['node',str(HERE/'capture-site.cjs'),str(ROOT),str(capture_path),browser],check=True,timeout=100)
    captures=json.loads(capture_path.read_text(encoding='utf-8'))
    pages=build_inventory(captures)
    for page,capture in zip(pages,captures):
        page['_html']=capture['html']
    verify_copy(pages)
    for page in pages:
        del page['_html']
    inventory={'snapshot_date':date.isoformat(),'timezone':'Africa/Tunis','pages':pages}
    (HERE/'Content_Inventory.json').write_text(json.dumps(inventory,ensure_ascii=False,indent=2),encoding='utf-8')
    notes_path=HERE/'notes.json'
    if not notes_path.exists():
        notes_path.write_text(json.dumps({'general':[],'pages':{}},indent=2)+'\n',encoding='utf-8')
    report=make_report(pages,date,json.loads(notes_path.read_text(encoding='utf-8')))
    write_html(report,HERE/(STEM+'.html'))
    write_markdown(report,HERE/(STEM+'.md'))
    write_docx(report,HERE/(STEM+'.docx'),date)
    files=collect_source_files(pages)
    manifest={'snapshot_date':date.isoformat(),'algorithm':'SHA-256','files':hashes(files)}
    (HERE/'Source_Manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    with ZipFile(HERE/'Content_Source_Snapshot.zip','w',ZIP_DEFLATED) as archive:
        for file in files:
            archive.write(file,file.relative_to(ROOT).as_posix())
        archive.writestr('Source_Manifest.json',json.dumps(manifest,indent=2))
    if not args.no_pdf:
        import pymupdf
        output=HERE/(STEM+'.pdf')
        with tempfile.TemporaryDirectory(prefix='portfolio-print-') as temporary:
            raw=Path(temporary)/'reference.pdf'
            command=[browser,'--headless=new','--disable-gpu','--no-first-run','--no-default-browser-check','--no-pdf-header-footer','--user-data-dir='+str(Path(temporary)/'profile'),'--print-to-pdf='+str(raw),(HERE/(STEM+'.html')).as_uri()]
            completed=subprocess.run(command,capture_output=True,timeout=60)
            if completed.returncode or not raw.exists():
                raise RuntimeError('PDF export failed: '+completed.stderr.decode('utf-8',errors='replace')[-1500:])
            document=pymupdf.open(raw)
            # Add navigation bookmarks to the principal documentation sections.
            toc=[]
            for item in report.items:
                if item['kind']=='h1':
                    target=normalize(item['text'])
                    for i,p in enumerate(document):
                        if target in normalize(p.get_text()):
                            toc.append([1,target,i+1]);break
            reference_pages=len(document)
            for attachment in linked_pdfs(pages):
                label='Original downloadable CV' if attachment.name=='Farah_Sayari_CV2026.pdf' else 'PulmoTrack scientific paper' if attachment.name=='PulmoTrackPaper.pdf' else attachment.name
                toc.append([1,'Appendix · '+label,len(document)+1])
                with pymupdf.open(attachment) as original:
                    document.insert_pdf(original)
            document.set_toc(toc)
            document.set_metadata({'title':'Farah Sayari — Portfolio Content Reference','author':'Farah Sayari','subject':'Exact local portfolio content snapshot, '+date.isoformat(),'keywords':'portfolio, documentation, content inventory, Farah Sayari'})
            document.save(output,garbage=4,deflate=True)
            document.close()
        with pymupdf.open(output) as pdf:
            # Exclude running headers/footers so paragraphs spanning two pages
            # remain contiguous when checking the printed reference text.
            pdf_text=normalize(' '.join(pdf[i].get_text(clip=pymupdf.Rect(0,45,pdf[i].rect.width,pdf[i].rect.height-45)) for i in range(reference_pages)))
            # Printed hyphenated words may wrap after an existing hyphen/dash.
            # Compare without layout whitespace as a fallback; preserve output copy.
            compact_pdf=re.sub(r'\s+','',pdf_text)
            missing=[]
            for page in pages:
                for block in page['copy']:
                    values=block['headers']+[cell for row in block['rows'] for cell in row] if block['tag']=='table' else [block['text']]
                    for value in values:
                        if normalize(value) not in pdf_text and re.sub(r'\s+','',value) not in compact_pdf:
                            missing.append((page['file'],value))
            assert not missing, ('PDF content missing',missing[:5])
            print(f'PDF verified: {len(pdf)} pages, every page transcript included.')
    assert baseline==hashes(collect_source_files()), 'Website sources changed during generation.'
    print(f'Finished: {len(pages)} website pages documented. Website sources unchanged.')
    print(HERE/(STEM+'.pdf'))
    print(HERE/(STEM+'.docx'))


if __name__=='__main__':
    main()
