---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

## Technical reports

My bachelor final report can be downloaded [here](http://hharcolezi.github.io/files/2017_UNEMAT_Final_Work.pdf)

My master thesis dissertation can be downloaded [here](http://hharcolezi.github.io/files/2019_UNESP_Master_thesis_compressed.pdf)

## Articles

You can also find a complete list of my articles on my [Google Scholar profile](https://scholar.google.com/citations?hl=en&user=VJgSocwAAAAJ).

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
