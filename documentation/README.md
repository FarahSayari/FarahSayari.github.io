# Portfolio documentation

Open **Farah_Sayari_Portfolio_Documentation.pdf** to read the complete current reference.
Open **Farah_Sayari_Portfolio_Documentation.docx** in Word or LibreOffice to edit the document.

## Refresh after changing the website

From the portfolio folder, run:

```powershell
python documentation/generate.py
```

Or double-click **Refresh Documentation.cmd** on Windows. The command captures the current local HTML pages in a headless browser and regenerates all documentation outputs. It does not edit the website or submit the contact form. The PDF appends the original linked PDF documents, including the CV and PulmoTrack scientific paper.

Requirements: Python 3.10+, Node.js 22+, Chrome or Edge, and PyMuPDF (`python -m pip install pymupdf` if missing). The date defaults to today in Africa/Tunis. You can supply `--date YYYY-MM-DD`, `--browser "C:/path/to/browser.exe"`, or `--no-pdf` for editable outputs only. The Python timezone database must support Africa/Tunis; on systems without it, install `tzdata` or supply `--date`.

Generated Word, HTML, Markdown, JSON, PDF, and snapshot archive files are replaced on regeneration. Save manual document edits with a different filename. Editing the Word document does not change the website; export it to PDF directly from your word processor for documentation-only revisions. Keep persistent notes in **notes.json**; its general array and page-specific arrays contain plain text notes and are included in a separate owner-notes section.

## Outputs

- `Farah_Sayari_Portfolio_Documentation.pdf`: printable reference with PDF bookmarks and the original linked documents as appendices.
- `Farah_Sayari_Portfolio_Documentation.docx`: editable Word reference. The binary document appendices remain in the PDF and source archive.
- `Farah_Sayari_Portfolio_Documentation.html`: styled source that you can also open and print in a browser.
- `Farah_Sayari_Portfolio_Documentation.md`: plain-text editable copy.
- `Content_Inventory.json`: exact extracted text blocks, metadata, links, assets, fields, video sources and playback settings, and dynamic states for every root HTML page.
- `Browser_Capture.json`: browser-parsed HTML and rendered text for each page, captured with external requests blocked.
- `Source_Manifest.json`: SHA-256 checksums for captured source files.
- `Content_Source_Snapshot.zip`: original HTML, custom CSS/JS, referenced images, PDFs and demonstration videos, plus residual form/readme files. Vendor libraries are referenced rather than archived.

The documentation records all root-level HTML pages, including the retained starter template. HTML entities are decoded and whitespace normalized; visible wording is preserved. Hidden form messages and animated alternatives are documented separately. Source order is preserved for multi-column pages. Explanatory behavior notes reflect the current implementation and should be reviewed if interactions or page structures change substantially.

To keep a dated history, copy this documentation folder before regenerating. `notes.json` is never overwritten when it already exists.

## Publishing the website

Push website changes to `main` in `FarahSayari/FarahSayari.github.io`. The workflow in `.github/workflows/deploy-pages.yml` packages the static HTML, tracked assets, and readable documentation files, then deploys them to GitHub Pages. The Pages publishing source must be set to **GitHub Actions**.

The source snapshot ZIP, browser capture, JSON inventories, and documentation generator stay in the repository and are excluded from the published site artifact. The website's downloadable CV, scientific paper, and demonstration videos remain included. A successful Git push saves the changes in the repository; a successful Pages deployment is required before they appear on the live website.
