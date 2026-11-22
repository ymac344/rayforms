#!/usr/bin/env python3
"""Builds the static site. Run `python3 build.py` from the repository root.

All page content lives in this file; shared layout (header, footer) is defined
once here and written into every page. Output is plain HTML at the repo root.
"""
import os
from html import escape

ROOT = os.path.dirname(os.path.abspath(__file__))

COMPANY = 'ר.א.י (תעשיה לתבניות מתקדמות) בע"מ'
PHONE_OFFICE = '04-6020505'
PHONE_SALES = '050-4728956'
EMAIL = 'ariel@rayforms.co.il'
ADDRESS = 'הצורף 1, נוף-הגליל'
MAP_SRC = ('https://maps.google.com/maps?q=%D7%94%D7%A6%D7%95%D7%A8%D7%A3%201%20'
           '%D7%A0%D7%95%D7%A3%20%D7%94%D7%92%D7%9C%D7%99%D7%9C&t=m&z=10&output=embed&iwloc=near')

# ---------------------------------------------------------------- paths
P_PROJECTS = 'פרויקטים'
P_PROTECTED = 'מבנים-טרומיים/מרחבים-מוגנים'
P_TRANSFORMER = 'מבנים-טרומיים/חדרי-טרנספורמציה'
P_PORTABLE = 'מבנים-טרומיים/מבנים-מרחביים-יבילים'
P_PORTS = P_PORTABLE + '/רשות-הנמלים'
P_POSTAL = P_PORTABLE + '/מבני-חלוקת-דואר'
P_MEKOROT = P_PORTABLE + '/מבנים-לחברת-מקורות'
P_POLICE = P_PORTABLE + '/מבנה-מעבר-משטרת-ישראל'
P_ARMORY = 'מבנים-טרומיים/חדרי-נשק'
P_GUARD = 'מבנים-טרומיים/חדרי-שומר'
P_LIGHT = 'בניה-קלה'
P_CERTS = 'אישורים-והסמכות'
P_QUALITY = 'הצהרת-מדיניות-האיכות'
P_ABOUT = 'אודות'
P_CONTACT = 'צור-קשר'
P_PRJ_TZUR = 'projects/הקמת-משטרת-צור-באהר'
P_PRJ_TAIBE = 'projects/משטרת-טייבה'
P_PRJ_CAMP = 'projects/מחנה-בשטח-של-כ-5000-מר'

TITLES = {
    P_PROJECTS: 'פרויקטים',
    P_PROTECTED: 'מרחבים מוגנים',
    P_TRANSFORMER: 'ייצור חדרי שנאים (חדרי טרפו)',
    P_PORTABLE: 'מבנים מרחביים יבילים',
    P_PORTS: 'רשות הנמלים',
    P_POSTAL: 'מבני חלוקת דואר',
    P_MEKOROT: 'מבנים לחברת מקורות',
    P_POLICE: 'מבנה מעבר משטרת ישראל',
    P_ARMORY: 'חדרי נשק',
    P_GUARD: 'חדרי שומר',
    P_LIGHT: 'בניה קלה',
    P_CERTS: 'אישורים והסמכות',
    P_QUALITY: 'הצהרת מדיניות האיכות',
    P_ABOUT: 'אודות ר.א.י (תעשיה לתבניות מתקדמות) בע"מ',
    P_CONTACT: 'צור קשר',
    P_PRJ_TZUR: 'הקמת משטרת צור באהר',
    P_PRJ_TAIBE: 'משטרת טייבה',
    P_PRJ_CAMP: 'מחנה בשטח של כ-5000 מ״ר',
}

PRECAST = [P_PROTECTED, P_TRANSFORMER, P_PORTABLE, P_ARMORY, P_GUARD]
PORTABLE_CHILDREN = [P_PORTS, P_POSTAL, P_MEKOROT, P_POLICE]
PROJECTS = [
    (P_PRJ_TZUR, 'project-tzur-baher.webp'),
    (P_PRJ_TAIBE, 'project-taibe.webp'),
    (P_PRJ_CAMP, 'project-camp.webp'),
]
CLIENTS = [
    ('bezek', 'בזק'), ('cellcom', 'סלקום'), ('doar', 'דואר ישראל'), ('hashmal', 'חברת החשמל'),
    ('amidar', 'עמידר'), ('keisaria', 'החברה לפיתוח קיסריה'), ('police', 'משטרת ישראל'),
    ('shikun', 'שיכון ובינוי סולל בונה'), ('amigur', 'עמיגור'),
    ('haklaut', 'משרד החקלאות ופיתוח הכפר'), ('mekorot', 'מקורות'),
]

# ---------------------------------------------------------------- icons
ICONS = {
    'phone': '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/>',
    'mail': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
    'pin': '<path d="M12 21s7-6.2 7-11.5a7 7 0 0 0-14 0C5 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
    'menu': '<path d="M4 7h16M4 12h16M4 17h16"/>',
    'arrow': '<path d="M19 12H5m6-6-6 6 6 6"/>',
    'chevron': '<path d="m6 9 6 6 6-6"/>',
}


def icon(name):
    return f'<svg class="icon" viewBox="0 0 24 24" aria-hidden="true">{ICONS[name]}</svg>'


# ---------------------------------------------------------------- helpers
class Ctx:
    """Per-page context: resolves links relative to the page being written."""

    def __init__(self, path):
        self.path = path
        self.root = '../' * len(path.split('/')) if path else ''

    def url(self, path):
        return (self.root + path + '/') if path else (self.root or './')

    def asset(self, path):
        return self.root + 'assets/' + path


def tel(number):
    return 'tel:' + number.replace('-', '')


def card(c, path, image=None, title=None):
    title = escape(title or TITLES[path])
    media = ''
    cls = 'card card-plain'
    if image:
        cls = 'card'
        media = (f'<div class="card-media"><img src="{c.asset("img/" + image)}" alt="" '
                 f'width="1140" height="700" loading="lazy" decoding="async"></div>')
    return (f'<article class="{cls}">{media}<div class="card-body">'
            f'<h3><a href="{c.url(path)}">{title}</a></h3>{icon("arrow")}</div></article>')


def gallery(c, images, extra=''):
    cls = 'gallery' + (' single' if len(images) == 1 else '') + extra
    items = ''.join(
        f'<a href="{c.asset("img/" + src)}" data-lightbox><img src="{c.asset("img/" + src)}" '
        f'alt="{escape(alt)}" width="1140" height="700" loading="lazy" decoding="async"></a>'
        for src, alt in images)
    return f'<div class="{cls}">{items}</div>'


def pills(c, paths, heading):
    items = ''.join(f'<li><a href="{c.url(p)}">{escape(TITLES[p])}</a></li>' for p in paths)
    return f'<div class="related"><h2>{heading}</h2><ul class="pills">{items}</ul></div>'


def aside(c):
    return f'''<aside class="aside">
<h2>מעוניינים בפרטים נוספים?</h2>
<p>השאירו פרטים ונחזור אליכם בהקדם.</p>
<a class="btn btn-primary" href="{c.url(P_CONTACT)}">צור קשר</a>
<a class="btn btn-outline" href="{tel(PHONE_OFFICE)}">{icon('phone')}<span class="ltr">{PHONE_OFFICE}</span></a>
</aside>'''


def contact_list():
    return f'''<ul class="contact-list">
<li>{icon('phone')}<div><small>משרד</small><a class="ltr" href="{tel(PHONE_OFFICE)}">{PHONE_OFFICE}</a></div></li>
<li>{icon('phone')}<div><small>מכירות</small><a class="ltr" href="{tel(PHONE_SALES)}">{PHONE_SALES}</a></div></li>
<li>{icon('mail')}<div><small>אימייל</small><a class="ltr" href="mailto:{EMAIL}">{EMAIL}</a></div></li>
<li>{icon('pin')}<div><small>כתובת</small><span class="v">{ADDRESS}</span></div></li>
</ul>'''


def contact_form(with_email):
    email = ('<div class="field"><label for="f-email">אימייל</label>'
             '<input id="f-email" name="email" type="email" autocomplete="email" dir="ltr"></div>') if with_email else ''
    return f'''<form class="form" data-mailto="{EMAIL}">
<h3>השאירו פרטים ונחזור אליכם בהקדם.</h3>
<div class="form-row">
<div class="field"><label for="f-name">שם מלא</label><input id="f-name" name="name" type="text" autocomplete="name" required></div>
<div class="field"><label for="f-phone">טלפון</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" dir="ltr" required></div>
</div>
{email}
<div class="field"><label for="f-message">הודעה</label><textarea id="f-message" name="message"></textarea></div>
<button class="btn btn-primary" type="submit">שליחה</button>
</form>'''


def map_embed():
    return (f'<div class="map"><iframe src="{MAP_SRC}" title="{ADDRESS}" loading="lazy" '
            f'referrerpolicy="no-referrer-when-downgrade"></iframe></div>')


# ---------------------------------------------------------------- layout
def nav(c):
    def link(path, label=None, home=False):
        cur = ' aria-current="page"' if c.path == path else ''
        return f'<a href="{c.url(path)}"{cur}>{escape(label or TITLES[path])}</a>'

    def group(label, paths, children=None):
        active = ' is-active' if any(c.path == p or c.path.startswith(p + '/') for p in paths) else ''
        items = ''
        for p in paths:
            sub = ''
            if children and p in children:
                sub = '<ul>' + ''.join(f'<li>{link(k)}</li>' for k in children[p]) + '</ul>'
            items += f'<li>{link(p)}{sub}</li>'
        return (f'<li><button type="button" class="nav-parent{active}" aria-expanded="false">{label}{icon("chevron")}'
                f'</button><ul class="subnav">{items}</ul></li>')

    return f'''<nav class="nav" id="nav" aria-label="ניווט ראשי"><ul>
<li>{link('', 'דף הבית')}</li>
{group('מבנים טרומיים', PRECAST, {P_PORTABLE: PORTABLE_CHILDREN})}
<li>{link(P_LIGHT)}</li>
<li>{link(P_PROJECTS)}</li>
{group('אודות', [P_ABOUT, P_CERTS, P_QUALITY])}
<li>{link(P_CONTACT)}</li>
</ul></nav>'''


def layout(c, title, description, main, cta=True):
    full_title = f'{title} – Rayforms' if c.path else f'Rayforms – {COMPANY}'
    cta_html = f'''<section class="cta"><div class="wrap">
<div><h2>מעוניינים בפרטים נוספים?</h2><p>השאירו פרטים ונחזור אליכם בהקדם.</p></div>
<div class="actions"><a class="btn btn-primary" href="{c.url(P_CONTACT)}">צור קשר</a>
<a class="btn btn-ghost" href="{tel(PHONE_OFFICE)}">{icon('phone')}<span class="ltr">{PHONE_OFFICE}</span></a></div>
</div></section>''' if cta and 'class="aside"' not in main else ''
    precast = ''.join(f'<li><a href="{c.url(p)}">{escape(TITLES[p])}</a></li>' for p in PRECAST + [P_LIGHT])
    company = ''.join(f'<li><a href="{c.url(p)}">{escape(l)}</a></li>' for p, l in [
        (P_ABOUT, 'אודות ר.א.י'), (P_PROJECTS, 'פרויקטים'), (P_CERTS, 'אישורים והסמכות'),
        (P_QUALITY, 'הצהרת מדיניות האיכות'), (P_CONTACT, 'צור קשר')])
    return f'''<!doctype html>
<html lang="he" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(full_title)}</title>
<meta name="description" content="{escape(description)}">
<meta name="theme-color" content="#111820">
<meta property="og:title" content="{escape(full_title)}">
<meta property="og:description" content="{escape(description)}">
<meta property="og:type" content="website">
<meta property="og:locale" content="he_IL">
<link rel="icon" href="{c.asset('img/favicon.svg')}" type="image/svg+xml">
<link rel="preload" href="{c.asset('fonts/heebo-hebrew.woff2')}" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{c.asset('css/style.css')}">
</head>
<body>
<a class="skip" href="#content">דלג לתוכן</a>
<header class="site-header"><div class="wrap">
<a class="brand" href="{c.url('')}" aria-label="ר.א.י – דף הבית"><img src="{c.asset('img/logo.svg')}" alt="ר.א.י" width="76" height="40"></a>
{nav(c)}
<a class="btn btn-primary header-phone" href="{tel(PHONE_OFFICE)}" aria-label="התקשרו {PHONE_OFFICE}">{icon('phone')}<span>{PHONE_OFFICE}</span></a>
<button type="button" class="menu-toggle" aria-controls="nav" aria-expanded="false" aria-label="תפריט">{icon('menu')}</button>
</div></header>
<main id="content">
{main}
</main>
{cta_html}
<footer class="site-footer"><div class="wrap">
<div class="footer-grid">
<div><img src="{c.asset('img/logo.svg')}" alt="ר.א.י" width="84" height="44" loading="lazy">
<p>{escape(COMPANY)}<br>מבנים ואלמנטים טרומיים יבילים ועבודות בניה.</p></div>
<div><h2>תחומי פעילות</h2><ul>{precast}</ul></div>
<div><h2>החברה</h2><ul>{company}</ul></div>
<div><h2>צור קשר</h2><ul>
<li>משרד: <a class="ltr" href="{tel(PHONE_OFFICE)}">{PHONE_OFFICE}</a></li>
<li>מכירות: <a class="ltr" href="{tel(PHONE_SALES)}">{PHONE_SALES}</a></li>
<li><a class="ltr" href="mailto:{EMAIL}">{EMAIL}</a></li>
<li>{ADDRESS}</li>
</ul></div>
</div>
<div class="footer-bottom">כל הזכויות שמורות © 2026</div>
</div></footer>
<script src="{c.asset('js/main.js')}" defer></script>
</body>
</html>
'''


def page_head(c, title, crumbs=(), lead=''):
    items = f'<li><a href="{c.url("")}">דף הבית</a></li>'
    for label, path in crumbs:
        items += f'<li><a href="{c.url(path)}">{escape(label)}</a></li>' if path else f'<li>{escape(label)}</li>'
    items += f'<li aria-current="page">{escape(title)}</li>'
    lead_html = f'<p class="lead">{lead}</p>' if lead else ''
    return (f'<section class="page-head"><div class="wrap"><nav aria-label="מיקום באתר"><ol class="crumbs">{items}</ol></nav>'
            f'<h1>{escape(title)}</h1>{lead_html}</div></section>')


def inner(c, title, crumbs, body, lead='', with_aside=True):
    content = f'<div class="layout"><div>{body}</div>{aside(c)}</div>' if with_aside else body
    return page_head(c, title, crumbs, lead) + f'<section class="section"><div class="wrap">{content}</div></section>'


# ---------------------------------------------------------------- pages
CRUMB_PRECAST = ('מבנים טרומיים', None)
CRUMB_PORTABLE = (TITLES[P_PORTABLE], P_PORTABLE)
CRUMB_PROJECTS = ('פרויקטים', P_PROJECTS)

PROJECT_TEXT = '''<div class="prose">
<p><strong>לחברה נסיון רב בתחומי הקמת פרויקטים:</strong></p>
<ul>
<li>עבודות קבלניות בתחומי הבניין והתשתיות – תכנון, טכנולוגיה וביצוע בשטח.</li>
<li>החברה מבצעת פרויקטים החל בשיטת תכנון ביצוע.</li>
<li>החברה מבצעת פרויקטים המכילות תכנון וביצוע מערכות בנין כגון: אינסטלציה וכיבוי אש, מעליות, מערכות חשמל ומערכות מיזוג אוויר למניהן (VRF).</li>
</ul>
</div>'''


def home(c):
    tiles = [
        (P_TRANSFORMER, 'transformer-rooms.webp'), (P_PROTECTED, 'protected-2.webp'),
        (P_LIGHT, 'light-construction.webp'), (P_POSTAL, 'postal.webp'),
        (P_POLICE, 'police-transit.webp'), (P_PROJECTS, 'project-taibe.webp'),
    ]
    clients = ''.join(
        f'<li><img src="{c.asset("img/clients/" + f + ".webp")}" alt="{escape(n)}" loading="lazy" decoding="async"></li>'
        for f, n in CLIENTS)
    return f'''<section class="hero">
<video class="hero-media" data-src="{c.asset('video/hero.mp4')}" poster="{c.asset('img/hero-poster.jpg')}" muted loop playsinline preload="none" aria-hidden="true" tabindex="-1"></video>
<div class="wrap"><div class="hero-inner">
<span class="eyebrow">ר.א.י – תעשיה לתבניות מתקדמות</span>
<h1>מבנים ואלמנטים טרומיים יבילים ועבודות בניה</h1>
<p>יצרן מאושר של חברת החשמל לחדרי שנאים טרומיים ושל פיקוד העורף למרחבים מוגנים, וקבלן מוכר לעבודות ממשלתיות.</p>
<div class="actions"><a class="btn btn-primary" href="#activity">תחומי פעילות</a><a class="btn btn-ghost" href="{c.url(P_CONTACT)}">צור קשר</a></div>
</div></div>
</section>

<section class="creds" aria-label="אישורים והסמכות"><div class="wrap"><ul>
<li><strong>יצרן מאושר של חברת החשמל</strong><span>לייצור חדרי שנאים טרומיים</span></li>
<li><strong>יצרן מאושר ע"י פיקוד העורף</strong><span>מרחבים מוגנים מוסדיים ודירתיים</span></li>
<li><strong>תקן איכות ISO-9001</strong><span>של מכון התקנים · מפעל מוסמך לתקן 1923 חלק 2</span></li>
<li><strong>סיווג קבלני ענף 100 – ג'5</strong><span>קבלן מוכר לעבודות ממשלתיות</span></li>
</ul></div></section>

<section class="section" id="activity"><div class="wrap">
<div class="section-head"><div><span class="eyebrow">תחומי פעילות</span><h2>מבנים טרומיים, בניה קלה ופרויקטים</h2></div></div>
<div class="grid">{''.join(card(c, p, img) for p, img in tiles)}</div>
</div></section>

<section class="section section-alt"><div class="wrap split">
<div>
<span class="eyebrow">אודות</span>
<h2>נסיון רב בתחומי הבניה והבניה המתועשת</h2>
<p>חברת {escape(COMPANY)} הינה חברה המבצעת מבנים ואלמנטים טרומיים יבילים וכן חברה קבלנית לעבודות בניה.</p>
<ul class="checks">
<li>תכנון וייצור תבניות לעבודות בטון ופיתוח שיטות עבודה מתקדמות.</li>
<li>ייצור אלמנטים טרומיים והספקת מבנים יבילים מבטון.</li>
<li>עבודות קבלניות בתחומי הבניין והתשתיות – תכנון, טכנולוגיה וביצוע בשטח.</li>
</ul>
<a class="link-arrow" href="{c.url(P_ABOUT)}">עוד על החברה {icon('arrow')}</a>
</div>
<div class="split-media"><img src="{c.asset('img/postal.webp')}" alt="הצבת מבנים יבילים באתר" width="1140" height="700" loading="lazy" decoding="async"></div>
</div></section>

<section class="section"><div class="wrap">
<div class="section-head"><div><span class="eyebrow">פרויקטים</span><h2>פרויקטים נבחרים</h2></div>
<a class="link-arrow" href="{c.url(P_PROJECTS)}">לכל הפרויקטים {icon('arrow')}</a></div>
<div class="grid">{''.join(card(c, p, img) for p, img in PROJECTS)}</div>
</div></section>

<section class="section section-alt"><div class="wrap">
<div class="section-head"><div><span class="eyebrow">לקוחות</span><h2>בין לקוחותינו</h2></div></div>
<ul class="clients">{clients}</ul>
</div></section>

<section class="section"><div class="wrap">
<div class="iso"><img src="{c.asset('img/iso-9001-2015.svg')}" alt="ISO 9001:2015" width="150" height="108" loading="lazy">
<div><h2>עומדים בדרישות של ISO 9001:2015</h2><p><a class="link-arrow" href="{c.url(P_CERTS)}">אישורים והסמכות {icon('arrow')}</a></p></div></div>
</div></section>

<section class="section section-alt" id="contact"><div class="wrap">
<div class="contact"><div><span class="eyebrow">צור קשר</span><h2>נשמח לעמוד לרשותכם</h2>{contact_list()}</div>{contact_form(False)}</div>
{map_embed()}
</div></section>'''


def simple(path, crumbs, lead='', images=(), related=None, related_heading='', extra=''):
    def render(c):
        body = ''
        if images:
            body += gallery(c, images, ' flush')
        if not lead and not images and not extra:
            body += f'<div class="prose"><p>לפרטים נוספים על {escape(TITLES[path])} נשמח לעמוד לרשותכם.</p></div>'
        body += extra(c) if callable(extra) else extra
        if related:
            body += pills(c, [p for p in related if p != path], related_heading)
        return inner(c, TITLES[path], crumbs, body, lead)
    return render


def portable(c):
    imgs = {P_PORTS: 'ports-authority.webp', P_POSTAL: 'postal.webp', P_MEKOROT: 'mekorot-buildings.webp', P_POLICE: 'police-transit.webp'}
    body = f'<div class="grid grid-2">{"".join(card(c, p, imgs[p]) for p in PORTABLE_CHILDREN)}</div>'
    body += pills(c, [p for p in PRECAST if p != P_PORTABLE], 'מבנים טרומיים נוספים')
    lead = 'חלק גדול מפעילות החברה בשנים האחרונות היה ייצור מבנים מרחביים (מבנים יבילים). החברה רכשה נסיון רב בתחום זה ובעלת מוניטין בענף.'
    return inner(c, TITLES[P_PORTABLE], [CRUMB_PRECAST], body, lead)


def projects(c):
    body = PROJECT_TEXT + f'<div class="grid" style="margin-top:40px">{"".join(card(c, p, img) for p, img in PROJECTS)}</div>'
    return inner(c, TITLES[P_PROJECTS], [], body, with_aside=False)


def project(path, image):
    def render(c):
        body = PROJECT_TEXT + gallery(c, [(image, TITLES[path])])
        body += pills(c, [p for p, _ in PROJECTS if p != path], 'פרויקטים נוספים')
        return inner(c, TITLES[path], [CRUMB_PROJECTS], body)
    return render


def certs(c):
    items = [('iso-9001.webp', 'אישור ISO 9001'), ('contractor-license.webp', 'רשיון קבלן'), ('standard-1923.webp', 'תו תקן 1923')]
    figs = ''.join(
        f'<figure><a href="{c.asset("img/certs/" + f)}" data-lightbox><img src="{c.asset("img/certs/" + f)}" alt="{t}" '
        f'loading="lazy" decoding="async"></a><figcaption>{t}</figcaption></figure>' for f, t in items)
    body = f'<div class="gallery certs">{figs}</div>'
    return inner(c, TITLES[P_CERTS], [('אודות', P_ABOUT)], body, with_aside=False)


def about(c):
    body = f'''<div class="prose">
<p><strong>חברת {escape(COMPANY)}</strong> הינה חברה המבצעת מבנים ואלמנטים טרומיים יבילים וכן חברה קבלנית לעבודות בניה.</p>
<ul>
<li>החברה הינה בעלת סיווג קבלני – ענף 100 – ג'5 והינה קבלן מוכר לעבודות ממשלתיות באותו הסיווג.</li>
<li>החברה בעלת תקן איכות ISO-9001 של מכון התקנים.</li>
<li>המפעל מוסמך לתקן 1923 חלק 2.</li>
<li>חברתנו הינה יצרן מאושר של חברת החשמל לייצור חדרי שנאים טרומיים.</li>
<li>חברתנו הינה יצרן מאושר ע"י פיקוד העורף לייצור מרחבים מוגנים מוסדיים ודירתיים.</li>
</ul>

<h2>תחומי נסיון</h2>
<p>לחברה נסיון רב בתחומי הבניה והבניה מתועשת:</p>
<ul>
<li>תכנון וייצור תבניות לעבודות בטון ופיתוח שיטות עבודה מתקדמות.</li>
<li>ייצור אלמנטיים טרומיים.</li>
<li>ייצור והספקת מבנים יבילים מבטון.</li>
<li>עבודות קבלניות בתחומי הבניין והתשתיות – תכנון, טכנולוגיה וביצוע בשטח.</li>
<li>החברה מבצעת פרויקטים החל בשיטת תכנון ביצוע.</li>
<li>החברה מבצעת פרויקטים המכילות תכנון וביצוע מערכות בנין כגון: אינסטלציה וכיבוי אש, מעליות, מערכות חשמל ומערכות מיזוג אוויר למניהן (VRF).</li>
</ul>

<h2>כוח אדם ומשאבים</h2>
<h3>כוח אדם</h3>
<p>החברה מורכבת מצוות רב מקצועי הכולל מהנדסים, אדריכלים, מנהלי עבודה וצוותי ביצוע מקצועיים אשר ניידים ברחבי הארץ ואחראים לביצוע עבודות ההרכבה, בניה קונבנציונלית הפיתוח והגמרים.</p>
<h3>מפעל החברה</h3>
<p>מפעל החברה ליצור מבנים יבילים, אלמנטים טרומיים ממוקם באזור תעשיה הר יונה בנצרת עילית ובו מרוכז חלק גדול מפעילות החברה: משרדי הנהלה, תכנון, מכירות, יצור.<br>מפעל נוסף באזור התעשייה מבואות הגלבוע בשטח מעל 5000 מ"ר.</p>

<h2>יתרונות החברה</h2>
<h3>שימוש בשיטות מתועשות</h3>
<p>המוצרים עוברים תהלכי בקרת איכות אשר מבטיחים רמה גבוה של המוצר.</p>
<h3>משך הביצוע</h3>
<p>השיטות שלנו מאפשרות לבצע משימות רבות בלוחות הזמנים המינימליים ולחסוך בכוח עבודה ולשמור על טיב העבודה המרבי.</p>
<p>השימוש בשיטות שלנו מאפשר לעבוד עם צוות מצומצם של עובדים וזה מאפשר לבצע פרויקטים באתרים שונים ולהפריע כמה שפחות להתנהלות השוטפת.</p>
<p>המבנים יכול לשמש לכל הפונקציות הנדרשות לפי פרוגרמת המזמין: כיתות לימוד, משרדים, חדרי ישיבות, חדרי מגורים ועוד.</p>
<h3>מבנים מרחביים</h3>
<p>חלק גדול מפעילות החברה בשנים האחרונות היה ייצור מבנים מרחביים (מבנים יבילים). החברה רכשה נסיון רב בתחום זה ובעלת מוניטין בענף.</p>
</div>'''
    body += pills(c, [P_CERTS, P_QUALITY, P_PROJECTS], 'עוד על החברה')
    return inner(c, TITLES[P_ABOUT], [], body)


def quality(c):
    body = '''<div class="prose">
<p><strong>חברת ר.א.י תעשיה לתבניות מתקדמות בע"מ</strong> הינה חברה המבצעת מבנים ואלמנטים טרומים יבילים וכן קבלנית לעבודות בנייה.</p>
<p>החברה רואה בהשגת רמת איכות גבוהה בפרויקטים של החברה, דרך עיקרית לרכישת אמונם ושביעות רצונם של לקוחות החברה. החברה מאמינה שזהו תנאי הכרחי להמשך שגשוגה והתפתחותה של החברה.</p>
<p>החברה רואה כמטרה אסטרטגית מענה לדרישות וציפיות לקוחות החברה ברמת גימור גבוהה, טיפול רציף ומסור לאורך שלבי העבודה, עמידה בלוח זמנים למסירת האתר ומתן שירות טוב ללקוח לאחר מסירת הפרויקט.</p>
<p>הנהלת החברה מאמינה כי שיתוף העובדים בהקמת והפעלת מערכת האיכות הוא תנאי הכרחי להצלחתה.</p>
<p>הנהלת החברה מאמינה בשיפור ופיתוח מתמיד של מערכות החברה בכלל ושל העובדים בפרט.</p>
<p>כל הנהלים במדריך האיכות גובשו ע"י הנהלת החברה, ומטרתה של החברה היא שנהלים אלו יקוימו בקפדנות.</p>
<p>מטרת קובץ הנהלים של מדריך האיכות בחברה היא למסד מערך הבטחת איכות שיקיים רמת איכות התואמת את דרישות האיכות של <strong>ת"י ISO 9001:2008</strong>, לקבוע שיטות עמידה ונהלים אשר באמצעותם יושגו מטרות האיכות של החברה.</p>
<p>כל עובדי החברה מחויבים ליישום הדרישות המצוינות במדריך האיכות, ולהבטחת האיכות המפורטת בכל שלבי העבודה הנוגעים לתחומי פעילותם או המושפעים על ידם.</p>
<p>להבטחת האיכות יוקצו משאבים ע"פ הצורך, על מנת להוציא לפועל את דרישות התקן.</p>
<p>הנהלת החברה תדאג ליידע את כל העובדים בפרטי נוהל הבטחת איכות ע"י פעולות הדרכה ורענון שוטפות.</p>
<p>הנהלת הארגון מחויבת לתהליך שיפור מתמיד של אפקטיביות מערכת הניהול וזאת באמצעות כלים אשר יוגדרו במדריך האיכות של החברה כגון סקרי הנהלה ומבדקי איכות פנימיים וכן באמצעות משאבים שיוקצו לנושא.</p>
<p>הנהלת הארגון מוייבת לעמוד בכל הדרישות התחוקתיות של מדינת ישראל הקשורות לתחום העבודה של האירגון.</p>
<p>הנהלת החברה תדאג לכך שהנהלים יהיו ידועים ומובנים לכל העובדים בתחומי עבודתם הרלוונטיים.</p>
<p>הנהלת החברה תנהל בישיבותיה השוטפות מעקב אחר תהליך יישום מדיניות האיכות. כמו כן יערך מעקב תקופתי בישיבות סקרי הנהלה בנושא הבטחת איכות.</p>
<p class="signature">על החתום,<br>אינג' בוריס ויינברג.<span>מנכ"ל החברה.</span></p>
</div>'''
    body += pills(c, [P_CERTS, P_ABOUT], 'עוד על החברה')
    return inner(c, TITLES[P_QUALITY], [('אודות', P_ABOUT)], body)


def contact(c):
    main = page_head(c, TITLES[P_CONTACT], [], 'השאירו פרטים ונחזור אליכם בהקדם.')
    main += (f'<section class="section"><div class="wrap"><div class="contact"><div><h2>פרטי התקשרות</h2>'
             f'{contact_list()}</div>{contact_form(True)}</div>{map_embed()}</div></section>')
    return main


D_DEFAULT = 'ר.א.י (תעשיה לתבניות מתקדמות) בע"מ – מבנים ואלמנטים טרומיים יבילים ועבודות בניה.'
D_TRANSFORMER = 'חברתנו הינה יצרן מאושר לאספקת חדרי שנאים טרומיים על ידי חברת החשמל.'
D_PROTECTED = 'חברתנו הינה יצרן מאושר ע"י פיקוד העורף לייצור מרחבים מוגנים מוסדיים ודירתיים.'
PRECAST_MORE = 'מבנים טרומיים נוספים'
PORTABLE_MORE = 'מבנים מרחביים יבילים נוספים'

# (path, description, renderer, show CTA band)
PAGES = [
    ('', D_DEFAULT, home, False),
    (P_TRANSFORMER, D_TRANSFORMER, simple(
        P_TRANSFORMER, [CRUMB_PRECAST], D_TRANSFORMER,
        [('transformer-rooms.webp', TITLES[P_TRANSFORMER])], PRECAST, PRECAST_MORE), True),
    (P_PROTECTED, D_PROTECTED, simple(
        P_PROTECTED, [CRUMB_PRECAST], D_PROTECTED,
        [('protected-1.webp', 'הצבת מרחב מוגן'), ('protected-2.webp', 'הובלת מרחב מוגן'),
         ('ports-authority.webp', 'מרחב מוגן עבור רשות הנמלים')], PRECAST, PRECAST_MORE), True),
    (P_PORTABLE, D_DEFAULT, portable, True),
    (P_PORTS, 'מקלטים מיוחדים עבור רשות הנמלים.', simple(
        P_PORTS, [CRUMB_PRECAST, CRUMB_PORTABLE], 'מקלטים מיוחדים עבור רשות הנמלים',
        [('ports-authority.webp', TITLES[P_PORTS])], PORTABLE_CHILDREN, PORTABLE_MORE), True),
    (P_POSTAL, D_DEFAULT, simple(
        P_POSTAL, [CRUMB_PRECAST, CRUMB_PORTABLE], '',
        [('postal.webp', TITLES[P_POSTAL])], PORTABLE_CHILDREN, PORTABLE_MORE), True),
    (P_MEKOROT, D_DEFAULT, simple(
        P_MEKOROT, [CRUMB_PRECAST, CRUMB_PORTABLE], '',
        [('mekorot-buildings.webp', TITLES[P_MEKOROT])], PORTABLE_CHILDREN, PORTABLE_MORE), True),
    (P_POLICE, D_DEFAULT, simple(
        P_POLICE, [CRUMB_PRECAST, CRUMB_PORTABLE], '',
        [('police-transit.webp', TITLES[P_POLICE])], PORTABLE_CHILDREN, PORTABLE_MORE), True),
    (P_ARMORY, D_DEFAULT, simple(P_ARMORY, [CRUMB_PRECAST], related=PRECAST, related_heading=PRECAST_MORE), True),
    (P_GUARD, D_DEFAULT, simple(P_GUARD, [CRUMB_PRECAST], related=PRECAST, related_heading=PRECAST_MORE), True),
    (P_LIGHT, D_DEFAULT, simple(P_LIGHT, [], '', [('light-construction.webp', TITLES[P_LIGHT])]), True),
    (P_PROJECTS, 'לחברה נסיון רב בתחומי הקמת פרויקטים: עבודות קבלניות בתחומי הבניין והתשתיות.', projects, True),
    (P_ABOUT, D_DEFAULT, about, True),
    (P_CERTS, 'אישורים והסמכות: ISO 9001, רשיון קבלן ותו תקן 1923.', certs, True),
    (P_QUALITY, 'הצהרת מדיניות האיכות של חברת ר.א.י תעשיה לתבניות מתקדמות בע"מ.', quality, True),
    (P_CONTACT, f'צור קשר: {PHONE_OFFICE}, {ADDRESS}.', contact, False),
] + [(p, D_DEFAULT, project(p, img), True) for p, img in PROJECTS]


def main():
    for path, description, render, cta in PAGES:
        c = Ctx(path)
        html = layout(c, TITLES.get(path, ''), description, render(c), cta)
        out = os.path.join(ROOT, path, 'index.html')
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, 'w', encoding='utf-8') as f:
            f.write(html)
    print(f'built {len(PAGES)} pages')


if __name__ == '__main__':
    main()
