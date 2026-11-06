# Farah Sayari
Portfolio content reference
06 November 2026 · Africa/Tunis

An exact content record of the local portfolio: every HTML page, its text, navigation, project entries, links, images, form fields, and dynamic text states.

Snapshot: 2026-11-06 · Africa/Tunis · 12 HTML pages. The source files are the authority for this record.

## Document guide

Website wording is reproduced without rewriting. HTML entities are decoded and layout whitespace is normalized; line wrapping, bullets, and font treatment follow this document. Content follows HTML source order, so a two-column page is read column by column. Hover text and animated alternatives are recorded explicitly.

This is a content reference rather than a screenshot reproduction. Explanatory notes, inventories, and update instructions are separate from the sections marked “Exact page content.” External websites, the map service, and contact delivery were not verified; the contact form was not submitted.

### Pages covered

| No. | Page | Source file | Entry point |
| --- | --- | --- | --- |
| 1 | Home | index.html | Main navigation |
| 2 | About | about.html | Main navigation |
| 3 | Resume | resume.html | Main navigation |
| 4 | Certifications | certifications.html | Main navigation |
| 5 | Services | services.html | Main navigation |
| 6 | Portfolio | portfolio.html | Main navigation |
| 7 | LollyBooks project details | portfolio-details.html | Portfolio detail link |
| 8 | PulmoTrack project details | pulmotrack-details.html | Portfolio detail link |
| 9 | TestPilot project details | testpilot-details.html | Portfolio detail link |
| 10 | Digital Gallery | digital-gallery.html | Main navigation |
| 11 | Contact | contact.html | Main navigation |
| 12 | Starter template | starter-page.html | Retained template; absent from the main navigation |

### How to update this record

To update the website and its documentation: edit the relevant HTML, CSS, JavaScript, image, or CV file, then run the regeneration command below from the portfolio folder.

```text
python documentation/generate.py
```

On Windows, you can also double-click documentation/Refresh Documentation.cmd. The script reads the current website and refreshes the PDF, editable Word file, HTML, Markdown, JSON inventory, and source snapshot archive.

For a documentation-only revision, open the .docx file in Word or LibreOffice and save/export it as PDF. This does not change the website. Regeneration replaces generated outputs, so preserve manual Word edits under a different filename.

Keep ongoing commentary or planned work in documentation/notes.json. Those notes survive regeneration and are labeled separately from current website content.

### Where to make common changes

| Change | Edit these sources |
| --- | --- |
| Home introduction / animated job titles | index.html; animation timing in assets/js/main.js |
| Biography / contact profile / rotating photos | about.html; assets/img/me11.png, me22.png, me33.png |
| Resume text / downloadable CV | resume.html; assets/docs/Farah_Sayari_CV2026.pdf |
| Service titles and descriptions | services.html |
| Digital drawings / gallery introduction | digital-gallery.html; assets/css/collections.css |
| Course certificates / credential links | certifications.html; assets/css/collections.css |
| Project list / filters / thumbnails | portfolio.html; assets/img/portfolio/ and assets/img/masonry-portfolio/ |
| LollyBooks case study | portfolio-details.html; assets/img/portfolio/lollybooks/library-art.webp |
| TestPilot case study | testpilot-details.html; assets/css/portfolio.css |
| PulmoTrack case study / scientific paper | pulmotrack-details.html; assets/docs/PulmoTrackPaper.pdf; assets/img/portfolio/pulmotrack/paper-preview.png |
| Contact text / form fields / delivery endpoint | contact.html, including its inline JavaScript |
| Global header / footer | Repeated in each HTML file; update each affected page |
| Shared visual styles / page-specific styles | assets/css/main.css; assets/css/resume.css; assets/css/portfolio.css; assets/css/collections.css |
| Shared navigation / animations / filtering | assets/js/main.js |

## Shared header, navigation, and footer

Use the table below with the exact variants that follow. Each page’s visible brand, navigation labels, social destinations, footer text, and active navigation item are included.

| Page | Brand | Navigation | Header social | Footer | Active item |
| --- | --- | --- | --- | --- | --- |
| index.html | FARAH | N1 | S1 | F1 | Home |
| about.html | FARAH | N1 | S1 | F1 | About |
| resume.html | FARAH | N1 | S1 | F2 | Resume |
| certifications.html | FARAH | N1 | S1 | F1 | Certifications |
| services.html | FARAH | N1 | S1 | F1 | Services |
| portfolio.html | FARAH | N1 | S1 | F2 | Portfolio |
| portfolio-details.html | FARAH | N1 | S1 | F2 | Portfolio |
| pulmotrack-details.html | FARAH | N1 | S1 | F2 | Portfolio |
| testpilot-details.html | FARAH | N1 | S1 | F2 | Portfolio |
| digital-gallery.html | FARAH | N1 | S1 | F1 | Digital Gallery |
| contact.html | FARAH | N1 | S1 | F2 | Contact |
| starter-page.html | FARAH | N1 | S1 | F3 | (none) |

### Navigation N1

| Exact label (in source order) | Destination |
| --- | --- |
| Home | index.html |
| About | about.html |
| Resume | resume.html |
| Certifications | certifications.html |
| Services | services.html |
| Portfolio | portfolio.html |
| Digital Gallery | digital-gallery.html |
| Contact | contact.html |

### Header social links S1

| Label / icon class | Exact destination |
| --- | --- |
| GitHub | https://github.com/FarahSayari |
| Email | mailto:farahsayari.dev@gmail.com |
| LinkedIn | https://www.linkedin.com/in/farah-sayari-060745248 |

### Footer F1

> © Copyright Farah Sayari All Rights Reserved

> 

| Social label / icon class | Exact destination |
| --- | --- |
| GitHub | https://github.com/FarahSayari |
| Email | mailto:farah.sayari@esprit.tn |
| LinkedIn | https://www.linkedin.com/in/farah-sayari-060745248 |

### Footer F2

> © Copyright Farah Sayari All Rights Reserved

> 

| Social label / icon class | Exact destination |
| --- | --- |
| GitHub | https://github.com/FarahSayari |
| Email | mailto:farahsayari.dev@gmail.com |
| LinkedIn | https://www.linkedin.com/in/farah-sayari-060745248 |

### Footer F3

> © Copyright Kelly All Rights Reserved

> 

| Social label / icon class | Exact destination |
| --- | --- |
| Icon: bi bi-twitter-x | (empty) |
| Icon: bi bi-facebook | (empty) |
| Icon: bi bi-instagram | (empty) |
| Icon: bi bi-linkedin | (empty) |

An empty destination is shown as “(empty)”; a destination of # is a fragment placeholder. The starter template contains a malformed ThemeWagon anchor in its source. Its browser-parsed label and destination above are recorded as they currently resolve.

### Shared interactions and appearance

The site has a sticky header, a mobile navigation toggle, an initial preloader, a scroll-to-top icon, and animation-on-scroll effects. These elements have no additional visible body copy. The scroll-to-top icon uses href="#" and is activated after scrolling past 100 pixels in the current shared script.

| Style token | Current value |
| --- | --- |
| default-font | "Roboto",  system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", "Liberation Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji" |
| heading-font | "Raleway",  sans-serif |
| nav-font | "Poppins",  sans-serif |
| background-color | #ffffff |
| default-color | #444444 |
| heading-color | #222222 |
| accent-color | #34b7a7 |

## 01 · Home

| Page attribute | Exact value |
| --- | --- |
| Source file | index.html |
| Browser title | Farah Sayari Portfolio |
| Language | en |
| Description meta tag | (empty) |
| Keywords meta tag | (empty) |
| Main section IDs | hero |

### Exact page content

**Farah Sayari**

> I'm a Software Engineer|

> Welcome to my digital world!

> About Me

> View Resume

### Animated content and alternate states

The fixed introduction is “I'm a”. The animated span cycles through these exact titles; the cursor displays “|”. The first complete title is used in the transcript above.

> Software Engineer

> Data Scientist

> Digital Artist

| Animation parameter | Current value |
| --- | --- |
| typingSpeed | 110 ms |
| deletingSpeed | 70 ms |
| pauseAfterTyping | 1400 ms |
| pauseAfterDeleting | 300 ms |

### Main-content links and downloads

| Exact label / accessible label | Exact destination | Download filename |
| --- | --- | --- |
| About Me | about.html | (empty) |
| View Resume | resume.html | (empty) |

### Main-content images

| Image path | Exact alternate text | Role |
| --- | --- | --- |
| assets/img/hero-bg.jpg | Abstract hero background for Farah Sayari | (empty) |

## 02 · About

| Page attribute | Exact value |
| --- | --- |
| Source file | about.html |
| Browser title | About - Farah Sayari |
| Language | en |
| Description meta tag | (empty) |
| Keywords meta tag | (empty) |
| Main section IDs | about |

### Exact page content

**About**

> Get to know me, my background, and the kind of digital solutions I enjoy building.

**Junior Software Engineer specialized in Data Science**

> Hi, I’m Farah Sayari. I’m a Software Engineer specialized in Data Science, a book lover, and a creative soul with a passion for digital art.

> I build smart, practical, and user-friendly solutions using AI, Machine Learning, Deep Learning, automation, and full-stack development. Logic helps me build. Imagination helps me create.

> • Email: farahsayari.dev@gmail.com

> • Phone: +216 28528390

> • Linkedin: linkedin.com/in/farah-sayari-060745248

> • Degree: Software Engineering – Data Science

> • Github: github.com/FarahSayari

> • Freelance: Open to opportunities

> I’m open to junior opportunities in Software Engineering, Data Science, and AI.

### Animated content and alternate states

The 3 profile images alternate in a continuous loop. Current switch interval: 500 ms. Image paths and exact alternate text are in the image inventory below.

### Main-content links and downloads

| Exact label / accessible label | Exact destination | Download filename |
| --- | --- | --- |
| farahsayari.dev@gmail.com | mailto:farahsayari.dev@gmail.com | (empty) |
| linkedin.com/in/farah-sayari-060745248 | https://www.linkedin.com/in/farah-sayari-060745248 | (empty) |
| github.com/FarahSayari | https://github.com/FarahSayari | (empty) |

### Main-content images

| Image path | Exact alternate text | Role |
| --- | --- | --- |
| assets/img/me11.png | Farah Sayari profile photo 1 | (empty) |
| assets/img/me22.png | Farah Sayari profile photo 2 | (empty) |
| assets/img/me33.png | Farah Sayari profile photo 3 | (empty) |

## 03 · Resume

| Page attribute | Exact value |
| --- | --- |
| Source file | resume.html |
| Browser title | Resume - Farah Sayari |
| Language | en |
| Description meta tag | Explore Farah Sayari's resume: AI and software engineering experience, education, technical skills, and projects in Data Science and agentic AI. |
| Keywords meta tag | (absent) |
| Main section IDs | resume |

The source has two columns: summary, education, skills, languages, and activities first; professional experience and projects second. The text below follows that source order. The downloadable CV is a separate PDF and is appended to the final PDF reference unchanged.

### Exact page content

**Resume**

> AI & Software Engineer specializing in Data Science, agentic AI, and full-stack development.

> Download CV (PDF)

**Summary**

**Farah Sayari**

> Software Engineer specializing in Data Science, with hands-on experience in Machine Learning, Deep Learning, agentic AI, and full-stack development. I build intelligent, data-driven applications and am seeking a full-time opportunity in AI, Data Science, or Software Engineering.

> • Ariana, Tunisia

> • +216 28 528 390

> • farahsayari.dev@gmail.com

> • GitHub · LinkedIn

**Education**

**Engineering Cycle in Computer Science – Data Science**

> Sep 2023 – Nov 2026

> ESPRIT – Private Higher School of Engineering and Technology

**Bachelor’s Degree in Computer Systems Engineering – Embedded Systems & IoT**

> Sep 2020 – Jun 2023

> Faculty of Sciences of Bizerte

**Technical Skills**

**Programming**

> Python, Java, JavaScript, R, C

**AI & Machine Learning**

> Scikit-learn, TensorFlow, Keras, PyTorch, MLflow, Deep Learning, NLP, Recommendation Systems

**Generative AI & Agents**

> LLMs, RAG, LangChain, LangGraph, Qdrant, Ollama, Prompt Engineering

**Backend & Frontend**

> Spring Boot, FastAPI, Flask, Angular, React, REST APIs

**Data Engineering & Analytics**

> SQL, PostgreSQL, Hadoop, Talend, Data Warehousing, Power BI, Time Series Analysis

**DevOps & Tools**

> Git, Docker, GitHub Actions, Jenkins, Linux, Cypress, Kubernetes

**Languages**

> • Arabic Native

> • French C2

> • English C1

**Activities & Awards**

> • IEEE Computational Intelligence Society (CIS) — ESPRIT Chapter, 2025.

> • Bal des Projets — ESPRIT (2024 & 2025) — Academic projects pre-selected for both editions.

> • IEEEXtreme 17.0 & 18.0 — Participant.

> • University English Competition (2024) — 3rd Place.

> Interests: Reading & Literature, Digital Art & Illustration.

**Professional Experience**

**AI & Full-Stack Software Engineer Intern**

> Feb – Aug 2026

> VERMEG · PFE Internship

> TestPilot — AI-Assisted Test Automation Platform

> • Designed and developed a full-stack test automation platform using Angular, Spring Boot, FastAPI, and PostgreSQL, enabling QA teams to manage, generate, and execute automated tests.

> • Engineered a hybrid agentic AI pipeline using Python, LangGraph, and LLMs to transform recorded user interactions into structured test models and executable Cypress scripts.

> • Developed a Chrome extension (Manifest V3) to capture browser interactions and implemented LLM-assisted script repair with validation and controlled retries.

> • Integrated Cypress test execution, automated reporting, GitHub Actions CI/CD, and Docker to support continuous testing and deployment.

**Data Scientist Intern**

> Jul – Aug 2025

> Esprit-Tech · Summer Internship

> Clustering Algorithms for Heterogeneous Student Groups

> • Implemented and compared multiple clustering algorithms, achieving a 0.72 Silhouette Score, and built an interactive Streamlit dashboard to visualize and evaluate results.

> • Developed an automated group formation pipeline integrated into the backend, supporting teachers in forming balanced and diverse student teams.

**Projects**

**LollyBooks**

> Oct – Present · Ongoing

> Co-Founder & Software Engineer

> Personalized Digital Library & AI Reading Companion

> • Co-designed and developed an interactive digital library featuring customizable bookshelves, reading analytics, and goal tracking.

> • Integrated the Open Library REST API and Goodreads CSV processing to automate book metadata retrieval and reading history imports.

> • Prototyped recommendations based on reading preferences and mood, and designed an LLM-powered reading companion for conversational book discovery.

**Aura**

> Oct – Present · Ongoing

> AI & Software Engineer

> Agentic AI Career Assistant

> • Redesigning a local, agentic AI assistant to automate job discovery and match job descriptions with personal skills and experience.

> • Developing an LLM-powered application assistant to generate tailored cover letters, analyze CV compatibility, and recommend targeted resume improvements.

> • Adapting RAG, semantic search, and agent orchestration using LangChain, LangGraph, and Qdrant to support personalized job search and application workflows.

### Main-content links and downloads

| Exact label / accessible label | Exact destination | Download filename |
| --- | --- | --- |
| Download CV (PDF) | assets/docs/Farah_Sayari_CV2026.pdf | Farah_Sayari_CV2026.pdf |
| +216 28 528 390 | tel:+21628528390 | (empty) |
| farahsayari.dev@gmail.com | mailto:farahsayari.dev@gmail.com | (empty) |
| GitHub | https://github.com/FarahSayari | (empty) |
| LinkedIn | https://www.linkedin.com/in/farah-sayari-060745248 | (empty) |

## 04 · Certifications

| Page attribute | Exact value |
| --- | --- |
| Source file | certifications.html |
| Browser title | Certifications - Farah Sayari |
| Language | en |
| Description meta tag | Courses and certifications from my learning journey. |
| Keywords meta tag | (empty) |
| Main section IDs | certifications |

### Exact page content

**Certifications**

> Courses and certifications from my learning journey.

**Always learning.**

> A place to share the certificates I earn through courses and continued learning.

> My course certificates are coming soon.

## 05 · Services

| Page attribute | Exact value |
| --- | --- |
| Source file | services.html |
| Browser title | Services - Farah Sayari |
| Language | en |
| Description meta tag | (empty) |
| Keywords meta tag | (empty) |
| Main section IDs | services |

### Exact page content

**Services**

> Here are the areas where I enjoy building, experimenting, and creating digital solutions.

**Data Science & AI**

> Building intelligent solutions with machine learning, deep learning, data analysis, and AI-powered workflows.

**Web Development**

> Creating practical and user-friendly web applications using modern frontend and backend technologies.

**AI Agents & Automation**

> Designing smart agents, RAG pipelines, and automated workflows that help reduce manual tasks and improve decision-making.

**Test Automation & QA**

> Working on automated testing workflows, test generation, execution, and reporting to improve software reliability.

**Data Analytics & BI**

> Transforming raw data into clear insights using dashboards, reporting tools, statistics, and business intelligence techniques.

**Creative Digital Work**

> Exploring digital art, visual design, and friendly UI ideas to make technology feel more human and engaging.

> I like combining logic, data, creativity, and usability to build solutions that are both smart and pleasant to use.

## 06 · Portfolio

| Page attribute | Exact value |
| --- | --- |
| Source file | portfolio.html |
| Browser title | Portfolio - Farah Sayari |
| Language | en |
| Description meta tag | Explore Farah Sayari's projects in software engineering, Data Science, and AI, starting with LollyBooks. |
| Keywords meta tag | (absent) |
| Main section IDs | portfolio |

The portfolio uses a masonry grid with project labels in hover overlays. The image inventory below records the current thumbnails. Entries with no description or detail links are recorded as placeholders.

### Exact page content

**Portfolio**

> A selection of my work in software engineering, Data Science, and AI.

> • All

> • App

> • Web

**LollyBooks**

> Personalized Digital Library & AI Reading Companion

**AI Agent Recruiter**

**TestPilot**

> AI-Assisted Test Automation Platform

**PulmoTrack**

> AI-Powered Pulmonary Nodule Analysis

### Project entries and filter membership

| Project | Description | Filters | Detail destination |
| --- | --- | --- | --- |
| LollyBooks | Personalized Digital Library & AI Reading Companion | App, Web | portfolio-details.html |
| AI Agent Recruiter | (empty) | App | (none) |
| TestPilot | AI-Assisted Test Automation Platform | App | testpilot-details.html |
| PulmoTrack | AI-Powered Pulmonary Nodule Analysis | Web | pulmotrack-details.html |

The default filter is All. Filter membership and every existing detail destination are listed in the table above. Project image preview links open the lightbox. Entries without detail links remain unlinked. The filter controls also support Enter and Space in the current inline script.

### Main-content links and downloads

| Exact label / accessible label | Exact destination | Download filename |
| --- | --- | --- |
| Preview LollyBooks artwork | assets/img/portfolio/lollybooks/library-art.jpg | (empty) |
| LollyBooks project details | portfolio-details.html | (empty) |
| TestPilot project details | testpilot-details.html | (empty) |
| PulmoTrack project details | pulmotrack-details.html | (empty) |

### Main-content images

| Image path | Exact alternate text | Role |
| --- | --- | --- |
| assets/img/portfolio/lollybooks/library-art.jpg | Cozy pink bookshelves with string lights and a My Reading Library neon sign | (empty) |
| assets/img/masonry-portfolio/masonry-portfolio-2.jpg | (empty) | presentation |
| assets/img/portfolio/testpilot/TESTPILOT%20AI%20Automation%20Platform.png | TestPilot logo and AI-Assisted Test Automation Platform title on a purple gradient background | (empty) |
| assets/img/portfolio/pulmotrack/pulmotrack.png | PulmoTrack project artwork illustrating CT-based nodule detection, segmentation, and classification | (empty) |

## 07 · LollyBooks project details

| Page attribute | Exact value |
| --- | --- |
| Source file | portfolio-details.html |
| Browser title | LollyBooks - Farah Sayari |
| Language | en |
| Description meta tag | LollyBooks: a personalized digital library and AI reading companion. Discover Farah Sayari's contributions as Co-Founder and Software Engineer. |
| Keywords meta tag | (absent) |
| Main section IDs | portfolio-details |

### Exact page content

> Back to Portfolio

**LollyBooks — Personalized Digital Library & AI Reading Companion**

> A cozy digital space to track your reading journey, discover new books, and build a library that reflects your personality.

**Project Information**

> • Category: Web Application · Personalization & Recommendation Systems

> • Project Type: Personal Startup Project

> • Role: Co-Founder & Software Engineer

> • Project Date: October 2026 – Present

> • Status: Active Development (Functional Prototype)

> • Project URL: Coming Soon

**Your Library, Your Stories, Your Little World**

> LollyBooks is a personalized digital library designed to make reading tracking more engaging, accessible, and enjoyable.

> The idea was born from a personal passion for reading and the desire to create a beautiful virtual bookshelf where readers can preserve their reading journey, even without owning physical copies of their books.

> As a Co-Founder and Software Engineer, I contributed to the product vision, interface design, and development of the initial web application prototype, combining interactive book management, reading analytics, and personalized book discovery.

**Key Features & Contributions**

> • Interactive Digital Library: Developed customizable virtual bookshelves with multiple display modes, allowing readers to organize their collections visually.

> • Book Data Integration: Integrated the Open Library REST API for automated metadata retrieval and implemented Goodreads CSV importing to migrate reading histories, ratings, and reviews.

> • Reading Analytics & Goals: Implemented reading statistics, progress tracking, and personalized reading goals to help users reflect on their reading habits.

> • Personalized Recommendations: Prototyped a recommendation system based on reading history, ratings, genre preferences, and reading moods.

> • Reading Companion: Designed a conversational recommendation experience to help readers discover books aligned with their interests and preferences.

**Project Vision & Future Development**

> LollyBooks is evolving from a functional prototype into a scalable, AI-powered reading platform.

> The long-term vision includes an LLM-powered reading companion, deeper personalization through reading reviews and preferences, multilingual support, community features, and a production-ready architecture.

> The goal is to create more than a book-tracking application: a personal reading universe that grows and evolves with every reader.

### Main-content links and downloads

| Exact label / accessible label | Exact destination | Download filename |
| --- | --- | --- |
| Back to Portfolio | portfolio.html | (empty) |

### Main-content images

| Image path | Exact alternate text | Role |
| --- | --- | --- |
| assets/img/portfolio/lollybooks/library-art.webp | Cozy pink bookshelves with string lights and a My Reading Library neon sign | (empty) |

## 08 · PulmoTrack project details

| Page attribute | Exact value |
| --- | --- |
| Source file | pulmotrack-details.html |
| Browser title | PulmoTrack - Farah Sayari |
| Language | en |
| Description meta tag | Explore Farah Sayari's PulmoTrack LUNA16 CT research: candidate screening, true/false nodule classification, exploratory segmentation, notebook evaluations, and a live Streamlit showcase. |
| Keywords meta tag | (absent) |
| Main section IDs | portfolio-details, research-paper |

### Exact page content

> Back to Portfolio

**PulmoTrack — Deep Learning for Pulmonary Nodule Analysis**

> Research · Deep Learning · Medical Imaging · Computer Vision

> An academic medical-imaging project using LUNA16 CT scans to study nodule candidate detection, binary classification and exploratory 3D segmentation, presented through an interactive research website.

> Previous image

> Next image

**Project Information**

> • Category: Research, DL, Medical Imaging, Computer Vision

> • Role: Data Scientist, Project Manager

> • Methodology: CRISP-DM

> • Dataset: LUNA16

> • Status: Completed

> • Scientific Paper: Available · Team research manuscript

> Open Live Showcase (opens in a new tab)

> View Source on GitHub (opens in a new tab)

**Technologies**

> Research: Python, PyTorch, torchvision, NumPy, pandas, SciPy, scikit-learn, SimpleITK.

> Analysis & delivery: Jupyter Notebook, Google Colab, Matplotlib, Plotly, Pillow, Streamlit, Git, GitHub and Streamlit Community Cloud.

**Project Summary**

> Jump directly to a section of the project.

> • Project Information

> • Technologies

> • Project Overview

> • My Contributions

> • LUNA16 Dataset

> • Project Methodology

> • Explore the Three DSOs DSO1 — Nodule Detection Data Processing Models Applied Results & Evaluation DSO2 — Nodule Classification Data Processing Models Applied Results & Evaluation DSO3 — Exploratory 3D Segmentation Data Processing Models Applied Results & Evaluation

> • Deployment

> • Research Paper Paper-reported LUNA16 highlights

**Project Overview**

> Lung cancer is the leading cause of cancer-related death worldwide and is often diagnosed at an advanced stage, when treatment options are more limited. Earlier identification and appropriate follow-up can improve the opportunity for effective treatment.

> PulmoTrack explores how deep learning can analyze pulmonary nodules in volumetric CT data. The project connects medical-image preprocessing, three research objectives, model evaluation and a deployed interface that makes the experiments understandable to a portfolio audience.

> The work is an academic research study. Its recorded models evaluate nodule candidates and masks; they do not establish a clinically validated cancer diagnosis system.

> Scientific context: World Health Organization — Lung cancer.

**My Contributions**

> • LUNA16 preprocessing. Worked on CT resampling, annotation and candidate inspection, world-to-voxel coordinate conversion, intensity normalization and 3D patch preparation.

> • Detection and classification. Developed and studied 3D candidate-screening and binary classification approaches, comparing their saved training histories, confusion matrices and ROC evaluations.

> • Exploratory segmentation. Investigated 3D U-Net, attention and residual-attention variants, and tiny-nodule oversampling, documenting both promising summaries and difficult positive-only cases.

> • Results and documentation. Organized notebook outputs, kept evaluation cohorts and checkpoint results distinct, and contributed to the team research manuscript.

> • Deployment. Created a Streamlit research showcase with CT visualizations, model overviews, result interpretation, source resources and access to the research paper.

**LUNA16 Dataset**

> LUNA16 (Lung Nodule Analysis 2016) is derived from LIDC-IDRI and contains 888 volumetric chest CT scans. It provides CT volumes, candidate locations and nodule annotations for pulmonary nodule research.

> The official reference standard includes nodules at least 3 mm in diameter accepted by at least three of four radiologists. Scans with slice thickness greater than 2.5 mm were excluded. The CT collection is approximately 90 GB in scale; the deployed showcase uses saved outputs rather than distributing the dataset.

> The project prepares different patch collections for different experiments: 64³ voxels for detection/classification and 48³ voxels for the archived segmentation studies.

> Dataset source and access: LUNA16 official data page.

**Project Methodology**

> PulmoTrack follows the CRISP-DM methodology, from understanding the research problem and preparing LUNA16 CT data to modeling, evaluation, and deployment. This iterative workflow guides the three research objectives and the presentation of their results in the Streamlit showcase.

**Explore the Three DSOs**

> Data processing prepares the CT scans for learning; modeling builds and trains networks using that prepared data. Before preparing the task-specific datasets, we resampled CT volumes to 1 × 1 × 1 mm voxel spacing and converted annotation coordinates from millimetres to voxel locations using each scan’s origin and spacing, accounting for medical-image order (x, y, z) and NumPy array order (z, y, x).

> The evaluation tables preserve each saved checkpoint’s recorded cohort. Accuracy is calculated from the original confusion matrix, while ROC-AUC comes from the corresponding recorded output.

**DSO1 — Nodule Detection**

> This objective screens supplied candidate locations. Each input is a 3D patch around a candidate, and the output is a nodule or non-nodule label.

**Data Processing**

> • Candidate matching: Compared candidates with annotated nodule centres from the same scan. A distance below 5 mm defined the strict positive label for the selected dataset; preparation also explored a looser 10 mm label.

> • Dataset selection: Retained 1,215 positive candidates and randomly sampled 8,000 negatives, producing 9,215 patches. The larger negative collection exposes the model to varied non-nodule appearances.

> • Patch extraction: Extracted 64 × 64 × 64 patches around candidates and padded border patches to preserve the expected dimensions.

> • Normalization and tensors: Subtracted each patch’s mean and divided by its standard deviation, then created one-channel tensors with shape (1, 64, 64, 64).

> • Dataset split: Used a seeded random patch split of 6,451 training, 1,843 validation and 921 test examples.

**Models Applied**

> Applied a U-Net-style 3D encoder classifier with 32 → 64 → 128 → 256 feature channels. Convolution and pooling build 3D features, followed by global average pooling and a linear head that produces two class scores. This model has no segmentation decoder and predicts a patch label, rather than a boundary or bounding box.

> Training used weighted focal loss (γ = 2), Adam with learning rate 0.0001, batch size 16 and 20 recorded epochs. Class weights emphasize less frequent positive examples, while focal loss concentrates learning on difficult cases. The lowest validation loss determined the selected checkpoint.

**Results & Evaluation**

| Cohort | Patches | Accuracy | ROC-AUC |
| --- | --- | --- | --- |
| Validation | 1,843 | 98.37% | 0.9928 |
| Test | 921 | 97.83% | 0.9961 |

> DSO1 — Test-set confusion matrix.

> DSO1 — Test-set ROC curve; AUC is rounded in the plot legend.

> DSO1 — Training and validation history.

> On the 921-patch test cohort, the saved model correctly identifies 112 of 121 nodule patches (92.56% sensitivity), with 11 false positives and 9 false negatives. These are candidate-level outcomes; they do not establish false positives per full CT scan.

> Interpretation: The test accuracy of 97.83% and ROC-AUC of 0.9961 show strong separation on the recorded candidate cohort. Sensitivity of 92.56% also makes the remaining nine missed nodule patches visible.

**DSO2 — Nodule Classification**

> The recorded task classifies a 3D candidate patch as a true nodule or false nodule. Although the wider project discusses benign/malignant classification, these implemented evaluations use binary candidate labels.

**Data Processing**

> • Separate patch collection: Prepared this dataset independently of the 9,215 detection examples. The preparation cell filters candidates marked as class 1 and compares their positions with annotation centres using a 6 mm matching threshold.

> • Patch extraction and normalization: Extracted 64 × 64 × 64 patches, padded when needed, and applied mean-and-standard-deviation normalization.

> • Labels and storage: Saved tensors into separate folders, with label 1 for true nodules and 0 for false nodules.

> • Dataset and initial split: The notebook reports 1,243 true-nodule and 761 false-nodule patches, totalling 2,004. The initial split contains 1,603 training, 200 validation and 201 test patches.

**Models Applied**

> • Improved 3D CNN: Three convolution blocks followed by adaptive pooling, a dense layer, dropout and a two-class output; 17 recorded epochs.

> • ResNet3D Lite: Residual blocks combine transformed features with shortcut connections, followed by global pooling and a classification head; 6 recorded epochs.

> • U-Net encoder classifier: Four encoder stages followed by global pooling and a dense two-class head; 30 recorded epochs.

> All three architectures use cross-entropy loss and Adam with an initial learning rate of 0.0001. Dropout regularizes the CNN and U-Net heads. Validation loss guides checkpoint selection, and saved evaluations are kept separate from final-epoch logs.

**Results & Evaluation**

| Study / cohort | Patches | Accuracy | ROC-AUC |
| --- | --- | --- | --- |
| Improved 3D CNN · validation | 200 | 74.50% | 0.8269 |
| Improved 3D CNN · test | 201 | 74.63% | 0.8335 |
| ResNet3D Lite · validation | 401 | 72.07% | 0.7678 |
| U-Net encoder · validation | 200 | 74.00% | 0.8116 |

> DSO2 — Improved 3D CNN training and validation history.

> The Improved 3D CNN test evaluation identifies 107 of 123 true-nodule patches, with 35 false positives and 16 false negatives. Its accuracy and AUC describe binary candidate labels, not malignancy diagnosis.

> How to compare these results. Each model retains its own recorded cohort. The ResNet matrix contains 401 patches despite an earlier 200-patch validation log. Splitting is by patch, and a patient-disjoint benchmark is not established. These studies support analysis of the recorded runs, not a controlled architecture ranking.

> Interpretation: The Improved 3D CNN reaches 74.63% test accuracy and ROC-AUC 0.8335 on its 201-patch cohort. Its 35 false positives and 16 false negatives show the remaining classification errors. The differing evaluation cohorts prevent treating these recorded runs as a controlled ranking of the three architectures.

**DSO3 — Exploratory 3D Segmentation**

> This objective predicts a mask identifying nodule voxels within a 3D CT patch. It is a parallel research exploration, rather than a prerequisite for detection or classification.

**Data Processing**

> • Volume preparation: Prepared lung regions, clipped intensities to −1000 to 400 HU and scaled them to the range [0, 1].

> • Reference masks: Created spherical masks from annotated nodule centres and diameters. These approximate reference regions are not manually traced nodule boundaries.

> • Patch extraction: Extracted 48 × 48 × 48 positive CT patches with corresponding mask patches. Negative patches were sampled away from annotated nodules and paired with empty masks.

> • Augmentation and normalization: Explored flips, rotations, zoom, noise and intensity shifts, with patch-level min–max normalization in the model loader.

> • Splits and tiny nodules: The baseline records 2,036 training and 509 validation patches. Later experiments oversampled selected small-nodule examples to increase their exposure during training.

**Models Applied**

> The segmentation flow is CT patch → encoder → bottleneck → decoder → voxel probability map. Decoder upsampling and encoder-to-decoder skip connections help reconstruct spatial detail.

> • 3D U-Net: Baseline encoder–decoder architecture.

> • Attention 3D U-Net: Attention gates weight features passed through skip connections.

> • Residual Attention 3D U-Net: Residual convolution blocks combined with attention gates.

> • Tiny-nodule training: Baseline architecture with modified sampling and augmentation.

> Recorded training used binary cross-entropy loss and Adam at 0.0001. A sigmoid produces voxel probabilities, and a 0.5 threshold converts them into binary masks.

**Results & Evaluation**

> Segmentation results depend strongly on the selected patches and the handling of empty masks. The table preserves these separate experimental contexts; all values are notebook-reported summaries.

| Model study | Evaluation context | Patches | Reported score |
| --- | --- | --- | --- |
| 3D U-Net | Five positives · A | 5 | Dice 0.2115 |
| 3D U-Net | Five positives · B | 5 | Dice 0.3127 |
| 3D U-Net | Mixed validation loader | 509 | Dice 0.9504 |
| Attention U-Net | Five positive patches | 5 | Dice 0.1599 |
| Attention U-Net | Ten mixed patches | 10 | Dice 0.9800 |
| Residual attention | Ten positives · initial | 10 | Dice 0.1200 |
| Residual attention | Ten positives · later | 10 | Dice 0.0348 |

> DSO3 — Baseline 3D U-Net training and validation loss.

> The 0.9504 validation Dice comes from a mixed, augmented loader, where smoothing assigns empty prediction/reference pairs a Dice near 1. The attention model’s mixed-patch evaluator similarly assigns perfect scores to empty pairs. Positive-only samples show the remaining difficulty of recovering small nodule regions.

> Tiny-nodule augmentation retains saved prediction examples and a final validation binary cross-entropy loss of 0.0446. No Dice, precision, recall or F1 evaluation was recorded for that run; a lower loss is not an overlap score.

> Recorded Attention 3D U-Net positive-nodule example — Dice 0.8000, precision 0.8630, recall 0.7456. Single case from the ten-patch mixed evaluation.

> Evaluation context: The notebook applies random augmentation to images and masks through separate calls, so their spatial transformations are not guaranteed to match; validation also inherits augmentation. Patch splits do not establish patient-disjoint evaluation. Together with the mixed-versus-positive-only score differences, these limitations keep the segmentation findings exploratory.

**Deployment**

> My PulmoTrack contribution is hosted on Streamlit Community Cloud, with the GitHub repository as its deployment source. The interface preserves the dark navy and teal medical-imaging identity, sidebar navigation and CT-focused visual presentation.

> Visitors can explore model architectures, recorded metrics, training histories, original segmentation predictions, pilot Grad-CAM, research resources and the manuscript viewer. The app presents saved evidence; it requires no CT dataset download or live model execution.

> Delivery workflow: Research notebooks → exported figures and result summaries → Streamlit interface → GitHub → Streamlit Community Cloud.

> The website is a completed research showcase, rather than a patient-upload or diagnostic inference service. Repository changes can be reflected in the deployed app through Community Cloud’s GitHub integration.

> Open Live Showcase (opens in a new tab)

> View Source on GitHub (opens in a new tab)

> Deployment reference: Streamlit Community Cloud documentation.

**Research Paper**

> Title: PulmoTrack: A Deep Learning Solution for Pulmonary Nodule Segmentation, Detection, and Classification on CT and Chest X-ray Scans

> Document: Team research manuscript · May 2025 · 11 pages.

> Authors: Farah Sayari and co-authors.

> The manuscript covers the broader team project, including CT and chest X-ray work. This portfolio page focuses on the LUNA16 CT contribution.

**Paper-reported LUNA16 highlights**

> The manuscript reports segmentation Dice 0.95, detection sensitivity 92% at 1.5 false positives per scan, and classification AUC 0.91 (pp. 4–5).

> View Paper (PDF) (opens in a new tab)

> Download Paper (PDF)

### Animated content and alternate states

The project image card contains 2 manually switchable images. Previous/next buttons, slide indicators, keyboard navigation, and touch swipes select an image. Automatic rotation is disabled; the first image is initially selected.

| Slide | Image path |
| --- | --- |
| 1 | assets/img/portfolio/pulmotrack/pulmotrack.png |
| 2 | assets/img/portfolio/pulmotrack/team.png |

### Main-content links and downloads

| Exact label / accessible label | Exact destination | Download filename |
| --- | --- | --- |
| Back to Portfolio | portfolio.html | (empty) |
| Open the live PulmoTrack research showcase (opens in a new tab) | https://pulmotrack-farahsayari-contribution-sef2wgqdo5bzl9wmgfwxry.streamlit.app/ | (empty) |
| Enlarge the PulmoTrack team photo | assets/img/portfolio/pulmotrack/team.png | (empty) |
| Open Live Showcase (opens in a new tab) | https://pulmotrack-farahsayari-contribution-sef2wgqdo5bzl9wmgfwxry.streamlit.app/ | (empty) |
| View Source on GitHub (opens in a new tab) | https://github.com/FarahSayari/pulmoTrack-farahsayari-contribution | (empty) |
| Project Information | #project-info-title | (empty) |
| Technologies | #technologies | (empty) |
| Project Overview | #project-overview | (empty) |
| My Contributions | #my-contributions | (empty) |
| LUNA16 Dataset | #luna16-dataset | (empty) |
| Project Methodology | #project-methodology | (empty) |
| Explore the Three DSOs | #research-objectives | (empty) |
| DSO1 — Nodule Detection | #dso1-title | (empty) |
| Data Processing | #dso1-data-processing | (empty) |
| Models Applied | #dso1-models-applied | (empty) |
| Results & Evaluation | #detection-results-title | (empty) |
| DSO2 — Nodule Classification | #dso2-title | (empty) |
| Data Processing | #dso2-data-processing | (empty) |
| Models Applied | #dso2-models-applied | (empty) |
| Results & Evaluation | #classification-results-title | (empty) |
| DSO3 — Exploratory 3D Segmentation | #dso3-title | (empty) |
| Data Processing | #dso3-data-processing | (empty) |
| Models Applied | #dso3-models-applied | (empty) |
| Results & Evaluation | #segmentation-results-title | (empty) |
| Deployment | #deployment | (empty) |
| Research Paper | #research-paper-title | (empty) |
| Paper-reported LUNA16 highlights | #paper-reported-highlights | (empty) |
| World Health Organization — Lung cancer | https://www.who.int/news-room/fact-sheets/detail/lung-cancer | (empty) |
| LUNA16 official data page | https://luna16.grand-challenge.org/Data/ | (empty) |
| Enlarge the PulmoTrack project methodology diagram | assets/img/portfolio/pulmotrack/methodology.png | (empty) |
| Enlarge the nodule detection illustration | assets/img/portfolio/pulmotrack/Nodule%20detection.png | (empty) |
| Enlarge the nodule detection model architecture | assets/img/portfolio/pulmotrack/arch%20detection.png | (empty) |
| Enlarge detection test-set confusion matrix with 789 true negatives, 11 false positives, 9 false negatives and 112 true positives | assets/img/portfolio/pulmotrack/02_dso1_test_confusion_matrix.png | (empty) |
| Enlarge detection test-set ROC curve | assets/img/portfolio/pulmotrack/03_dso1_test_roc_curve.png | (empty) |
| Enlarge detection training and validation loss and accuracy across 20 epochs | assets/img/portfolio/pulmotrack/07_dso1_training_history.png | (empty) |
| Enlarge the nodule classification illustration | assets/img/portfolio/pulmotrack/Nodule%20classification.png | (empty) |
| Enlarge the nodule classification model architecture | assets/img/portfolio/pulmotrack/arch%20classification.png | (empty) |
| Enlarge improved 3D CNN training and validation loss and accuracy across 17 epochs | assets/img/portfolio/pulmotrack/08_dso2_training_history.png | (empty) |
| Enlarge the exploratory segmentation illustration | assets/img/portfolio/pulmotrack/Exploratory%20segmentation.png | (empty) |
| Enlarge the nodule segmentation model architecture | assets/img/portfolio/pulmotrack/arch%20segmentation.png | (empty) |
| Enlarge 3D U-Net training and validation loss across 50 epochs | assets/img/portfolio/pulmotrack/09_dso3_training_loss.png | (empty) |
| Enlarge the recorded Attention 3D U-Net positive-nodule prediction | assets/img/portfolio/pulmotrack/attention-positive-prediction.png | (empty) |
| Open Live Showcase (opens in a new tab) | https://pulmotrack-farahsayari-contribution-sef2wgqdo5bzl9wmgfwxry.streamlit.app/ | (empty) |
| View Source on GitHub (opens in a new tab) | https://github.com/FarahSayari/pulmoTrack-farahsayari-contribution | (empty) |
| Streamlit Community Cloud documentation | https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app | (empty) |
| View Paper (PDF) (opens in a new tab) | assets/docs/PulmoTrackPaper.pdf | (empty) |
| Download Paper (PDF) | assets/docs/PulmoTrackPaper.pdf | PulmoTrackPaper.pdf |

### Main-content images

| Image path | Exact alternate text | Role |
| --- | --- | --- |
| assets/img/portfolio/pulmotrack/pulmotrack.png | PulmoTrack concept artwork illustrating CT-based nodule detection, segmentation, and classification | (empty) |
| assets/img/portfolio/pulmotrack/team.png | PulmoTrack project team standing together | (empty) |
| assets/img/portfolio/pulmotrack/methodology.png | PulmoTrack CRISP-DM workflow: business understanding, data understanding, data preparation, modeling, evaluation, and deployment | (empty) |
| assets/img/portfolio/pulmotrack/Nodule%20detection.png | PulmoTrack nodule detection concept illustration showing candidate nodules highlighted on a CT scan | (empty) |
| assets/img/portfolio/pulmotrack/arch%20detection.png | Nodule detection architecture: CT preprocessing and patch extraction followed by a 3D encoder, bottleneck, global average pooling, and a nodule/non-nodule classification head | (empty) |
| assets/img/portfolio/pulmotrack/02_dso1_test_confusion_matrix.png | Detection test-set confusion matrix with 789 true negatives, 11 false positives, 9 false negatives and 112 true positives | (empty) |
| assets/img/portfolio/pulmotrack/03_dso1_test_roc_curve.png | Detection test-set ROC curve | (empty) |
| assets/img/portfolio/pulmotrack/07_dso1_training_history.png | Detection training and validation loss and accuracy across 20 epochs | (empty) |
| assets/img/portfolio/pulmotrack/Nodule%20classification.png | PulmoTrack classification concept artwork depicting the broader benign/malignant project goal; the recorded evaluations below use true/false nodule labels | (empty) |
| assets/img/portfolio/pulmotrack/arch%20classification.png | Improved 3D CNN concept architecture showing CT preprocessing, patch extraction, convolution blocks, pooling and a classification head; the recorded evaluations use true/false nodule labels | (empty) |
| assets/img/portfolio/pulmotrack/08_dso2_training_history.png | Improved 3D CNN training and validation loss and accuracy across 17 epochs | (empty) |
| assets/img/portfolio/pulmotrack/Exploratory%20segmentation.png | PulmoTrack segmentation concept illustration showing a CT patch, reference mask, predicted mask and 3D U-Net; recorded evaluation contexts are detailed below | (empty) |
| assets/img/portfolio/pulmotrack/arch%20segmentation.png | 3D U-Net segmentation architecture: CT preprocessing, patch extraction, encoder, bottleneck, decoder with skip connections, and output nodule masks | (empty) |
| assets/img/portfolio/pulmotrack/09_dso3_training_loss.png | 3D U-Net training and validation loss across 50 epochs | (empty) |
| assets/img/portfolio/pulmotrack/attention-positive-prediction.png | Five CT slices with reference and predicted masks from a recorded Attention 3D U-Net positive-nodule case; Dice 0.8000, precision 0.8630, recall 0.7456 | (empty) |

## 09 · TestPilot project details

| Page attribute | Exact value |
| --- | --- |
| Source file | testpilot-details.html |
| Browser title | TestPilot - Farah Sayari |
| Language | en |
| Description meta tag | TestPilot, an AI-assisted test automation platform developed by Farah Sayari during her end-of-studies internship at VERMEG, turns recorded browser interactions into validated Cypress tests. |
| Keywords meta tag | (absent) |
| Main section IDs | portfolio-details |

### Exact page content

> Back to Portfolio

**TestPilot — AI-Assisted Test Automation Platform**

> Full-Stack Engineering · Agentic AI · Test Automation · DevOps

> Developed during my end-of-studies internship (PFE) at VERMEG, TestPilot is an AI-assisted regression testing platform that transforms recorded browser interactions into structured test scenarios and automated Cypress tests, integrating AI-powered generation, human validation, and test management.

> Previous image

> Next image

**Project Information**

> • Category: Software Engineering · Agentic AI · Test Automation

> • Project Type: End-of-Studies Internship (PFE)

> • Company: VERMEG

> • Role: Full-Stack & AI Software Engineer

> • Duration: February – August 2026

> • Methodology: Scrumban

> • Status: Completed — Functional Prototype

**Technologies & Tools**

> Frontend: Angular

> Backend: Java · Spring Boot · Spring Security · REST APIs

> AI & Agentic Workflows: Python · FastAPI · LangGraph · LLMs · Ollama · Gemma

> Browser Automation: Chrome Extension (Manifest V3) · Cypress · JavaScript

> Database: PostgreSQL

> DevOps & Infrastructure: Docker · Nginx · GitHub Actions · CI/CD

**Project Summary**

> Jump directly to a section of the project.

> • Project Information

> • Technologies & Tools

> • Project Overview

> • The Challenge

> • The Solution End-to-End Workflow Execution Modes

> • Development Methodology — Scrumban

> • My Contributions Full-Stack Application Development Browser Recording & Test Automation Agentic AI Pipeline DevOps & Integration

> • AI Architecture — Controlled Agentic Automation Agent 1 — Scenario Processing Agent 2 — Test Model Generation Agent 3 — Cypress Script Generation

> • Additional Capabilities Test Management AI Assistance Chatbot CI/CD Integration

> • Demonstrations & Validation Demo 1 — From Scenario Recording to Automated Testing Demo 2 — CI/CD-Triggered Regression Testing Demonstration Application — SauceDemo

> • Key Takeaways

**Project Overview**

> Developed during my end-of-studies internship at VERMEG, TestPilot is a full-stack, AI-assisted platform designed to streamline regression testing.

> It enables Business Analysts and QA Engineers to record application workflows, transform them into structured test models, and generate automated Cypress scripts through a hybrid agentic AI pipeline.

> The platform goes beyond test generation by integrating test management, script validation, human approval, automated execution, and reporting.

> Through Docker and GitHub Actions, TestPilot also supports continuous testing within CI/CD workflows, connecting test automation to the software delivery process.

> The objective is to make regression testing more efficient, reliable, and traceable while keeping human oversight at the center of the process.

**The Challenge**

> In complex software environments, frequent updates make regression testing essential to ensure applications remain stable and reliable.

> Although test automation tools already exist, creating and maintaining test scripts still requires significant manual effort. QA teams must write scripts, update them as applications evolve, and manage test executions.

> This repetitive work takes time, increases the risk of human errors, and can slow down software delivery. AI can help automate these tasks, but generated tests still need to be reviewed and validated.

> The challenge: How can we reduce the manual effort of creating and maintaining automated regression tests while ensuring their reliability and keeping human control?

**The Solution**

> TestPilot brings the different stages of regression testing into a single platform, combining browser recording, AI-assisted test generation, automated validation, test management, and execution.

> The platform supports four user roles — Admin, Business Analyst (BA), QA Engineer, and QA Manager — each with responsibilities and permissions tailored to the testing workflow.

> Rather than relying entirely on AI-generated code, TestPilot follows a structured process where test assets are progressively generated, validated, and reviewed before execution.

**End-to-End Workflow**

> • Record: Capture real user interactions through a custom Chrome extension.

> • Process: Transform recorded actions into structured scenarios, variables, and reliable locators.

> • Generate: Produce a Test Model and an executable Cypress script draft.

> • Validate: Verify the generated script through automated execution.

> • Review & Approve: Allow QA teams to inspect and approve validated scripts.

> • Manage & Execute: Organize regression campaigns through Test Plans and Test Cycles, then analyze execution results.

**Execution Modes**

> TestPilot supports three ways to execute regression test cycles:

> • Manual Execution: Launch a test cycle directly from the platform.

> • Scheduled Execution: Automatically run test cycles at predefined times.

> • CI/CD-Triggered Execution: Automatically trigger regression cycles through GitHub Actions as part of a software delivery pipeline.

> By combining AI-assisted automation, role-based collaboration, and flexible execution modes, TestPilot simplifies regression testing while maintaining traceability, reliability, and human control.

**Development Methodology — Scrumban**

> TestPilot was developed using Scrumban, combining the iterative approach of Scrum with the flexibility of Kanban.

> Development was organized around a prioritized backlog, incremental feature delivery, and regular progress reviews.

> The project evolved through successive stages, from the full-stack foundation and browser recording extension to the AI generation pipeline, test management, validation, and CI/CD integration.

> This approach allowed me to continuously test new features, address technical challenges, and refine the platform based on feedback throughout the internship.

**My Contributions**

> I was responsible for designing and developing the platform across its principal components.

**Full-Stack Application Development**

> • Developed the web application using Angular, Spring Boot, and PostgreSQL.

> • Implemented REST APIs, authentication, role-based access control, and project management features.

> • Built interfaces for scenario recording, test management, script validation, and execution reporting.

**Browser Recording & Test Automation**

> • Developed a Chrome extension using Manifest V3 to capture browser interactions and relevant page observations.

> • Implemented action processing, locator selection, and variable extraction to reconstruct recorded workflows.

> • Integrated Cypress for automated test validation and regression execution.

**Agentic AI Pipeline**

> • Designed a hybrid architecture combining deterministic processing with controlled LLM assistance.

> • Developed workflows for scenario processing, Test Model generation, and Cypress script generation.

> • Integrated AI-assisted script improvement with validation feedback and bounded execution controls.

**DevOps & Integration**

> • Containerized application services using Docker.

> • Integrated GitHub Actions for CI/CD workflows.

> • Connected automated regression execution with reporting and traceability mechanisms.

**AI Architecture — Controlled Agentic Automation**

> At the core of TestPilot is a hybrid agentic AI pipeline, built using the LangGraph framework and powered by a locally hosted LLM (Gemma via Ollama).

> The architecture combines deterministic processing with controlled LLM assistance to transform recorded browser interactions into automated tests through three specialized agents:

**Agent 1 — Scenario Processing**

> Cleans and structures recorded interactions, extracts variables, and identifies suitable element locators.

**Agent 2 — Test Model Generation**

> Transforms processed actions into a structured Test Model containing test steps, preconditions, variables, and proposed assertions.

**Agent 3 — Cypress Script Generation**

> Converts the Test Model into an executable Cypress test script draft.

> All three agents are orchestrated using LangGraph, while the local LLM provides assistance for generation, enrichment, and improvement when needed.

> Rather than relying entirely on LLM-generated outputs, TestPilot follows a hybrid approach that combines deterministic logic with AI assistance to improve consistency and reliability.

> Generated scripts undergo automated validation and human review before being approved for official test execution, ensuring that AI supports the testing process without replacing human control.

**Additional Capabilities**

**Test Management**

> TestPilot includes a test management module for organizing Test Cases, Test Plans, and Test Cycles, allowing QA teams to manage regression campaigns and follow execution results.

**AI Assistance Chatbot**

> TestPilot features an intelligent assistant powered by a locally hosted Gemma LLM, designed to help users navigate the platform, understand testing workflows, and access relevant project information.

> Built with LangGraph and Retrieval-Augmented Generation (RAG), the chatbot combines application documentation with real-time project data retrieved through secure, read-only tools.

> To improve reliability and reduce AI hallucinations, I implemented several safeguards:

> • Evidence-grounded responses: The assistant retrieves relevant information before answering and provides validated supporting sources.

> • Hallucination reduction: When information is missing or insufficient, it acknowledges its limitations rather than generating unsupported answers.

> • Role-based access: Project information is retrieved according to the user's permissions, preventing unauthorized access.

> • Controlled AI behavior: The assistant operates within predefined tools and execution limits, without modifying data or performing sensitive actions.

**CI/CD Integration**

> GitHub Actions integration demonstrates how regression campaigns can be triggered within a software delivery workflow, with execution results retrieved for reporting.

**Demonstrations & Validation**

> To demonstrate TestPilot's capabilities, I used SauceDemo, an external sample e-commerce application, as a controlled testing environment.

> The demonstrations cover the complete testing workflow, from recording user interactions and generating automated tests to triggering regression campaigns through CI/CD.

**Demo 1 — From Scenario Recording to Automated Testing**

> This demonstration illustrates how TestPilot transforms a recorded business scenario into an executable automated test.

> It covers:

> • Recording browser interactions using the Chrome extension.

> • Processing the recorded actions.

> • Generating the structured Test Model.

> • Generating the Cypress script.

> • Validating the generated script.

> Your browser does not support embedded video. Watch the scenario recording demo (MP4).

> Video: Scenario Recording & AI Generation Demo

**Demo 2 — CI/CD-Triggered Regression Testing**

> This demonstration showcases TestPilot's integration with GitHub Actions.

> A code change is pushed to the separate SauceDemo application repository, triggering an automated CI/CD workflow.

> The workflow deploys the updated test application in the controlled demonstration environment, starts a TestPilot regression cycle, and retrieves its execution results.

> This illustrates how TestPilot can integrate regression testing into a continuous delivery workflow without requiring manual execution of every test campaign.

> Your browser does not support embedded video. Watch the CI/CD regression testing demo (MP4).

> Video: Automated Regression Testing with GitHub Actions

**Demonstration Application — SauceDemo**

> Both demonstrations use SauceDemo, a publicly available sample e-commerce application developed by Sauce Labs.

> SauceDemo was used exclusively as an external application under test and is not part of TestPilot's original development.

> Credits: SauceDemo — Sauce Labs (opens in a new tab)

**Key Takeaways**

> Developing TestPilot gave me hands-on experience in building a complete software engineering solution that combines full-stack development, agentic AI, browser automation, and DevOps.

> One of the most important lessons was that reliable AI-assisted automation requires more than generating code. It also depends on structured processing, validation, traceability, and human oversight.

> This project strengthened my ability to design interconnected services, solve integration challenges, and build practical AI-powered tools that support real software engineering workflows.

### Animated content and alternate states

The project image card contains 7 manually switchable images. Previous/next buttons, slide indicators, keyboard navigation, and touch swipes select an image. Automatic rotation is disabled; the first image is initially selected.

| Slide | Image path |
| --- | --- |
| 1 | assets/img/portfolio/testpilot/testpilot%20first%20pict.png |
| 2 | assets/img/portfolio/testpilot/select%20project.png |
| 3 | assets/img/portfolio/testpilot/admin%20dashboard.png |
| 4 | assets/img/portfolio/testpilot/BA%20dashboard.png |
| 5 | assets/img/portfolio/testpilot/record.png |
| 6 | assets/img/portfolio/testpilot/QA%20engineer%20dashboard.png |
| 7 | assets/img/portfolio/testpilot/qa%20manager%20dashboard.png |

### Main-content links and downloads

| Exact label / accessible label | Exact destination | Download filename |
| --- | --- | --- |
| Back to Portfolio | portfolio.html | (empty) |
| Enlarge TestPilot project artwork | assets/img/portfolio/testpilot/testpilot%20first%20pict.png | (empty) |
| Enlarge Project selection | assets/img/portfolio/testpilot/select%20project.png | (empty) |
| Enlarge Administrator dashboard | assets/img/portfolio/testpilot/admin%20dashboard.png | (empty) |
| Enlarge Business Analyst dashboard | assets/img/portfolio/testpilot/BA%20dashboard.png | (empty) |
| Enlarge Scenario recording | assets/img/portfolio/testpilot/record.png | (empty) |
| Enlarge QA Engineer dashboard | assets/img/portfolio/testpilot/QA%20engineer%20dashboard.png | (empty) |
| Enlarge QA Manager dashboard | assets/img/portfolio/testpilot/qa%20manager%20dashboard.png | (empty) |
| Project Information | #project-info-title | (empty) |
| Technologies & Tools | #technologies-tools | (empty) |
| Project Overview | #project-overview | (empty) |
| The Challenge | #the-challenge | (empty) |
| The Solution | #the-solution | (empty) |
| End-to-End Workflow | #end-to-end-workflow | (empty) |
| Execution Modes | #execution-modes | (empty) |
| Development Methodology — Scrumban | #development-methodology-scrumban | (empty) |
| My Contributions | #my-contributions | (empty) |
| Full-Stack Application Development | #full-stack-application-development | (empty) |
| Browser Recording & Test Automation | #browser-recording-test-automation | (empty) |
| Agentic AI Pipeline | #agentic-ai-pipeline | (empty) |
| DevOps & Integration | #devops-integration | (empty) |
| AI Architecture — Controlled Agentic Automation | #ai-architecture-controlled-agentic-automation | (empty) |
| Agent 1 — Scenario Processing | #agent-1-scenario-processing | (empty) |
| Agent 2 — Test Model Generation | #agent-2-test-model-generation | (empty) |
| Agent 3 — Cypress Script Generation | #agent-3-cypress-script-generation | (empty) |
| Additional Capabilities | #additional-capabilities | (empty) |
| Test Management | #test-management | (empty) |
| AI Assistance Chatbot | #ai-assistance-chatbot | (empty) |
| CI/CD Integration | #ci-cd-integration | (empty) |
| Demonstrations & Validation | #demonstrations-validation | (empty) |
| Demo 1 — From Scenario Recording to Automated Testing | #scenario-demo-title | (empty) |
| Demo 2 — CI/CD-Triggered Regression Testing | #cicd-demo-title | (empty) |
| Demonstration Application — SauceDemo | #demonstration-application-saucedemo | (empty) |
| Key Takeaways | #key-takeaways | (empty) |
| Enlarge the AI-Powered Regression Testing Workflow illustration | assets/img/portfolio/testpilot/AI-Powered%20Regression%20Testing%20Workflow.png | (empty) |
| Enlarge the TestPilot AI architecture diagram | assets/img/portfolio/testpilot/ai%20arch.png | (empty) |
| Enlarge the TestPilot AI Assistance Showcase | assets/img/portfolio/testpilot/TestPilot%20AI%20Assistance%20Showcase.png | (empty) |
| Watch the scenario recording demo (MP4) | assets/videos/testpilot-recorded-scenario.mp4 | (empty) |
| Watch the CI/CD regression testing demo (MP4) | assets/videos/testpilot-ci-cd-demo.mp4 | (empty) |
| SauceDemo — Sauce Labs (opens in a new tab) | https://www.saucedemo.com/ | (empty) |

### Main-content images

| Image path | Exact alternate text | Role |
| --- | --- | --- |
| assets/img/portfolio/testpilot/testpilot%20first%20pict.png | TestPilot project artwork showing its AI-assisted test automation dashboard and recording-to-execution workflow | (empty) |
| assets/img/portfolio/testpilot/select%20project.png | TestPilot project selection screen showing available workspaces and project-specific user roles | (empty) |
| assets/img/portfolio/testpilot/admin%20dashboard.png | TestPilot administrator dashboard showing users, projects, environments and administrative activity | (empty) |
| assets/img/portfolio/testpilot/BA%20dashboard.png | TestPilot Business Analyst dashboard showing scenario totals, test design progress and review tasks | (empty) |
| assets/img/portfolio/testpilot/record.png | TestPilot scenario recording form with project context, environment selection and scenario details | (empty) |
| assets/img/portfolio/testpilot/QA%20engineer%20dashboard.png | TestPilot QA Engineer dashboard showing automation validation tasks, ready test cases and execution results | (empty) |
| assets/img/portfolio/testpilot/qa%20manager%20dashboard.png | TestPilot QA Manager dashboard showing test plans, scheduled executions, cycle readiness and campaign results | (empty) |
| assets/img/portfolio/testpilot/AI-Powered%20Regression%20Testing%20Workflow.png | Illustration of manual test-script maintenance, campaign management and results analysis, with AI-generated scripts awaiting human review | (empty) |
| assets/img/portfolio/testpilot/ai%20arch.png | Diagram of TestPilot's three LangGraph agents with Spring Boot orchestration, local Gemma through Ollama, and automated validation and human review | (empty) |
| assets/img/portfolio/testpilot/TestPilot%20AI%20Assistance%20Showcase.png | TestPilot AI assistance showcase with example chatbot responses, documentation sources, role-based read-only access and bounded AI behavior | (empty) |

### Demonstration videos

#### Demo 1 — From Scenario Recording to Automated Testing

| Source file | Media type |
| --- | --- |
| assets/videos/testpilot-recorded-scenario.mp4 | video/mp4 |

| Playback attribute | Value |
| --- | --- |
| Poster image | assets/img/portfolio/testpilot/record.png |
| Controls | True |
| Autoplay | False |
| Inline playback | True |
| Preload | none |

#### Demo 2 — CI/CD-Triggered Regression Testing

| Source file | Media type |
| --- | --- |
| assets/videos/testpilot-ci-cd-demo.mp4 | video/mp4 |

| Playback attribute | Value |
| --- | --- |
| Poster image | assets/img/portfolio/testpilot/ci-cd-demo-poster.jpg |
| Controls | True |
| Autoplay | False |
| Inline playback | True |
| Preload | none |

## 10 · Digital Gallery

| Page attribute | Exact value |
| --- | --- |
| Source file | digital-gallery.html |
| Browser title | Digital Gallery - Farah Sayari |
| Language | en |
| Description meta tag | A personal collection of my digital drawings, made for the joy of creating. |
| Keywords meta tag | (empty) |
| Main section IDs | digital-gallery |

### Exact page content

**Digital Gallery**

> A personal collection of my digital drawings, made for the joy of creating.

> Spidey Digital drawing

### Main-content links and downloads

| Exact label / accessible label | Exact destination | Download filename |
| --- | --- | --- |
| Enlarge Spidey digital drawing | assets/img/gallery/spidey.png | (empty) |

### Main-content images

| Image path | Exact alternate text | Role |
| --- | --- | --- |
| assets/img/gallery/spidey.png | Spidey digital drawing of a Spider-Man character and a girl above a city skyline, with hearts and sparkles on a purple background | (empty) |

## 11 · Contact

| Page attribute | Exact value |
| --- | --- |
| Source file | contact.html |
| Browser title | Contact - Farah Sayari |
| Language | en |
| Description meta tag | Contact Farah Sayari for software engineering, data science, AI, and collaboration opportunities. |
| Keywords meta tag | Farah Sayari, contact, software engineer, data science, Tunisia |
| Main section IDs | contact |

### Exact page content

**Contact**

> Have an opportunity, project idea, or collaboration in mind? Feel free to reach out.

**Location**

> Ariana, Tunisia

**Email**

> farahsayari.dev@gmail.com

**Phone**

> +216 28528390

**Social Links**

> GitHub | LinkedIn

**Send me a message**

> Your Name

> Your Email

> Subject

> Message

> Send Message

> You can also email me directly at farahsayari.dev@gmail.com.

### Main-content links and downloads

| Exact label / accessible label | Exact destination | Download filename |
| --- | --- | --- |
| farahsayari.dev@gmail.com | mailto:farahsayari.dev@gmail.com | (empty) |
| +216 28528390 | tel:+21628528390 | (empty) |
| GitHub | https://github.com/FarahSayari | (empty) |
| LinkedIn | https://www.linkedin.com/in/farah-sayari-060745248 | (empty) |
| farahsayari.dev@gmail.com | mailto:farahsayari.dev@gmail.com | (empty) |

### Embedded content

| Exact title | Exact embed URL |
| --- | --- |
| Map of Ariana, Tunisia | https://www.google.com/maps?q=Ariana%2C%20Tunisia&output=embed |

### Contact form configuration and field copy

| Attribute | Value |
| --- | --- |
| Form ID | contact-form |
| Method | POST |
| Action | https://formspree.io/f/xgojgjbj |

#### Your Name

| Field attribute | Exact value |
| --- | --- |
| HTML name | name |
| Type | text |
| Placeholder | Your name |
| Default / hidden value | (empty) |
| Required | yes |
| Visibility | visible |

#### Your Email

| Field attribute | Exact value |
| --- | --- |
| HTML name | email |
| Type | email |
| Placeholder | your.email@example.com |
| Default / hidden value | (empty) |
| Required | yes |
| Visibility | visible |

#### Subject

| Field attribute | Exact value |
| --- | --- |
| HTML name | subject |
| Type | text |
| Placeholder | Opportunity / Collaboration / Question |
| Default / hidden value | (empty) |
| Required | yes |
| Visibility | visible |

#### Message

| Field attribute | Exact value |
| --- | --- |
| HTML name | message |
| Type | textarea |
| Placeholder | Write your message here... |
| Default / hidden value | (empty) |
| Required | yes |
| Visibility | visible |

#### _subject

| Field attribute | Exact value |
| --- | --- |
| HTML name | _subject |
| Type | hidden |
| Placeholder | (empty) |
| Default / hidden value | New portfolio message from Farah Sayari website |
| Required | no |
| Visibility | hidden |

#### Website

| Field attribute | Exact value |
| --- | --- |
| HTML name | _gotcha |
| Type | text |
| Placeholder | (empty) |
| Default / hidden value | (empty) |
| Required | no |
| Visibility | hidden |

#### Conditional interface messages

> Loading

> Your message has been sent. Thank you!

> Please complete all fields with a valid email address.

> Message could not be sent. Please email me directly instead.

The browser validates required fields and the email format. On submission the inline script posts FormData to the configured action with Accept: application/json, shows a loading state, and disables the submit button. A successful response resets the form and shows the success message. An invalid form or unsuccessful request shows the corresponding message above. The _gotcha field is the hidden honeypot; the _subject field supplies the notification subject.

## 12 · Starter template

| Page attribute | Exact value |
| --- | --- |
| Source file | starter-page.html |
| Browser title | Starter Page - Kelly Bootstrap Template |
| Language | en |
| Description meta tag | (empty) |
| Keywords meta tag | (empty) |
| Main section IDs | starter-section |

Retained template file. It is not linked from the main navigation or the current project list. Its template copy is reproduced below as part of the complete file inventory.

### Exact page content

**Starter Section**

> Necessitatibus eius consequatur ex aliquid fuga eum quidem sint consectetur velit

> Use this page as a starter for your own custom pages.

## Source inventory and current content differences

### Current differences retained in this record

The document records the website as it exists. These items are observations for future editing; the website was not changed while preparing this reference.

| Observation | Pages / current value |
| --- | --- |
| Header/footer email destinations | farahsayari.dev@gmail.com: about.html, certifications.html, contact.html, digital-gallery.html, index.html, portfolio-details.html, portfolio.html, pulmotrack-details.html, resume.html, services.html, starter-page.html, testpilot-details.html; farah.sayari@esprit.tn: about.html, certifications.html, digital-gallery.html, index.html, services.html |
| Project entries without descriptions or links | AI Agent Recruiter |
| Different project naming | The resume calls its career assistant Aura; the portfolio entry is titled AI Agent Recruiter. This reference does not assume that they are the same project. |
| Retained starter page | starter-page.html. Current brand: FARAH. Its exact content and links are recorded in its section. |
| Residual contact template backend | forms/contact.php remains present. Configured receiving address: contact@example.com. Current HTML form actions: https://formspree.io/f/xgojgjbj |

### Stylesheet and script references

| Reference | Used by |
| --- | --- |
| https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=Raleway:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap | index.html, about.html, resume.html, certifications.html, services.html, portfolio.html, portfolio-details.html, pulmotrack-details.html, testpilot-details.html, digital-gallery.html, contact.html, starter-page.html |
| assets/vendor/bootstrap/css/bootstrap.min.css | index.html, about.html, resume.html, certifications.html, services.html, portfolio.html, portfolio-details.html, pulmotrack-details.html, testpilot-details.html, digital-gallery.html, contact.html, starter-page.html |
| assets/vendor/bootstrap-icons/bootstrap-icons.css | index.html, about.html, resume.html, certifications.html, services.html, portfolio.html, portfolio-details.html, pulmotrack-details.html, testpilot-details.html, digital-gallery.html, contact.html, starter-page.html |
| assets/vendor/aos/aos.css | index.html, about.html, resume.html, certifications.html, services.html, portfolio.html, portfolio-details.html, pulmotrack-details.html, testpilot-details.html, digital-gallery.html, contact.html, starter-page.html |
| assets/vendor/swiper/swiper-bundle.min.css | index.html, about.html, resume.html, certifications.html, services.html, portfolio.html, portfolio-details.html, pulmotrack-details.html, testpilot-details.html, digital-gallery.html, contact.html, starter-page.html |
| assets/vendor/glightbox/css/glightbox.min.css | index.html, about.html, resume.html, certifications.html, services.html, portfolio.html, portfolio-details.html, pulmotrack-details.html, testpilot-details.html, digital-gallery.html, contact.html, starter-page.html |
| assets/css/main.css | index.html, about.html, resume.html, certifications.html, services.html, portfolio.html, portfolio-details.html, pulmotrack-details.html, testpilot-details.html, digital-gallery.html, contact.html, starter-page.html |
| assets/vendor/bootstrap/js/bootstrap.bundle.min.js | index.html, about.html, resume.html, certifications.html, services.html, portfolio.html, portfolio-details.html, pulmotrack-details.html, testpilot-details.html, digital-gallery.html, contact.html, starter-page.html |
| assets/vendor/php-email-form/validate.js | index.html, about.html, resume.html, certifications.html, services.html, portfolio.html, portfolio-details.html, pulmotrack-details.html, testpilot-details.html, digital-gallery.html, starter-page.html |
| assets/vendor/aos/aos.js | index.html, about.html, resume.html, certifications.html, services.html, portfolio.html, portfolio-details.html, pulmotrack-details.html, testpilot-details.html, digital-gallery.html, contact.html, starter-page.html |
| assets/vendor/waypoints/noframework.waypoints.js | index.html, about.html, resume.html, certifications.html, services.html, portfolio.html, portfolio-details.html, pulmotrack-details.html, testpilot-details.html, digital-gallery.html, contact.html, starter-page.html |
| assets/vendor/purecounter/purecounter_vanilla.js | index.html, about.html, resume.html, certifications.html, services.html, portfolio.html, portfolio-details.html, pulmotrack-details.html, testpilot-details.html, digital-gallery.html, contact.html, starter-page.html |
| assets/vendor/swiper/swiper-bundle.min.js | index.html, about.html, resume.html, certifications.html, services.html, portfolio.html, portfolio-details.html, pulmotrack-details.html, testpilot-details.html, digital-gallery.html, contact.html, starter-page.html |
| assets/vendor/glightbox/js/glightbox.min.js | index.html, about.html, resume.html, certifications.html, services.html, portfolio.html, portfolio-details.html, pulmotrack-details.html, testpilot-details.html, digital-gallery.html, contact.html, starter-page.html |
| assets/vendor/imagesloaded/imagesloaded.pkgd.min.js | index.html, about.html, resume.html, certifications.html, services.html, portfolio.html, portfolio-details.html, pulmotrack-details.html, testpilot-details.html, digital-gallery.html, contact.html, starter-page.html |
| assets/vendor/isotope-layout/isotope.pkgd.min.js | index.html, about.html, resume.html, certifications.html, services.html, portfolio.html, portfolio-details.html, pulmotrack-details.html, testpilot-details.html, digital-gallery.html, contact.html, starter-page.html |
| assets/js/main.js | index.html, about.html, resume.html, certifications.html, services.html, portfolio.html, portfolio-details.html, pulmotrack-details.html, testpilot-details.html, digital-gallery.html, contact.html, starter-page.html |
| assets/css/resume.css | resume.html |
| assets/css/collections.css | certifications.html, digital-gallery.html |
| assets/css/portfolio.css | portfolio.html, portfolio-details.html, pulmotrack-details.html, testpilot-details.html |

### Favicons

| Page | Link relation | Path |
| --- | --- | --- |
| index.html | icon | assets/img/favicon.png |
| index.html | apple-touch-icon | assets/img/apple-touch-icon.png |
| about.html | icon | assets/img/favicon.png |
| about.html | apple-touch-icon | assets/img/apple-touch-icon.png |
| resume.html | icon | assets/img/favicon.png |
| resume.html | apple-touch-icon | assets/img/apple-touch-icon.png |
| certifications.html | icon | assets/img/favicon.png |
| certifications.html | apple-touch-icon | assets/img/apple-touch-icon.png |
| services.html | icon | assets/img/favicon.png |
| services.html | apple-touch-icon | assets/img/apple-touch-icon.png |
| portfolio.html | icon | assets/img/favicon.png |
| portfolio.html | apple-touch-icon | assets/img/apple-touch-icon.png |
| portfolio-details.html | icon | assets/img/favicon.png |
| portfolio-details.html | apple-touch-icon | assets/img/apple-touch-icon.png |
| pulmotrack-details.html | icon | assets/img/favicon.png |
| pulmotrack-details.html | apple-touch-icon | assets/img/apple-touch-icon.png |
| testpilot-details.html | icon | assets/img/favicon.png |
| testpilot-details.html | apple-touch-icon | assets/img/apple-touch-icon.png |
| digital-gallery.html | icon | assets/img/favicon.png |
| digital-gallery.html | apple-touch-icon | assets/img/apple-touch-icon.png |
| contact.html | icon | assets/img/favicon.png |
| contact.html | apple-touch-icon | assets/img/apple-touch-icon.png |
| starter-page.html | icon | assets/img/favicon.png |
| starter-page.html | apple-touch-icon | assets/img/apple-touch-icon.png |

### Downloadable documents

| Local PDF file | Referenced by |
| --- | --- |
| assets/docs/Farah_Sayari_CV2026.pdf | resume.html |
| assets/docs/PulmoTrackPaper.pdf | pulmotrack-details.html |

Each original linked PDF is preserved in Content_Source_Snapshot.zip. Its unmodified pages are appended to the PDF version of this reference; the Word/HTML/Markdown versions identify the documents rather than rewriting them. View and download labels and requested filenames appear in the page-specific link tables.

### Source snapshot and verification

Content_Source_Snapshot.zip contains the captured HTML files, custom CSS and JavaScript, referenced local images and PDF documents, and the residual form/readme files. Source_Manifest.json records SHA-256 checksums. Content_Inventory.json contains the structured page inventory; Browser_Capture.json preserves the browser-parsed DOM and text. Vendor libraries are identified by reference rather than copied into the source archive.

The page transcripts are checked against every non-hidden text fragment inside each main element. Source hashes are checked before and after generation to confirm the website files remain unchanged. The generated PDF is checked for text coverage and readable page bounds.

## Owner notes and future updates

These notes are editable in documentation/notes.json. They are not current website copy and are kept separately from the exact page transcripts.

No owner notes have been added yet.
