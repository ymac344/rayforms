# rayforms

Redesigned static website for ר.א.י (תעשיה לתבניות מתקדמות) בע"מ, based on the content of https://rayforms.co.il/.

**View the site:** [Hebrew](https://ymac344.github.io/rayforms/) · [English](https://ymac344.github.io/rayforms/en/)

The original WordPress/Elementor snapshot is preserved in git history (first commit).

## Structure

- `build.py` – all page content in Hebrew and English, and the shared layout (header, navigation, footer). Generates every `index.html`: Hebrew pages at the root, English pages under `en/`.
- `assets/css/style.css` – the design (colors, typography, layout).
- `assets/js/main.js` – mobile menu, image lightbox, hero video, contact form.
- `assets/img`, `assets/video`, `assets/fonts` – media and the Heebo font.

## Editing

Change text or pages in `build.py`, then rebuild:

    python3 build.py

Preview locally with `python3 -m http.server` and open http://localhost:8000/.

## Notes

- The contact form has no server behind it: submitting opens the visitor's email app with the message addressed to the company.
- Hebrew page addresses are the same as on the original site. Every page links to its counterpart in the other language from the header.
