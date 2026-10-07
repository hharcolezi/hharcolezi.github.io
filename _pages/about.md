---
permalink: /
author_profile: false
---

<link rel="stylesheet" href="/assets/css/homepage-refresh.css">

<section class="profile-hero" aria-labelledby="home-title">
  <div class="profile-hero__content">
    <p class="profile-hero__eyebrow" id="profile-position">Assistant Professor · ÉTS Montréal</p>
    <h1 id="home-title" class="profile-hero__title">Héber H. Arcolezi</h1>
    <p class="profile-hero__lead" id="profile-hero-lead">Privacy, auditing, and fairness for responsible AI.</p>
    <p class="profile-hero__summary" id="profile-hero-summary">I design, analyze, and audit privacy-preserving machine learning systems, with a focus on differential privacy, inference risks, and fairness.</p>

    <div class="profile-hero__keywords" id="profile-keywords" aria-label="Research keywords">
      <span>Differential Privacy</span><span>Privacy Auditing</span><span>Fairness in ML</span><span>Privacy–Utility Trade-offs</span><span>Local Differential Privacy</span>
    </div>

    <nav class="profile-hero__links" aria-label="Contact links">
      <a href="mailto:heber.hwang-arcolezi@etsmtl.ca"><i class="fas fa-envelope" aria-hidden="true"></i><span>Email</span></a>
      <a href="https://scholar.google.com/citations?hl=en&user=VJgSocwAAAAJ&view_op=list_works&sortby=pubdate" target="_blank" rel="noopener noreferrer"><i class="ai ai-google-scholar" aria-hidden="true"></i><span>Google Scholar</span></a>
      <a href="https://github.com/hharcolezi" target="_blank" rel="noopener noreferrer"><i class="fab fa-github" aria-hidden="true"></i><span>GitHub</span></a>
      <a href="https://x.com/hharcolezi" target="_blank" rel="noopener noreferrer"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M18.901 1.153h3.68l-8.04 9.19L24 22.847h-7.406l-5.8-7.584-6.637 7.584H.478l8.6-9.83L0 1.153h7.594l5.243 6.932zM17.61 20.645h2.04L6.486 3.24H4.298z"/></svg><span>X</span></a>
      <a href="https://hharcolezi.github.io/files/HHA_CV.pdf" target="_blank" rel="noopener noreferrer"><i class="fas fa-file-pdf" aria-hidden="true"></i><span>CV</span></a>
    </nav>
  </div>

  <aside class="profile-hero__aside">
    <div class="profile-hero__portrait-frame"><img class="profile-hero__image" src="/images/HHA_profile.png" alt="Portrait of Héber H. Arcolezi"></div>
    <p class="profile-hero__location"><i class="fas fa-map-marker-alt" aria-hidden="true"></i> Montréal, Canada</p>
  </aside>
</section>

<section class="home-overview">
  <article class="home-panel">
    <header class="home-panel__header"><span class="home-panel__icon home-panel__icon--blue"><i class="far fa-user"></i></span><h2>About</h2></header>
    <p id="profile-about">I am an Assistant Professor in the Department of Software and Information Technology Engineering at <a href="https://www.etsmtl.ca/" target="_blank" rel="noopener noreferrer">ÉTS Montréal</a>, where I co-lead the Trustworthy Information Systems Lab <a href="https://tisl-lab.github.io/" target="_blank" rel="noopener noreferrer">(TISL)</a> research group. Previously, I was a Tenured Research Scientist at <a href="https://www.inria.fr/en/inria-centre-university-grenoble-alpes" target="_blank" rel="noopener noreferrer">Inria Grenoble</a>.</p>
    <div class="home-background"><span class="home-background__label">Background</span><p id="profile-background">I received my Ph.D. in Computer Science from the <a href="https://www.ubfc.fr/" target="_blank" rel="noopener noreferrer">University of Bourgogne Franche-Comté (UBFC)</a>, my M.Sc. in Electrical Engineering from the <a href="https://www2.unesp.br/" target="_blank" rel="noopener noreferrer">São Paulo State University (UNESP)</a>, and my B.Eng. in Electrical Engineering from the <a href="https://www.unemat.br/" target="_blank" rel="noopener noreferrer">Mato Grosso State University (UNEMAT)</a>.</p></div>
  </article>

  <article class="home-panel">
    <header class="home-panel__header"><span class="home-panel__icon home-panel__icon--violet"><i class="fas fa-crosshairs"></i></span><h2>Research Focus</h2></header>
    <p id="profile-research" class="home-panel__intro">My research addresses the technical challenges of Responsible AI through the lenses of fairness, privacy-preserving techniques, and explainability. My goal is to design systems that are both mathematically private and socially equitable.</p>
    <div id="research-focus-list" class="research-focus-list"></div>
    <a class="home-panel__more" href="/projects/">Explore research projects →</a>
  </article>

  <article class="home-panel">
    <header class="home-panel__header"><span class="home-panel__icon home-panel__icon--green"><i class="fas fa-bullhorn"></i></span><h2>Recent News</h2></header>
    <div class="news-app" id="news-app"><div id="news-state" class="news-state">News is generated during the website build.</div><div id="news-list" class="news-list"></div></div>
  </article>
</section>

<section class="featured-publications" aria-labelledby="featured-publications-title">
  <div class="home-section-heading"><div><span class="home-section-heading__icon"><i class="far fa-file-alt"></i></span><h2 id="featured-publications-title">Selected Publications</h2></div><a href="/publications/">View all publications →</a></div>
  <div id="featured-publications-list" class="featured-publications-grid"></div>
</section>

<section class="home-contact-card" aria-labelledby="contact-title">
  <div class="home-contact-card__header">
    <span class="home-contact-card__icon"><i class="fas fa-envelope" aria-hidden="true"></i></span>
    <h2 id="contact-title">Contact</h2>
  </div>
  <p>I am always happy to discuss the possibility of new collaborations.</p>
  <dl class="home-contact-card__details">
    <div>
      <dt>Email</dt>
      <dd><a href="mailto:heber.hwang-arcolezi@etsmtl.ca">heber.hwang-arcolezi@etsmtl.ca</a></dd>
    </div>
    <div>
      <dt>Postal Address</dt>
      <dd>1100, rue Notre-Dame Ouest, Montréal (Qc) H3C 1K3, Canada.</dd>
    </div>
  </dl>
</section>
<p class="home-updated">Last update: {{ site.time | date: "%b %-d, %Y" }}.</p>
