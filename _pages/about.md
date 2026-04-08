---
permalink: /
title: "About Me"
author_profile: false
redirect_from: 
  - /about/
  - /about.html
---

<section class="editorial-hero" aria-labelledby="home-title">
  <div class="editorial-hero__left">
    <p class="editorial-hero__watermark" aria-hidden="true">Heber Hwang Arcolezi</p>
    <p class="editorial-hero__eyebrow">Assistant Professor · ÉTS Montréal</p>
    <h1 id="home-title" class="editorial-hero__title">Heber Hwang Arcolezi</h1>
    <p class="editorial-hero__lead">Designing trustworthy information systems for Responsible AI.</p>

    <div class="editorial-hero__tags" aria-label="Research topics">
      <span>Fairness</span>
      <span>Privacy-Preserving Techniques</span>
      <span>Explainability</span>
      <span>Responsible AI</span>
    </div>

    <nav class="editorial-hero__links" aria-label="Contact links">
      <a href="mailto:heber.hwang-arcolezi@etsmtl.ca">Email</a>
      <a href="https://scholar.google.com/citations?user=lt28fGUAAAAJ&hl=en" target="_blank" rel="noopener noreferrer">Scholar</a>
      <a href="https://github.com/hharcolezi" target="_blank" rel="noopener noreferrer">GitHub</a>
      <a href="https://x.com/hharcolezi" target="_blank" rel="noopener noreferrer">Twitter</a>
      <a href="/files/HHA_CV.pdf">CV</a>
    </nav>
  </div>

  <aside class="editorial-hero__right" aria-label="Portrait and affiliation">
    <img class="editorial-hero__image" src="/images/HHA_profile.png" alt="Portrait of Heber Hwang Arcolezi" />
    <div class="editorial-hero__institution">
      <p class="role">Assistant Professor</p>
      <p class="dept">Department of Software and Information Technology Engineering · ÉTS Montréal</p>
      <p class="location">Montréal, Canada</p>
    </div>
  </aside>
</section>

<section class="editorial-columns" aria-label="About and research overview">
  <article>
    <h2>About</h2>
    <p>
      I am an Assistant Professor at
      <a href="https://www.etsmtl.ca/" target="_blank" rel="noopener noreferrer">ÉTS Montréal</a>, where I co-lead the
      <a href="https://tisl-lab.github.io/" target="_blank" rel="noopener noreferrer">Trustworthy Information Systems Lab (TISL)</a>.
      Previously, I was a Tenured Research Scientist at
      <a href="https://www.inria.fr/en/inria-centre-university-grenoble-alpes" target="_blank" rel="noopener noreferrer">Inria Grenoble</a>.
    </p>
  </article>

  <article>
    <h2>Research Interests</h2>
    <p>
      My research addresses responsible AI through privacy-preserving learning, fairness-aware methods,
      and explainability. I build systems that are mathematically private while remaining practically useful.
    </p>
  </article>

  <article>
    <h2>Background</h2>
    <p>
      I received my Ph.D. in Computer Science from the University of Bourgogne Franche-Comté (UBFC) and my
      M.Sc. in Electrical Engineering from São Paulo State University (UNESP). I focus on connecting theory,
      systems, and real-world deployments.
    </p>
  </article>
</section>

<style>
  :root {
    --editorial-bg: #f9f9f9;
    --editorial-text: #101010;
    --editorial-muted: #9d9d9d;
    --editorial-accent: #8c4f2e;
    --editorial-rule: #e8e4df;
  }

  body {
    background: var(--editorial-bg);
    color: var(--editorial-text);
  }

  .page {
    padding-inline: clamp(1.2rem, 3.5vw, 2.4rem);
  }

  .page__content {
    max-width: 1240px;
  }

  .masthead {
    border-bottom: 1px solid var(--editorial-rule);
    background: var(--editorial-bg);
  }

  .greedy-nav .visible-links a {
    text-transform: uppercase;
    letter-spacing: 0.13em;
    font-size: 0.68rem;
    color: #2a2a2a;
  }

  .greedy-nav .visible-links a:hover {
    color: var(--editorial-accent);
  }

  .editorial-hero {
    margin: clamp(1.5rem, 5vw, 3.4rem) 0 clamp(2.3rem, 6vw, 4.2rem);
    display: grid;
    grid-template-columns: minmax(0, 1.45fr) minmax(280px, 0.85fr);
    gap: clamp(1.6rem, 4vw, 3.2rem);
    align-items: end;
    padding-bottom: clamp(1.6rem, 4vw, 2.4rem);
    border-bottom: 1px solid var(--editorial-rule);
  }

  .editorial-hero__left {
    position: relative;
  }

  .editorial-hero__watermark {
    position: absolute;
    top: clamp(-0.7rem, -1.5vw, -1.3rem);
    left: 0;
    width: min(980px, 100%);
    margin: 0;
    z-index: 0;
    font-weight: 800;
    letter-spacing: -0.04em;
    line-height: 0.82;
    font-size: clamp(3.2rem, 12vw, 8.8rem);
    color: #e8e8e8;
    pointer-events: none;
    user-select: none;
  }

  .editorial-hero__eyebrow,
  .editorial-hero__title,
  .editorial-hero__lead,
  .editorial-hero__tags,
  .editorial-hero__links {
    position: relative;
    z-index: 1;
  }

  .editorial-hero__eyebrow {
    margin: 0;
    font-size: 0.82rem;
    letter-spacing: 0.11em;
    text-transform: uppercase;
    font-weight: 600;
  }

  .editorial-hero__title {
    margin: 0.25rem 0 0;
    font-size: clamp(2.8rem, 8.1vw, 6.6rem);
    line-height: 0.9;
    letter-spacing: -0.045em;
    font-weight: 800;
    max-width: 8.7ch;
  }

  .editorial-hero__lead {
    margin: 1.2rem 0 0;
    max-width: 35ch;
    font-size: clamp(1rem, 2.3vw, 1.95rem);
    line-height: 1.35;
  }

  .editorial-hero__tags {
    margin-top: 1.3rem;
    display: flex;
    flex-wrap: wrap;
    gap: 0.9rem;
  }

  .editorial-hero__tags span {
    text-decoration: underline;
    text-decoration-thickness: 1px;
    text-underline-offset: 0.21em;
    font-size: 0.92rem;
    letter-spacing: 0.02em;
  }

  .editorial-hero__links {
    margin-top: 1.35rem;
    display: flex;
    flex-wrap: wrap;
    gap: 1.25rem;
  }

  .editorial-hero__links a {
    text-transform: uppercase;
    letter-spacing: 0.12em;
    font-size: 0.74rem;
    color: var(--editorial-accent);
    text-decoration: none;
    border-bottom: 1px solid color-mix(in srgb, var(--editorial-accent) 48%, transparent);
    padding-bottom: 0.18rem;
  }

  .editorial-hero__links a:hover {
    border-bottom-color: var(--editorial-accent);
  }

  .editorial-hero__right {
    display: grid;
    gap: 1.15rem;
  }

  .editorial-hero__image {
    width: 100%;
    max-width: 390px;
    aspect-ratio: 1 / 1;
    object-fit: cover;
    display: block;
    justify-self: start;
  }

  .editorial-hero__institution .role {
    margin: 0;
    font-size: 1.95rem;
    line-height: 1.08;
  }

  .editorial-hero__institution .dept,
  .editorial-hero__institution .location {
    margin: 0.65rem 0 0;
    font-size: 1.02rem;
    color: #333;
    line-height: 1.45;
    max-width: 28ch;
  }

  .editorial-columns {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: clamp(1.1rem, 2.8vw, 2.4rem);
    margin-bottom: 1.8rem;
  }

  .editorial-columns article {
    border-top: 1px solid var(--editorial-rule);
    padding-top: 1.1rem;
  }

  .editorial-columns h2 {
    margin: 0;
    font-size: 1.05rem;
    letter-spacing: 0.04em;
    text-transform: uppercase;
  }

  .editorial-columns p {
    margin: 0.75rem 0 0;
    color: #222;
    line-height: 1.72;
    font-size: 1.01rem;
  }

  .editorial-columns a {
    color: inherit;
    text-underline-offset: 0.17em;
  }

  @media (max-width: 980px) {
    .editorial-hero {
      grid-template-columns: 1fr;
      align-items: start;
    }

    .editorial-hero__watermark {
      font-size: clamp(2.8rem, 20vw, 7rem);
      line-height: 0.9;
      opacity: 0.82;
    }

    .editorial-hero__right {
      margin-top: 0.7rem;
      max-width: 460px;
    }

    .editorial-columns {
      grid-template-columns: 1fr;
      gap: 1.3rem;
    }
  }

  @media (max-width: 640px) {
    .editorial-hero__links {
      gap: 0.95rem;
      row-gap: 0.5rem;
    }

    .editorial-hero__links a,
    .greedy-nav .visible-links a {
      letter-spacing: 0.09em;
    }
  }
</style>
