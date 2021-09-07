---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---


You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>

My master thesis dissertation can be downloaded [here](http://hharcolezi.github.io/files/2019_UNESP_Master_thesis_compressed.pdf)

My bachelor final report can be downloaded [here](http://hharcolezi.github.io/files/2017_UNEMAT_Final_Work.pdf)

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
