#!/usr/bin/env python3
"""Builds the static site. Run `python3 build.py` from the repository root.

All page content lives in this file, in Hebrew ('he') and English ('en').
Shared layout (header, footer) is defined once and written into every page.
Hebrew pages are written at the repository root, English pages under /en/.
"""
import os
from html import escape

ROOT = os.path.dirname(os.path.abspath(__file__))
LANGS = ('he', 'en')

# Phone links always dial the international number; the displayed format is per language (see T).
TEL_OFFICE = 'tel:+97246020505'
TEL_SALES = 'tel:+972504728956'
EMAIL = 'ariel@rayforms.co.il'
MAP_SRC = ('https://maps.google.com/maps?q=%D7%94%D7%A6%D7%95%D7%A8%D7%A3%201%20'
           '%D7%A0%D7%95%D7%A3%20%D7%94%D7%92%D7%9C%D7%99%D7%9C&t=m&z=10&output=embed&iwloc=near')

# ---------------------------------------------------------------- pages
# key: (Hebrew path, English path, Hebrew title, English title)
PAGE_INFO = {
    'home': ('', 'en', '', ''),
    'projects': ('פרויקטים', 'en/projects', 'פרויקטים', 'Projects'),
    'protected': ('מבנים-טרומיים/מרחבים-מוגנים', 'en/precast/protected-spaces',
                  'מרחבים מוגנים', 'Protected Spaces'),
    'transformer': ('מבנים-טרומיים/חדרי-טרנספורמציה', 'en/precast/transformer-rooms',
                    'ייצור חדרי שנאים (חדרי טרפו)', 'Transformer Rooms'),
    'portable': ('מבנים-טרומיים/מבנים-מרחביים-יבילים', 'en/precast/portable-buildings',
                 'מבנים מרחביים יבילים', 'Portable Modular Buildings'),
    'ports': ('מבנים-טרומיים/מבנים-מרחביים-יבילים/רשות-הנמלים', 'en/precast/portable-buildings/ports-authority',
              'רשות הנמלים', 'Ports Authority'),
    'postal': ('מבנים-טרומיים/מבנים-מרחביים-יבילים/מבני-חלוקת-דואר', 'en/precast/portable-buildings/mail-distribution',
               'מבני חלוקת דואר', 'Mail Distribution Buildings'),
    'mekorot': ('מבנים-טרומיים/מבנים-מרחביים-יבילים/מבנים-לחברת-מקורות', 'en/precast/portable-buildings/mekorot',
                'מבנים לחברת מקורות', 'Buildings for Mekorot'),
    'police': ('מבנים-טרומיים/מבנים-מרחביים-יבילים/מבנה-מעבר-משטרת-ישראל', 'en/precast/portable-buildings/israel-police-checkpoint',
               'מבנה מעבר משטרת ישראל', 'Israel Police Checkpoint Building'),
    'armory': ('מבנים-טרומיים/חדרי-נשק', 'en/precast/armories', 'חדרי נשק', 'Armories'),
    'guard': ('מבנים-טרומיים/חדרי-שומר', 'en/precast/guard-booths', 'חדרי שומר', 'Guard Booths'),
    'light': ('בניה-קלה', 'en/light-construction', 'בניה קלה', 'Light Construction'),
    'certs': ('אישורים-והסמכות', 'en/certifications', 'אישורים והסמכות', 'Certifications'),
    'quality': ('הצהרת-מדיניות-האיכות', 'en/quality-policy', 'הצהרת מדיניות האיכות', 'Quality Policy Statement'),
    'about': ('אודות', 'en/about', 'אודות ר.א.י (תעשיה לתבניות מתקדמות) בע"מ',
              'About R.A.Y. (Advanced Formwork Industries) Ltd.'),
    'contact': ('צור-קשר', 'en/contact', 'צור קשר', 'Contact'),
    'prj_tzur': ('projects/הקמת-משטרת-צור-באהר', 'en/projects/tzur-baher-police-station',
                 'הקמת משטרת צור באהר', 'Tzur Baher Police Station'),
    'prj_taibe': ('projects/משטרת-טייבה', 'en/projects/taibe-police-station',
                  'משטרת טייבה', 'Taibe Police Station'),
    'prj_camp': ('projects/מחנה-בשטח-של-כ-5000-מר', 'en/projects/camp-5000-sqm',
                 'מחנה בשטח של כ-5000 מ״ר', 'Camp of Approx. 5,000 m²'),
}

PRECAST = ['protected', 'transformer', 'portable', 'armory', 'guard']
PORTABLE_CHILDREN = ['ports', 'postal', 'mekorot', 'police']
PROJECTS = [('prj_tzur', 'project-tzur-baher.webp'), ('prj_taibe', 'project-taibe.webp'), ('prj_camp', 'project-camp.webp')]
CLIENTS = [
    ('bezek', 'בזק', 'Bezeq'), ('cellcom', 'סלקום', 'Cellcom'), ('doar', 'דואר ישראל', 'Israel Post'),
    ('hashmal', 'חברת החשמל', 'Israel Electric Corporation'), ('amidar', 'עמידר', 'Amidar'),
    ('keisaria', 'החברה לפיתוח קיסריה', 'Caesarea Development Corporation'),
    ('police', 'משטרת ישראל', 'Israel Police'), ('shikun', 'שיכון ובינוי סולל בונה', 'Shikun & Binui Solel Boneh'),
    ('amigur', 'עמיגור', 'Amigour'), ('haklaut', 'משרד החקלאות ופיתוח הכפר', 'Ministry of Agriculture and Rural Development'),
    ('mekorot', 'מקורות', 'Mekorot'),
]

# Alternative designs offered in the "Designs" menu: (id, Hebrew name, English name, swatch colours).
# The look of each is defined in assets/css/themes.css.
DESIGNS = [
    ('classic', 'קלאסי (נוכחי)', 'Classic (current)', '#dd313f', '#111820'),
    ('graphite', 'גרפיט – כהה', 'Graphite – dark', '#e5404d', '#0f1419'),
    ('concrete', 'בטון – תעשייתי', 'Concrete – industrial', '#c8392b', '#d6d2ca'),
    ('blueprint', 'שרטוט – כחול', 'Blueprint – blue', '#1f6fd0', '#0f2742'),
    ('safety', 'צהוב בטיחות', 'Safety yellow', '#f7b500', '#16181b'),
    ('editorial', 'קלאסי עם סריף', 'Editorial – serif', '#8f1d2c', '#f2ecdf'),
    ('galilee', 'גליל – ירוק', 'Galilee – green', '#2f7a55', '#f1eee3'),
    ('steel', 'פלדה – טורקיז', 'Steel – teal', '#0e8f87', '#1c2733'),
    ('soft', 'רך – מעוגל', 'Soft – rounded', '#4f46e5', '#f3f4fc'),
]

# Alternative page layouts offered in the same menu: (id, Hebrew name, English name).
# Each is defined in assets/css/layouts.css and can be combined with any colour scheme.
LAYOUTS = [
    ('standard', 'רגיל (נוכחי)', 'Standard (current)'),
    ('centered', 'ממורכז', 'Centered'),
    ('split', 'מפוצל – טקסט לצד וידאו', 'Split – text beside video'),
    ('sidebar', 'תפריט צד', 'Side menu'),
    ('showcase', 'תצוגה – תמונות גדולות', 'Showcase – large photos'),
    ('compact', 'קומפקטי – רשימה', 'Compact – list'),
]

# ---------------------------------------------------------------- text
T = {
    'he': dict(
        dir='rtl', locale='he_IL', other_label='EN', other_name='English',
        company='ר.א.י (תעשיה לתבניות מתקדמות) בע"מ', brand='ר.א.י',
        address='הצורף 1, נוף-הגליל', phone_office='04-6020505', phone_sales='050-4728956',
        skip='דלג לתוכן', home='דף הבית', nav_label='ניווט ראשי', menu='תפריט', crumbs_label='מיקום באתר',
        brand_home='ר.א.י – דף הבית', call='התקשרו',
        nav_precast='מבנים טרומיים', nav_about='אודות', nav_designs='עיצובים', designs_layout='תבנית', designs_colors='ערכת צבעים', about_short='אודות ר.א.י',
        footer_tagline='מבנים ואלמנטים טרומיים יבילים ועבודות בניה.',
        footer_activity='תחומי פעילות', footer_company='החברה', rights='כל הזכויות שמורות © 2026',
        office='משרד', sales='מכירות', email='אימייל', address_label='כתובת',
        contact='צור קשר', cta_title='מעוניינים בפרטים נוספים?', cta_text='השאירו פרטים ונחזור אליכם בהקדם.',
        form_title='השאירו פרטים ונחזור אליכם בהקדם.', f_name='שם מלא', f_phone='טלפון', f_message='הודעה', f_send='שליחה',
        contact_details='פרטי התקשרות',
        more_precast='מבנים טרומיים נוספים', more_portable='מבנים מרחביים יבילים נוספים',
        more_projects='פרויקטים נוספים', more_company='עוד על החברה',
        empty='לפרטים נוספים על {} נשמח לעמוד לרשותכם.',
        d_default='ר.א.י (תעשיה לתבניות מתקדמות) בע"מ – מבנים ואלמנטים טרומיים יבילים ועבודות בניה.',
        d_transformer='חברתנו הינה יצרן מאושר לאספקת חדרי שנאים טרומיים על ידי חברת החשמל.',
        d_protected='חברתנו הינה יצרן מאושר ע"י פיקוד העורף לייצור מרחבים מוגנים מוסדיים ודירתיים.',
        d_ports='מקלטים מיוחדים עבור רשות הנמלים',
        d_portable='חלק גדול מפעילות החברה בשנים האחרונות היה ייצור מבנים מרחביים (מבנים יבילים). החברה רכשה נסיון רב בתחום זה ובעלת מוניטין בענף.',
        d_projects='לחברה נסיון רב בתחומי הקמת פרויקטים: עבודות קבלניות בתחומי הבניין והתשתיות.',
        d_certs='אישורים והסמכות: ISO 9001, רשיון קבלן ותו תקן 1923.',
        d_quality='הצהרת מדיניות האיכות של חברת ר.א.י תעשיה לתבניות מתקדמות בע"מ.',
        alt_protected=['הצבת מרחב מוגן', 'הובלת מרחב מוגן', 'מרחב מוגן עבור רשות הנמלים'],
        certs=['אישור ISO 9001', 'רשיון קבלן', 'תו תקן 1923'],
        # home
        hero_eyebrow='ר.א.י – תעשיה לתבניות מתקדמות',
        hero_title='מבנים ואלמנטים טרומיים יבילים ועבודות בניה',
        hero_text='יצרן מאושר של חברת החשמל לחדרי שנאים טרומיים ושל פיקוד העורף למרחבים מוגנים, וקבלן מוכר לעבודות ממשלתיות.',
        hero_btn='תחומי פעילות',
        creds_label='אישורים והסמכות',
        creds=[('יצרן מאושר של חברת החשמל', 'לייצור חדרי שנאים טרומיים'),
               ('יצרן מאושר ע"י פיקוד העורף', 'מרחבים מוגנים מוסדיים ודירתיים'),
               ('תקן איכות ISO-9001', 'של מכון התקנים · מפעל מוסמך לתקן 1923 חלק 2'),
               ("סיווג קבלני ענף 100 – ג'5", 'קבלן מוכר לעבודות ממשלתיות')],
        act_eyebrow='תחומי פעילות', act_title='מבנים טרומיים, בניה קלה ופרויקטים',
        about_eyebrow='אודות', about_title='נסיון רב בתחומי הבניה והבניה המתועשת',
        about_text='חברת ר.א.י (תעשיה לתבניות מתקדמות) בע"מ הינה חברה המבצעת מבנים ואלמנטים טרומיים יבילים וכן חברה קבלנית לעבודות בניה.',
        about_points=['תכנון וייצור תבניות לעבודות בטון ופיתוח שיטות עבודה מתקדמות.',
                      'ייצור אלמנטים טרומיים והספקת מבנים יבילים מבטון.',
                      'עבודות קבלניות בתחומי הבניין והתשתיות – תכנון, טכנולוגיה וביצוע בשטח.'],
        about_more='עוד על החברה', about_img_alt='הצבת מבנים יבילים באתר',
        prj_eyebrow='פרויקטים', prj_title='פרויקטים נבחרים', prj_all='לכל הפרויקטים',
        clients_eyebrow='לקוחות', clients_title='בין לקוחותינו',
        iso_title='עומדים בדרישות של ISO 9001:2015',
        contact_title='נשמח לעמוד לרשותכם',
    ),
    'en': dict(
        dir='ltr', locale='en_US', other_label='עב', other_name='עברית',
        company='R.A.Y. (Advanced Formwork Industries) Ltd.', brand='R.A.Y.',
        address='HaTsoref St 1, Nof HaGalil, Israel', phone_office='+972-4-602-0505', phone_sales='+972-50-472-8956',
        skip='Skip to content', home='Home', nav_label='Main navigation', menu='Menu', crumbs_label='Breadcrumb',
        brand_home='R.A.Y. – Home', call='Call',
        nav_precast='Precast Structures', nav_about='About', nav_designs='Designs', designs_layout='Layout', designs_colors='Colour scheme', about_short='About R.A.Y.',
        footer_tagline='Portable precast structures and elements, and construction works.',
        footer_activity='What we do', footer_company='Company', rights='All rights reserved © 2026',
        office='Office', sales='Sales', email='Email', address_label='Address',
        contact='Contact', cta_title='Would you like more details?', cta_text='Leave your details and we will get back to you shortly.',
        form_title='Leave your details and we will get back to you shortly.', f_name='Full name', f_phone='Phone', f_message='Message', f_send='Send',
        contact_details='Contact details',
        more_precast='More precast structures', more_portable='More portable modular buildings',
        more_projects='More projects', more_company='More about the company',
        empty='For more details about {}, we will be glad to assist you.',
        d_default='R.A.Y. (Advanced Formwork Industries) Ltd. – portable precast structures and elements, and construction works.',
        d_transformer='Our company is a manufacturer approved by the Israel Electric Corporation to supply precast transformer rooms.',
        d_protected='Our company is a manufacturer approved by the Home Front Command to produce institutional and residential protected spaces.',
        d_ports='Special shelters for the Ports Authority',
        d_portable='In recent years, a large part of the company\'s activity has been the production of modular (portable) buildings. The company has gained extensive experience in this field and has a strong reputation in the industry.',
        d_projects='The company has extensive experience in project construction: contracting works in building and infrastructure.',
        d_certs='Certifications: ISO 9001, contractor license and Israeli Standard 1923 mark.',
        d_quality='Quality policy statement of R.A.Y. Advanced Formwork Industries Ltd.',
        alt_protected=['Placing a protected space', 'Transporting a protected space', 'Protected space for the Ports Authority'],
        certs=['ISO 9001 certificate', 'Contractor license', 'Standard 1923 mark'],
        # home
        hero_eyebrow='R.A.Y. – Advanced Formwork Industries',
        hero_title='Portable precast structures and elements, and construction works',
        hero_text='An approved manufacturer of precast transformer rooms for the Israel Electric Corporation and of protected spaces for the Home Front Command, and a recognized contractor for government works.',
        hero_btn='What we do',
        creds_label='Certifications',
        creds=[('Approved by the Israel Electric Corporation', 'Manufacturer of precast transformer rooms'),
               ('Approved by the Home Front Command', 'Institutional and residential protected spaces'),
               ('ISO 9001 quality standard', 'Standards Institution of Israel · plant certified to Standard 1923 Part 2'),
               ('Contractor classification: Branch 100, G-5', 'Recognized contractor for government works')],
        act_eyebrow='What we do', act_title='Precast structures, light construction and projects',
        about_eyebrow='About', about_title='Extensive experience in construction and industrialized building',
        about_text='R.A.Y. (Advanced Formwork Industries) Ltd. produces portable precast structures and elements, and is also a contracting company for construction works.',
        about_points=['Design and manufacture of formwork for concrete works, and development of advanced working methods.',
                      'Manufacture of precast elements and supply of portable concrete buildings.',
                      'Contracting works in building and infrastructure – design, technology and on-site execution.'],
        about_more='More about the company', about_img_alt='Placing portable buildings on site',
        prj_eyebrow='Projects', prj_title='Selected projects', prj_all='All projects',
        clients_eyebrow='Clients', clients_title='Among our clients',
        iso_title='Meeting the requirements of ISO 9001:2015',
        contact_title='We will be glad to assist you',
    ),
}

PROJECT_TEXT = {
    'he': '''<div class="prose">
<p><strong>לחברה נסיון רב בתחומי הקמת פרויקטים:</strong></p>
<ul>
<li>עבודות קבלניות בתחומי הבניין והתשתיות – תכנון, טכנולוגיה וביצוע בשטח.</li>
<li>החברה מבצעת פרויקטים החל בשיטת תכנון ביצוע.</li>
<li>החברה מבצעת פרויקטים המכילות תכנון וביצוע מערכות בנין כגון: אינסטלציה וכיבוי אש, מעליות, מערכות חשמל ומערכות מיזוג אוויר למניהן (VRF).</li>
</ul>
</div>''',
    'en': '''<div class="prose">
<p><strong>The company has extensive experience in project construction:</strong></p>
<ul>
<li>Contracting works in building and infrastructure – design, technology and on-site execution.</li>
<li>The company carries out projects using the design-build method.</li>
<li>The company carries out projects that include the design and installation of building systems such as plumbing and fire protection, elevators, electrical systems and air-conditioning systems of all types (VRF).</li>
</ul>
</div>''',
}

ABOUT_TEXT = {
    'he': '''<div class="prose">
<p><strong>חברת ר.א.י (תעשיה לתבניות מתקדמות) בע"מ</strong> הינה חברה המבצעת מבנים ואלמנטים טרומיים יבילים וכן חברה קבלנית לעבודות בניה.</p>
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
</div>''',
    'en': '''<div class="prose">
<p><strong>R.A.Y. (Advanced Formwork Industries) Ltd.</strong> produces portable precast structures and elements, and is also a contracting company for construction works.</p>
<ul>
<li>The company holds contractor classification Branch 100, G-5, and is a recognized contractor for government works in that classification.</li>
<li>The company holds the ISO 9001 quality standard from the Standards Institution of Israel.</li>
<li>The plant is certified to Israeli Standard 1923 Part 2.</li>
<li>Our company is a manufacturer approved by the Israel Electric Corporation to produce precast transformer rooms.</li>
<li>Our company is a manufacturer approved by the Home Front Command to produce institutional and residential protected spaces.</li>
</ul>

<h2>Areas of experience</h2>
<p>The company has extensive experience in construction and industrialized building:</p>
<ul>
<li>Design and manufacture of formwork for concrete works, and development of advanced working methods.</li>
<li>Manufacture of precast elements.</li>
<li>Manufacture and supply of portable concrete buildings.</li>
<li>Contracting works in building and infrastructure – design, technology and on-site execution.</li>
<li>The company carries out projects using the design-build method.</li>
<li>The company carries out projects that include the design and installation of building systems such as plumbing and fire protection, elevators, electrical systems and air-conditioning systems of all types (VRF).</li>
</ul>

<h2>Personnel and resources</h2>
<h3>Personnel</h3>
<p>The company is made up of a multidisciplinary team of engineers, architects, site managers and professional crews who travel throughout the country and are responsible for assembly works, conventional construction, site development and finishes.</p>
<h3>The company's plant</h3>
<p>The company's plant for producing portable buildings and precast elements is located in the Har Yona industrial zone in Nazareth Illit (now Nof HaGalil), where a large part of the company's activity is concentrated: management offices, design, sales and production.<br>An additional plant, covering more than 5,000 m², is located in the Mevo'ot HaGilboa industrial zone.</p>

<h2>The company's advantages</h2>
<h3>Industrialized methods</h3>
<p>The products go through quality-control processes that ensure a high standard of product.</p>
<h3>Execution time</h3>
<p>Our methods make it possible to complete many tasks on minimal schedules, save labor and maintain the highest quality of work.</p>
<p>Using our methods makes it possible to work with a small crew, which allows projects to be carried out at various sites with as little disruption as possible to day-to-day operations.</p>
<p>The buildings can serve any function required by the client's program: classrooms, offices, meeting rooms, living quarters and more.</p>
<h3>Modular buildings</h3>
<p>In recent years, a large part of the company's activity has been the production of modular (portable) buildings. The company has gained extensive experience in this field and has a strong reputation in the industry.</p>
</div>''',
}

QUALITY_TEXT = {
    'he': '''<div class="prose">
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
</div>''',
    'en': '''<div class="prose">
<p><strong>R.A.Y. Advanced Formwork Industries Ltd.</strong> produces portable precast structures and elements, and is also a contractor for construction works.</p>
<p>The company regards achieving a high level of quality in its projects as the principal way to earn the trust and satisfaction of its clients. The company believes this is an essential condition for its continued prosperity and development.</p>
<p>The company sees as a strategic goal meeting its clients' requirements and expectations with a high standard of finish, continuous and dedicated attention throughout the stages of the work, meeting the schedule for handing over the site, and providing good service to the client after the project is delivered.</p>
<p>The company's management believes that involving employees in establishing and operating the quality system is an essential condition for its success.</p>
<p>The company's management believes in the continual improvement and development of the company's systems in general and of its employees in particular.</p>
<p>All the procedures in the quality manual were formulated by the company's management, and the company's aim is that these procedures be strictly followed.</p>
<p>The purpose of the procedures in the company's quality manual is to establish a quality-assurance system that maintains a level of quality meeting the requirements of <strong>Israeli Standard ISO 9001:2008</strong>, and to set out the methods and procedures through which the company's quality objectives will be achieved.</p>
<p>All company employees are committed to implementing the requirements set out in the quality manual, and to the quality assurance specified at every stage of the work that relates to, or is affected by, their areas of activity.</p>
<p>Resources will be allocated for quality assurance as needed, in order to put the requirements of the standard into practice.</p>
<p>The company's management will make sure all employees are informed of the details of the quality-assurance procedure through ongoing training and refresher activities.</p>
<p>The organization's management is committed to a process of continual improvement of the effectiveness of the management system, using tools defined in the company's quality manual, such as management reviews and internal quality audits, and resources allocated for this purpose.</p>
<p>The organization's management is committed to meeting all the legal requirements of the State of Israel that relate to the organization's field of work.</p>
<p>The company's management will make sure the procedures are known and understood by all employees in their relevant areas of work.</p>
<p>The company's management will monitor the implementation of the quality policy in its regular meetings. In addition, quality assurance will be reviewed periodically in management review meetings.</p>
<p class="signature">Signed,<br>Eng. Boris Weinberg<span>Chief Executive Officer</span></p>
</div>''',
}

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
    cls = 'icon icon-dir' if name == 'arrow' else 'icon'
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true">{ICONS[name]}</svg>'


# ---------------------------------------------------------------- helpers
class Ctx:
    """Per-page context: language, text lookup, and links relative to the page being written."""

    def __init__(self, lang, key):
        self.lang = lang
        self.key = key
        self.t = T[lang]
        self.path = self.path_of(key)
        self.root = '../' * len(self.path.split('/')) if self.path else ''

    def path_of(self, key, lang=None):
        return PAGE_INFO[key][LANGS.index(lang or self.lang)]

    def title(self, key):
        return PAGE_INFO[key][2 + LANGS.index(self.lang)]

    def url(self, key, lang=None):
        path = self.path_of(key, lang)
        return (self.root + path + '/') if path else (self.root or './')

    def asset(self, path):
        return self.root + 'assets/' + path


def card(c, key, image=None):
    media = ''
    cls = 'card card-plain'
    if image:
        cls = 'card'
        media = (f'<div class="card-media"><img src="{c.asset("img/" + image)}" alt="" '
                 f'width="1140" height="700" loading="lazy" decoding="async"></div>')
    return (f'<article class="{cls}">{media}<div class="card-body">'
            f'<h3><a href="{c.url(key)}">{escape(c.title(key))}</a></h3>{icon("arrow")}</div></article>')


def gallery(c, images, extra=''):
    cls = 'gallery' + (' single' if len(images) == 1 else '') + extra
    items = ''.join(
        f'<a href="{c.asset("img/" + src)}" data-lightbox><img src="{c.asset("img/" + src)}" '
        f'alt="{escape(alt)}" width="1140" height="700" loading="lazy" decoding="async"></a>'
        for src, alt in images)
    return f'<div class="{cls}">{items}</div>'


def pills(c, keys, heading):
    items = ''.join(f'<li><a href="{c.url(k)}">{escape(c.title(k))}</a></li>' for k in keys)
    return f'<div class="related"><h2>{heading}</h2><ul class="pills">{items}</ul></div>'


def aside(c):
    t = c.t
    return f'''<aside class="aside">
<h2>{t['cta_title']}</h2>
<p>{t['cta_text']}</p>
<a class="btn btn-primary" href="{c.url('contact')}">{t['contact']}</a>
<a class="btn btn-outline" href="{TEL_OFFICE}">{icon('phone')}<span class="ltr">{t['phone_office']}</span></a>
</aside>'''


def contact_list(c):
    t = c.t
    return f'''<ul class="contact-list">
<li>{icon('phone')}<div><small>{t['office']}</small><a class="ltr" href="{TEL_OFFICE}">{t['phone_office']}</a></div></li>
<li>{icon('phone')}<div><small>{t['sales']}</small><a class="ltr" href="{TEL_SALES}">{t['phone_sales']}</a></div></li>
<li>{icon('mail')}<div><small>{t['email']}</small><a class="ltr" href="mailto:{EMAIL}">{EMAIL}</a></div></li>
<li>{icon('pin')}<div><small>{t['address_label']}</small><span class="v">{t['address']}</span></div></li>
</ul>'''


def contact_form(c, with_email):
    t = c.t
    email = (f'<div class="field"><label for="f-email">{t["email"]}</label>'
             '<input id="f-email" name="email" type="email" autocomplete="email" dir="ltr"></div>') if with_email else ''
    return f'''<form class="form" data-mailto="{EMAIL}">
<h3>{t['form_title']}</h3>
<div class="form-row">
<div class="field"><label for="f-name">{t['f_name']}</label><input id="f-name" name="name" type="text" autocomplete="name" required></div>
<div class="field"><label for="f-phone">{t['f_phone']}</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" dir="ltr" required></div>
</div>
{email}
<div class="field"><label for="f-message">{t['f_message']}</label><textarea id="f-message" name="message"></textarea></div>
<button class="btn btn-primary" type="submit">{t['f_send']}</button>
</form>'''


def map_embed(c):
    return (f'<div class="map"><iframe src="{MAP_SRC}&hl={c.lang}" title="{escape(c.t["address"])}" loading="lazy" '
            f'referrerpolicy="no-referrer-when-downgrade"></iframe></div>')


# ---------------------------------------------------------------- layout
def nav(c):
    t = c.t

    def link(key, label=None):
        cur = ' aria-current="page"' if c.key == key else ''
        return f'<a href="{c.url(key)}"{cur}>{escape(label or c.title(key))}</a>'

    def group(label, keys, children=None):
        children = children or {}
        members = list(keys) + [k for p in keys for k in children.get(p, [])]
        active = ' is-active' if c.key in members else ''
        items = ''
        for k in keys:
            sub = ''
            if k in children:
                sub = '<ul>' + ''.join(f'<li>{link(x)}</li>' for x in children[k]) + '</ul>'
            items += f'<li>{link(k)}{sub}</li>'
        return (f'<li><button type="button" class="nav-parent{active}" aria-expanded="false">{label}{icon("chevron")}'
                f'</button><ul class="subnav">{items}</ul></li>')

    return f'''<nav class="nav" id="nav" aria-label="{t['nav_label']}"><ul>
<li>{link('home', t['home'])}</li>
{group(t['nav_precast'], PRECAST, {'portable': PORTABLE_CHILDREN})}
<li>{link('light')}</li>
<li>{link('projects')}</li>
{group(t['nav_about'], ['about', 'certs', 'quality'])}
<li>{link('contact')}</li>
{designs_menu(c)}
</ul></nav>'''


def designs_menu(c):
    """Temporary menu for previewing alternative layouts (layouts.css) and colour schemes (themes.css)."""
    t = c.t
    idx = 1 + LANGS.index(c.lang)
    layouts = ''.join(
        f'<li><a href="?layout={d[0]}" data-set="layout" data-value="{d[0]}">{d[idx]}</a></li>' for d in LAYOUTS)
    colors = ''.join(
        f'<li><a href="?design={d[0]}" data-set="design" data-value="{d[0]}">'
        f'<span class="swatch" style="--a:{d[3]};--b:{d[4]}"></span>{d[idx]}</a></li>' for d in DESIGNS)
    return (f'<li><button type="button" class="nav-parent" aria-expanded="false">{t["nav_designs"]}{icon("chevron")}</button>'
            f'<div class="subnav designs">'
            f'<div><span class="designs-title">{t["designs_layout"]}</span><ul>{layouts}</ul></div>'
            f'<div><span class="designs-title">{t["designs_colors"]}</span><ul>{colors}</ul></div>'
            f'</div></li>')


# Applies the chosen layout and colour scheme before the page paints (from the URL or the last choice).
DESIGN_SCRIPT = ("<script>(function(){try{var h=document.documentElement,k=['design','layout'],i,m,v;"
                 "for(i=0;i<2;i++){m=location.search.match(new RegExp('[?&]'+k[i]+'=([a-z]+)'));"
                 "v=m?m[1]:localStorage.getItem(k[i]);if(m)localStorage.setItem(k[i],v);"
                 "if(v&&v!=='classic'&&v!=='standard')h.setAttribute('data-'+k[i],v)}}catch(e){}})();</script>")


def layout(c, description, main, cta=True):
    t = c.t
    other = 'en' if c.lang == 'he' else 'he'
    title = c.title(c.key)
    full_title = f'{title} – Rayforms' if title else f'Rayforms – {t["company"]}'
    cta_html = f'''<section class="cta"><div class="wrap">
<div><h2>{t['cta_title']}</h2><p>{t['cta_text']}</p></div>
<div class="actions"><a class="btn btn-primary" href="{c.url('contact')}">{t['contact']}</a>
<a class="btn btn-ghost" href="{TEL_OFFICE}">{icon('phone')}<span class="ltr">{t['phone_office']}</span></a></div>
</div></section>''' if cta and 'class="aside"' not in main else ''
    precast = ''.join(f'<li><a href="{c.url(k)}">{escape(c.title(k))}</a></li>' for k in PRECAST + ['light'])
    company = ''.join(f'<li><a href="{c.url(k)}">{escape(l)}</a></li>' for k, l in [
        ('about', t['about_short']), ('projects', c.title('projects')), ('certs', c.title('certs')),
        ('quality', c.title('quality')), ('contact', t['contact'])])
    alternates = ''.join(f'<link rel="alternate" hreflang="{l}" href="{c.url(c.key, l)}">\n' for l in LANGS)
    return f'''<!doctype html>
<html lang="{c.lang}" dir="{t['dir']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(full_title)}</title>
<meta name="description" content="{escape(description)}">
<meta name="theme-color" content="#111820">
<meta property="og:title" content="{escape(full_title)}">
<meta property="og:description" content="{escape(description)}">
<meta property="og:type" content="website">
<meta property="og:locale" content="{t['locale']}">
{alternates}<link rel="icon" href="{c.asset('img/favicon.svg')}" type="image/svg+xml">
<link rel="preload" href="{c.asset('fonts/heebo-' + ('hebrew' if c.lang == 'he' else 'latin') + '.woff2')}" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{c.asset('css/style.css')}">
<link rel="stylesheet" href="{c.asset('css/themes.css')}">
<link rel="stylesheet" href="{c.asset('css/layouts.css')}">
{DESIGN_SCRIPT}
</head>
<body>
<a class="skip" href="#content">{t['skip']}</a>
<header class="site-header"><div class="wrap">
<a class="brand" href="{c.url('home')}"><span class="logo" role="img" aria-label="{t['brand']}"></span></a>
{nav(c)}
<div class="header-actions">
<a class="lang-switch" href="{c.url(c.key, other)}" lang="{other}" hreflang="{other}" aria-label="{t['other_name']}" title="{t['other_name']}">{t['other_label']}</a>
<a class="btn btn-primary header-phone" href="{TEL_OFFICE}" aria-label="{t['call']} {t['phone_office']}">{icon('phone')}<span>{t['phone_office']}</span></a>
<button type="button" class="menu-toggle" aria-controls="nav" aria-expanded="false" aria-label="{t['menu']}">{icon('menu')}</button>
</div>
</div></header>
<main id="content">
{main}
</main>
{cta_html}
<footer class="site-footer"><div class="wrap">
<div class="footer-grid">
<div><span class="logo" role="img" aria-label="{t['brand']}"></span>
<p>{escape(t['company'])}<br>{t['footer_tagline']}</p></div>
<div><h2>{t['footer_activity']}</h2><ul>{precast}</ul></div>
<div><h2>{t['footer_company']}</h2><ul>{company}</ul></div>
<div><h2>{t['contact']}</h2><ul>
<li>{t['office']}: <a class="ltr" href="{TEL_OFFICE}">{t['phone_office']}</a></li>
<li>{t['sales']}: <a class="ltr" href="{TEL_SALES}">{t['phone_sales']}</a></li>
<li><a class="ltr" href="mailto:{EMAIL}">{EMAIL}</a></li>
<li>{t['address']}</li>
</ul></div>
</div>
<div class="footer-bottom">{t['rights']}</div>
</div></footer>
<script src="{c.asset('js/main.js')}" defer></script>
</body>
</html>
'''


def page_head(c, crumbs=(), lead=''):
    title = c.title(c.key)
    items = f'<li><a href="{c.url("home")}">{c.t["home"]}</a></li>'
    for crumb in crumbs:
        if crumb == 'precast':  # a menu group, not a page
            items += f'<li>{c.t["nav_precast"]}</li>'
        else:
            label = c.t['nav_about'] if crumb == 'about' else c.title(crumb)
            items += f'<li><a href="{c.url(crumb)}">{escape(label)}</a></li>'
    items += f'<li aria-current="page">{escape(title)}</li>'
    lead_html = f'<p class="lead">{lead}</p>' if lead else ''
    return (f'<section class="page-head"><div class="wrap"><nav aria-label="{c.t["crumbs_label"]}"><ol class="crumbs">{items}</ol></nav>'
            f'<h1>{escape(title)}</h1>{lead_html}</div></section>')


def inner(c, crumbs, body, lead='', with_aside=True):
    content = f'<div class="layout"><div>{body}</div>{aside(c)}</div>' if with_aside else body
    return page_head(c, crumbs, lead) + f'<section class="section"><div class="wrap">{content}</div></section>'


# ---------------------------------------------------------------- page renderers
def home(c):
    t = c.t
    tiles = [
        ('transformer', 'transformer-rooms.webp'), ('protected', 'protected-2.webp'),
        ('light', 'light-construction.webp'), ('postal', 'postal.webp'),
        ('police', 'police-transit.webp'), ('projects', 'project-taibe.webp'),
    ]
    name_idx = 1 + LANGS.index(c.lang)
    clients = ''.join(
        f'<li><img src="{c.asset("img/clients/" + row[0] + ".webp")}" alt="{escape(row[name_idx])}" loading="lazy" decoding="async"></li>'
        for row in CLIENTS)
    creds = ''.join(f'<li><strong>{a}</strong><span>{b}</span></li>' for a, b in t['creds'])
    points = ''.join(f'<li>{p}</li>' for p in t['about_points'])
    return f'''<section class="hero">
<video class="hero-media" data-src="{c.asset('video/hero.mp4')}" poster="{c.asset('img/hero-poster.jpg')}" muted loop playsinline preload="none" aria-hidden="true" tabindex="-1"></video>
<div class="wrap"><div class="hero-inner">
<span class="eyebrow">{t['hero_eyebrow']}</span>
<h1>{t['hero_title']}</h1>
<p>{t['hero_text']}</p>
<div class="actions"><a class="btn btn-primary" href="#activity">{t['hero_btn']}</a><a class="btn btn-ghost" href="{c.url('contact')}">{t['contact']}</a></div>
</div></div>
</section>

<section class="creds" aria-label="{t['creds_label']}"><div class="wrap"><ul>{creds}</ul></div></section>

<section class="section" id="activity"><div class="wrap">
<div class="section-head"><div><span class="eyebrow">{t['act_eyebrow']}</span><h2>{t['act_title']}</h2></div></div>
<div class="grid">{''.join(card(c, k, img) for k, img in tiles)}</div>
</div></section>

<section class="section section-alt"><div class="wrap split">
<div>
<span class="eyebrow">{t['about_eyebrow']}</span>
<h2>{t['about_title']}</h2>
<p>{escape(t['about_text'])}</p>
<ul class="checks">{points}</ul>
<a class="link-arrow" href="{c.url('about')}">{t['about_more']} {icon('arrow')}</a>
</div>
<div class="split-media"><img src="{c.asset('img/postal.webp')}" alt="{t['about_img_alt']}" width="1140" height="700" loading="lazy" decoding="async"></div>
</div></section>

<section class="section"><div class="wrap">
<div class="section-head"><div><span class="eyebrow">{t['prj_eyebrow']}</span><h2>{t['prj_title']}</h2></div>
<a class="link-arrow" href="{c.url('projects')}">{t['prj_all']} {icon('arrow')}</a></div>
<div class="grid">{''.join(card(c, k, img) for k, img in PROJECTS)}</div>
</div></section>

<section class="section section-alt"><div class="wrap">
<div class="section-head"><div><span class="eyebrow">{t['clients_eyebrow']}</span><h2>{t['clients_title']}</h2></div></div>
<ul class="clients">{clients}</ul>
</div></section>

<section class="section"><div class="wrap">
<div class="iso"><img src="{c.asset('img/iso-9001-2015.svg')}" alt="ISO 9001:2015" width="150" height="108" loading="lazy">
<div><h2>{t['iso_title']}</h2><p><a class="link-arrow" href="{c.url('certs')}">{c.title('certs')} {icon('arrow')}</a></p></div></div>
</div></section>

<section class="section section-alt" id="contact"><div class="wrap">
<div class="contact"><div><span class="eyebrow">{t['contact']}</span><h2>{t['contact_title']}</h2>{contact_list(c)}</div>{contact_form(c, False)}</div>
{map_embed(c)}
</div></section>'''


def simple(crumbs, lead_key=None, images=(), alts_key=None, related=None, related_key=None):
    """A page with an optional lead sentence, photos and links to sibling pages."""
    def render(c):
        t = c.t
        body = ''
        if images:
            alts = t[alts_key] if alts_key else [c.title(c.key)] * len(images)
            body += gallery(c, list(zip(images, alts)), ' flush')
        if not lead_key and not images:
            body += f'<div class="prose"><p>{escape(t["empty"].format(c.title(c.key)))}</p></div>'
        if related:
            body += pills(c, [k for k in related if k != c.key], t[related_key])
        return inner(c, crumbs, body, escape(t[lead_key]) if lead_key else '')
    return render


def portable(c):
    imgs = {'ports': 'ports-authority.webp', 'postal': 'postal.webp', 'mekorot': 'mekorot-buildings.webp', 'police': 'police-transit.webp'}
    body = f'<div class="grid grid-2">{"".join(card(c, k, imgs[k]) for k in PORTABLE_CHILDREN)}</div>'
    body += pills(c, [k for k in PRECAST if k != 'portable'], c.t['more_precast'])
    return inner(c, ['precast'], body, escape(c.t['d_portable']))


def projects(c):
    body = PROJECT_TEXT[c.lang] + f'<div class="grid" style="margin-top:40px">{"".join(card(c, k, img) for k, img in PROJECTS)}</div>'
    return inner(c, [], body, with_aside=False)


def project(image):
    def render(c):
        body = PROJECT_TEXT[c.lang] + gallery(c, [(image, c.title(c.key))])
        body += pills(c, [k for k, _ in PROJECTS if k != c.key], c.t['more_projects'])
        return inner(c, ['projects'], body)
    return render


def certs(c):
    files = ['iso-9001.webp', 'contractor-license.webp', 'standard-1923.webp']
    figs = ''.join(
        f'<figure><a href="{c.asset("img/certs/" + f)}" data-lightbox><img src="{c.asset("img/certs/" + f)}" alt="{name}" '
        f'loading="lazy" decoding="async"></a><figcaption>{name}</figcaption></figure>' for f, name in zip(files, c.t['certs']))
    return inner(c, ['about'], f'<div class="gallery certs">{figs}</div>', with_aside=False)


def about(c):
    return inner(c, [], ABOUT_TEXT[c.lang] + pills(c, ['certs', 'quality', 'projects'], c.t['more_company']))


def quality(c):
    return inner(c, ['about'], QUALITY_TEXT[c.lang] + pills(c, ['certs', 'about'], c.t['more_company']))


def contact(c):
    t = c.t
    main = page_head(c, [], t['cta_text'])
    main += (f'<section class="section"><div class="wrap"><div class="contact"><div><h2>{t["contact_details"]}</h2>'
             f'{contact_list(c)}</div>{contact_form(c, True)}</div>{map_embed(c)}</div></section>')
    return main


PORTABLE_CRUMBS = ['precast', 'portable']

# key: (description text key, renderer, show call-to-action band)
PAGES = {
    'home': ('d_default', home, False),
    'transformer': ('d_transformer', simple(['precast'], 'd_transformer', ['transformer-rooms.webp'], None, PRECAST, 'more_precast'), True),
    'protected': ('d_protected', simple(['precast'], 'd_protected', ['protected-1.webp', 'protected-2.webp', 'ports-authority.webp'],
                                        'alt_protected', PRECAST, 'more_precast'), True),
    'portable': ('d_portable', portable, True),
    'ports': ('d_ports', simple(PORTABLE_CRUMBS, 'd_ports', ['ports-authority.webp'], None, PORTABLE_CHILDREN, 'more_portable'), True),
    'postal': ('d_default', simple(PORTABLE_CRUMBS, None, ['postal.webp'], None, PORTABLE_CHILDREN, 'more_portable'), True),
    'mekorot': ('d_default', simple(PORTABLE_CRUMBS, None, ['mekorot-buildings.webp'], None, PORTABLE_CHILDREN, 'more_portable'), True),
    'police': ('d_default', simple(PORTABLE_CRUMBS, None, ['police-transit.webp'], None, PORTABLE_CHILDREN, 'more_portable'), True),
    'armory': ('d_default', simple(['precast'], related=PRECAST, related_key='more_precast'), True),
    'guard': ('d_default', simple(['precast'], related=PRECAST, related_key='more_precast'), True),
    'light': ('d_default', simple([], None, ['light-construction.webp']), True),
    'projects': ('d_projects', projects, True),
    'about': ('d_default', about, True),
    'certs': ('d_certs', certs, True),
    'quality': ('d_quality', quality, True),
    'contact': ('d_default', contact, False),
    'prj_tzur': ('d_projects', project('project-tzur-baher.webp'), True),
    'prj_taibe': ('d_projects', project('project-taibe.webp'), True),
    'prj_camp': ('d_projects', project('project-camp.webp'), True),
}


def main():
    assert set(PAGES) == set(PAGE_INFO)
    count = 0
    for lang in LANGS:
        for key, (desc_key, render, cta) in PAGES.items():
            c = Ctx(lang, key)
            html = layout(c, c.t[desc_key], render(c), cta)
            out = os.path.join(ROOT, c.path, 'index.html')
            os.makedirs(os.path.dirname(out), exist_ok=True)
            with open(out, 'w', encoding='utf-8') as f:
                f.write(html)
            count += 1
    print(f'built {count} pages')


if __name__ == '__main__':
    main()
