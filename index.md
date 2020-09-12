---
layout: default
title: butiran
---

# butiran -- physics in plain text

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
  searchResultTemplate: '<tt><a href="{url}" tabindex="1">{title}</a></tt>',
  noResultsText: 'No results found!',
  json: '/search.json',
})
</script>
