---
permalink: /
title: "About Me"
author_profile: false
redirect_from: 
  - /about/
  - /about.html
---

<section class="profile-hero" aria-labelledby="home-title">
  <div class="profile-hero__content">
    <p class="profile-hero__eyebrow">Assistant Professor · ÉTS Montréal</p>
    <h1 id="home-title" class="profile-hero__title">Héber H. Arcolezi</h1>
    <p class="profile-hero__lead">Building Differential Privacy methods for Responsible and Trustworthy AI.</p>

    <div class="profile-hero__keywords" aria-label="Research keywords">
      <span>Differential Privacy</span>
      <span>Responsible AI</span>
      <span>Trustworthy AI</span>
    </div>

    <nav class="profile-hero__links" aria-label="Contact links">
      <a href="mailto:heber.hwang-arcolezi@etsmtl.ca" aria-label="Email">
        <i class="fas fa-envelope" aria-hidden="true"></i>
        <span>Email</span>
      </a>
      <a href="https://scholar.google.com/citations?user=lt28fGUAAAAJ&hl=en" target="_blank" rel="noopener noreferrer" aria-label="Google Scholar">
        <i class="ai ai-google-scholar" aria-hidden="true"></i>
        <span>Google Scholar</span>
      </a>
      <a href="https://x.com/hharcolezi" target="_blank" rel="noopener noreferrer" aria-label="X profile">
        <svg viewBox="0 0 24 24" role="img" aria-hidden="true" focusable="false">
          <path d="M18.901 1.153h3.68l-8.04 9.19L24 22.847h-7.406l-5.8-7.584-6.637 7.584H.478l8.6-9.83L0 1.153h7.594l5.243 6.932zM17.61 20.645h2.04L6.486 3.24H4.298z"/>
        </svg>
        <span>X</span>
      </a>
      <a href="/files/HHA_CV.pdf" aria-label="Curriculum Vitae">
        <i class="fas fa-file-pdf" aria-hidden="true"></i>
        <span>CV</span>
      </a>
    </nav>
  </div>

  <aside class="profile-hero__aside" aria-label="Portrait and affiliation">
    <img class="profile-hero__image" src="/images/HHA_profile.png" alt="Portrait of Héber H. Arcolezi" />
    <p class="profile-hero__location">Montréal, Canada</p>
  </aside>
</section>

<section class="profile-columns" aria-label="About and research overview">
  <article>
    <h2>About</h2>
    <p>
      I am an Assistant Professor in the Department of Software and Information Technology Engineering at
      <a href="https://www.etsmtl.ca/" target="_blank" rel="noopener noreferrer">ÉTS Montréal</a>, where I co-lead the
      Trustworthy Information Systems Lab
      <a href="https://tisl-lab.github.io/" target="_blank" rel="noopener noreferrer">(TISL)</a> research group.
      Previously, I was a Tenured Research Scientist at
      <a href="https://www.inria.fr/en/inria-centre-university-grenoble-alpes" target="_blank" rel="noopener noreferrer">Inria Grenoble</a>.
    </p>
  </article>

  <article>
    <h2>Research Interests</h2>
    <p>
      My research addresses the technical challenges of Responsible AI through the lenses of fairness,
      privacy-preserving techniques, and explainability. My goal is to design systems that are both
      mathematically private and socially equitable.
    </p>
  </article>

  <article>
    <h2>Background</h2>
    <p>
      I received my Ph.D. in Computer Science from the University of Bourgogne Franche-Comté (UBFC) and my
      M.Sc. in Electrical Engineering from the São Paulo State University (UNESP).
    </p>
  </article>
</section>

<style>
  :root {
    --profile-bg: #f7f8fb;
    --profile-text: #111318;
    --profile-muted: #50545f;
    --profile-line: #dfe4ee;
    --profile-accent: #1f4aa2;
  }

  body,
  .masthead {
    background: var(--profile-bg);
    color: var(--profile-text);
  }

  .masthead {
    border-bottom: 1px solid var(--profile-line);
  }

  .page {
    padding-inline: clamp(1.1rem, 3vw, 2.2rem);
  }

  .page__content {
    max-width: 1120px;
  }

  .profile-hero {
    margin: clamp(1.8rem, 4vw, 3rem) 0 clamp(2rem, 5vw, 3.4rem);
    display: grid;
    grid-template-columns: minmax(0, 1.5fr) minmax(240px, 0.8fr);
    gap: clamp(1.2rem, 3.4vw, 2.8rem);
    align-items: center;
    padding: clamp(1rem, 2vw, 1.5rem);
    border: 1px solid var(--profile-line);
    background: #ffffff;
    border-radius: 18px;
  }

  .profile-hero__eyebrow {
    margin: 0;
    text-transform: uppercase;
    letter-spacing: 0.11em;
    font-size: 0.76rem;
    color: var(--profile-muted);
    font-weight: 600;
  }

  .profile-hero__title {
    margin: 0.35rem 0 0;
    font-size: clamp(1.8rem, 4.2vw, 3rem);
    letter-spacing: -0.02em;
    line-height: 1.05;
  }

  .profile-hero__lead {
    margin: 0.95rem 0 0;
    max-width: 38ch;
    font-size: clamp(1rem, 1.8vw, 1.25rem);
    color: #1f2634;
  }

  .profile-hero__keywords {
    margin-top: 1rem;
    display: flex;
    gap: 0.6rem;
    flex-wrap: wrap;
  }

  .profile-hero__keywords span {
    font-size: 0.8rem;
    border: 1px solid #c9d3e6;
    border-radius: 999px;
    padding: 0.3rem 0.7rem;
    color: #23406f;
    background: #f5f8ff;
  }

  .profile-hero__links {
    margin-top: 1.2rem;
    display: flex;
    flex-wrap: wrap;
    gap: 0.65rem;
  }

  .profile-hero__links a {
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    padding: 0.42rem 0.7rem;
    border: 1px solid var(--profile-line);
    border-radius: 999px;
    color: #1a2233;
    text-decoration: none;
    font-size: 0.77rem;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    transition: border-color 0.2s ease, background-color 0.2s ease;
  }

  .profile-hero__links a:hover {
    border-color: var(--profile-accent);
    background: #f2f6ff;
  }

  .profile-hero__links i,
  .profile-hero__links svg {
    width: 1rem;
    height: 1rem;
    font-size: 1rem;
    flex-shrink: 0;
  }

  .profile-hero__links svg {
    fill: currentColor;
  }

  .profile-hero__aside {
    text-align: center;
  }

  .profile-hero__image {
    width: min(100%, 320px);
    aspect-ratio: 1 / 1;
    object-fit: cover;
    border-radius: 14px;
    border: 1px solid var(--profile-line);
  }

  .profile-hero__location {
    margin: 0.65rem 0 0;
    font-size: 0.88rem;
    color: var(--profile-muted);
  }

  .profile-columns {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: clamp(1rem, 2.5vw, 2rem);
    margin-bottom: 2rem;
  }

  .profile-columns article {
    background: #ffffff;
    border: 1px solid var(--profile-line);
    border-radius: 14px;
    padding: 1rem 1rem 1.1rem;
  }

  .profile-columns h2 {
    margin: 0;
    font-size: 0.92rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
  }

  .profile-columns p {
    margin: 0.7rem 0 0;
    color: #1d2130;
    line-height: 1.64;
    font-size: 0.97rem;
  }

  .profile-columns a {
    color: inherit;
    text-underline-offset: 0.2em;
  }

  @media (max-width: 980px) {
    .profile-hero {
      grid-template-columns: 1fr;
    }

    .profile-hero__aside {
      text-align: left;
    }

    .profile-columns {
      grid-template-columns: 1fr;
    }
  }
</style>
