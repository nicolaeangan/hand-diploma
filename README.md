# Upper Limb Atlas — template
Open `index.html` in a browser (no server needed).
- Edit `articles_data.py` (articles, cards/tags, categories) then run `python3 build.py` to regenerate all pages.
- Two articles are linked when they share a card (tag); edge weight = shared cards.
- `assets/style.css` holds the colour tokens (dark/light); `assets/graph.js` is a dependency-free SVG force graph.
Sample content only, not clinical advice.
