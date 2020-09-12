---
layout: default
title: butiran
---

# butiran

<!-- Html Elements for Search -->
<div id="search-container">
<input type="text" id="search-input" placeholder="search...">
<ul id="results-container"></ul>
</div>

<!-- Script pointing to search-script.js -->
<script src="/assets/js/simple-jekyll-search.min.js" type="text/javascript"></script>

<!-- Configuration -->
<script>
SimpleJekyllSearch({
  searchInput: document.getElementById('search-input'),
  resultsContainer: document.getElementById('results-container'),
  searchResultTemplate: '<li><a href="{url}" tabindex="1"><p>{title}</p><span>{url}</span></a></li>',
  noResultsText: '<li><p>No results found!</p></li>',
  json: '/search.json',
})
</script>
