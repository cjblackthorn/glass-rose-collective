---
layout: page
title: Projects
permalink: /projects/
---

<div class="grc-page-hero grc-dark-section">
  <h1>Projects, releases, showcases, and collaborative work in development.</h1>

  <p>
    Glass Rose Collective is being built as a living creative ecosystem. This page holds publications, music projects, creator showcases, multimedia releases, and collaborative initiatives.
  </p>
</div>

<div class="grc-editorial-section">
  <div class="grc-editorial-statement">
    <h2>Creative ecosystems need visible roots.</h2>

    <p>
      Projects give the collective shape. They show what is being built, what is emerging, and where creators may connect.
    </p>
  </div>

  <div class="grc-editorial-panel">
    <p>
      Some projects may be published directly through Glass Rose Collective. Others may be supported through guidance, collaboration, distribution planning, or trusted referrals.
    </p>

    <p>
      The goal is not volume. The goal is meaningful work handled with care.
    </p>
  </div>
</div>

<div class="grc-manifesto-divider"></div>

<h2>Featured Projects</h2>

<div class="grc-showcase-grid">
  {% for project in site.projects %}
    <section class="grc-showcase-card">
      {% if project.status %}
        <span class="grc-showcase-label">{{ project.status }}</span>
      {% endif %}

      <h3>
        <a href="{{ project.url | relative_url }}">{{ project.title }}</a>
      </h3>

      {% if project.category %}
        <p><strong>{{ project.category }}</strong></p>
      {% endif %}

      <p>{{ project.content | strip_html | truncatewords: 28 }}</p>
    </section>
  {% endfor %}
</div>

<div class="grc-dark-section">
  <h2>Project Philosophy</h2>

  <p>
    We are not trying to mass-produce releases for the sake of appearing busy.
  </p>

  <p>
    Glass Rose projects should feel intentional, human, creator-aware, and aligned with the emotional identity of the work itself.
  </p>
</div>

<h2>Future Project Types</h2>

<div class="grc-tag-grid">
  <span>Artist Showcases</span>
  <span>Collaborative Releases</span>
  <span>Poetry Collections</span>
  <span>Music Releases</span>
  <span>Visual Essays</span>
  <span>Creator Interviews</span>
  <span>Multimedia Projects</span>
  <span>Community Features</span>
</div>

<div class="grc-cta-panel">
  <h2>Have a project that may fit Glass Rose?</h2>

  <p>
    We are selective and capacity-aware, but we are interested in meaningful work, creator-first collaboration, and projects with emotional honesty.
  </p>

  <a class="grc-button" href="{{ '/contact/' | relative_url }}">Start a Conversation</a>
</div>