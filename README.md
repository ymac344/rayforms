# rayforms

Redesigned static website for ר.א.י (תעשיה לתבניות מתקדמות) בע"מ, based on the content of https://rayforms.co.il/.

**View the site:** [Hebrew](https://ymac344.github.io/rayforms/) · [English](https://ymac344.github.io/rayforms/en/)

The original WordPress/Elementor snapshot is preserved in git history (first commit).

## Design alternatives

The "Designs" menu in the site header previews two independent choices, which can be combined freely (the choice is remembered while browsing):

**Layout**

- [Standard (current)](https://ymac344.github.io/rayforms/?layout=standard)
- [Centered](https://ymac344.github.io/rayforms/?layout=centered)
- [Split – text beside video](https://ymac344.github.io/rayforms/?layout=split)
- [Side menu](https://ymac344.github.io/rayforms/?layout=sidebar)
- [Showcase – large photos](https://ymac344.github.io/rayforms/?layout=showcase)
- [Compact – list](https://ymac344.github.io/rayforms/?layout=compact)

**Colour scheme**

- [Classic (current)](https://ymac344.github.io/rayforms/?design=classic)
- [Graphite – dark](https://ymac344.github.io/rayforms/?design=graphite)
- [Concrete – industrial](https://ymac344.github.io/rayforms/?design=concrete)
- [Blueprint – blue](https://ymac344.github.io/rayforms/?design=blueprint)
- [Safety yellow](https://ymac344.github.io/rayforms/?design=safety)
- [Editorial – serif](https://ymac344.github.io/rayforms/?design=editorial)
- [Galilee – green](https://ymac344.github.io/rayforms/?design=galilee)
- [Steel – teal](https://ymac344.github.io/rayforms/?design=steel)
- [Soft – rounded](https://ymac344.github.io/rayforms/?design=soft)

A link can set both, for example [https://ymac344.github.io/rayforms/?layout=split&design=galilee](https://ymac344.github.io/rayforms/?layout=split&design=galilee).

Layouts are defined in `assets/css/layouts.css` and colour schemes in `assets/css/themes.css`. Once a combination is chosen, the menu and the unused options can be removed.

## Structure

- `build.py` – all page content in Hebrew and English, and the shared layout (header, navigation, footer). Generates every `index.html`: Hebrew pages at the root, English pages under `en/`.
- `assets/css/style.css` – the design (colors, typography, layout).
- `assets/js/main.js` – mobile menu, image lightbox, hero video, contact form.
- `assets/img`, `assets/video`, `assets/fonts` – media and fonts. `logo.svg` is the Hebrew logo, `logo-en.svg` the English one.

## Editing

Change text or pages in `build.py`, then rebuild:

    python3 build.py

Preview locally with `python3 -m http.server` and open http://localhost:8000/.

## Notes

- The contact form has no server behind it: submitting opens the visitor's email app with the message addressed to the company.
- Hebrew page addresses are the same as on the original site. Every page links to its counterpart in the other language from the header.
