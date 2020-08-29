---
layout: default
title: butiran
---

# butiran

[physics](physics) `|` [abm-pbsp](abm-pbsp) `|`
[abm-traffic-log](abm-traffic-log) `|` [abm-com-seir](abm-com-seir)

<!--p style="font-family: monospace">
{% comment %}
{% assign pad0 = '00' %}
{% assign n = pad0 | size %}
{% assign m = 0 | minus: n %}
{% assign i = site.posts.size %}
{% for post in site.posts %}
	{% assign d = post.date | split: ' ' %}
	{% assign i = i | minus: 1 | prepend: pad0 %}
	{% assign j = i | slice: m, n %}
	{% assign k = d.first | replace: "-", "" %}
	[{{ j }}]
	<a href="{{ site.baseurl }}{{ post.url }}">
		{{ post.date | date: "%d-%b" }} {{ post.title }}</a>,
{% endfor %}
{% endcomment %}
</p-->