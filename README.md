# rayforms

Static snapshot of https://rayforms.co.il/ (WordPress + Elementor), captured 2026-11-22 as the baseline for a site revamp.

- 18 pages, with links rewritten to relative paths so the site can be browsed locally:
  `python3 -m http.server` then open http://localhost:8000/
- `wp-content/` and `wp-includes/` hold the downloaded CSS, JS, fonts, images and the hero video.
- Dynamic features (contact form submission, reCAPTCHA, Google Maps embed) still point at the live site / third parties.
