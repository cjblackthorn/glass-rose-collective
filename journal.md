---
layout: page
title: Journal
permalink: /journal/
---

<div class="grc-page-hero grc-dark-section">
  <h1>Editorial reflections, creator spotlights, project updates, and collective voices.</h1>

  <p>
    The Glass Rose Journal exists as an evolving editorial space for artists, creators, collaborators, and emotionally honest creative work.
  </p>
</div>

<div class="grc-editorial-section">
  <div class="grc-editorial-statement">
    <h2>Creative ecosystems need conversation, not just content.</h2>

    <p>
      The Journal is where the collective speaks, reflects, experiments, documents growth, and highlights meaningful work.
    </p>
  </div>

  <div class="grc-editorial-panel">
    <p>
      Future entries may include creator spotlights, collaborative projects, release notes, indie culture commentary, artistic reflections, interviews, and multimedia storytelling.
    </p>
  </div>
</div>

<div class="grc-manifesto-divider"></div>

<h2>Latest Journal Entries</h2>

<div class="grc-showcase-grid">
  {% assign sorted_journal = site.journal | sort: 'date' | reverse %}

  {% for entry in sorted_journal %}
    <section class="grc-showcase-card">
      {% if entry.category %}
        <span class="grc-showcase-label">{{ entry.category }}</span>
      {% endif %}

      <h3>
        <a href="{{ entry.url | relative_url }}">{{ entry.title }}</a>
      </h3>

      {% if entry.date %}
        <p><strong>{{ entry.date | date: "%B %d, %Y" }}</strong></p>
      {% endif %}

      <p>{{ entry.content | strip_html | truncatewords: 30 }}</p>
    </section>
  {% endfor %}
</div>

<div class="grc-dark-section">
  <h2>Built for creators who still want to make something real.</h2>

  <p>
    Not everything meaningful can be compressed into algorithms, metrics, and engagement cycles.
  </p>

  <p>
    The Journal exists to preserve space for slower, more human creative expression.
  </p>
</div>

<div class="grc-cta-panel">
  <h2>The Journal is just beginning.</h2>

  <p>
    Creator spotlights, editorials, collaborative reflections, and future releases will continue expanding over time.
  </p>

  <a class="grc-button" href="{{ '/projects/' | relative_url }}">Explore Projects</a>
</div>