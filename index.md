---
layout: default
title: Spotkania
permalink: /spotkania/
permalink: index.html
---

<div class="home">
  <ul class="posts">
    {% for post in site.posts %}
    <li>
      <span class="post-date">
        <i class="fa fa-calendar lgray" ></i> {{ post.date | date: "%b %-d, %Y" }}
      </span>
      <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">
        {% if post.speaker %}{{ post.speaker | join: ', ' }} - {% endif %}{{ post.title }}
      </a>
    </li>
    {% endfor %}
  </ul>
  <p class="rss-subscribe">
    subscribe <a href="{{ "/feed.xml" | prepend: site.baseurl }}">via RSS</a>
  </p>
</div>