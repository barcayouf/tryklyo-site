# -*- coding: utf-8 -*-
# Builds 4 Instagram carousel slides (1080x1350) for klyo, vintage rodeo-poster style.
import os

BASE = os.path.dirname(os.path.abspath(__file__))

CSS = """
@import url('fonts/fonts-local.css');

* { margin:0; padding:0; box-sizing:border-box; }

:root {
  --bg: #262b3a;
  --ink: #b9d5d9;
  --ink-dim: rgba(185,213,217,.82);
}

html,body { width:1080px; height:1350px; overflow:hidden; }

.slide {
  position:relative;
  width:1080px; height:1350px;
  background:
    radial-gradient(ellipse 120% 90% at 50% 40%, rgba(255,255,255,.045), rgba(0,0,0,.22) 85%),
    var(--bg);
  color:var(--ink);
  direction:rtl;
  font-family:'Heebo',sans-serif;
  overflow:hidden;
}

/* denim grain */
.grain {
  position:absolute; inset:0; pointer-events:none; z-index:50;
  opacity:.5; mix-blend-mode:overlay;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='3' stitchTiles='stitch'/></filter><rect width='300' height='300' filter='url(%23n)' opacity='0.9'/></svg>");
  background-size:300px 300px;
}
.grain2 {
  position:absolute; inset:0; pointer-events:none; z-index:51;
  opacity:.22; mix-blend-mode:soft-light;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='900' height='900'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.012 0.02' numOctaves='4' stitchTiles='stitch'/></filter><rect width='900' height='900' filter='url(%23n)' opacity='1'/></svg>");
  background-size:900px 900px;
}

.slab { font-family:'Suez One',serif; font-weight:400; }

h1,h2,h3 { font-family:'Suez One',serif; font-weight:400; letter-spacing:.01em; }

.ink-soft { text-shadow:0 0 3px rgba(185,213,217,.28); }

.star { display:inline-block; }

/* footer strip shared by slides 2-4 */
.footer {
  position:absolute; bottom:52px; left:0; right:0;
  display:flex; align-items:center; justify-content:center; gap:26px;
  direction:ltr;
}
.footer .stars { letter-spacing:16px; font-size:30px; opacity:.9; }
.footer .brand { font-family:'Suez One',serif; font-size:40px; letter-spacing:.06em; }
.footer .site  { font-family:'Heebo'; font-weight:500; font-size:24px; letter-spacing:.14em; opacity:.85; }
"""

GRAIN = "<div class='grain'></div><div class='grain2'></div>"

# Screen-print style kettlebell-swing figure (side view, facing left)
HERO_SVG = """
<svg width='545' height='493' viewBox='0 0 520 470' xmlns='http://www.w3.org/2000/svg'>
  <defs>
    <filter id='rough' x='-10%' y='-10%' width='120%' height='120%'>
      <feTurbulence type='fractalNoise' baseFrequency='0.055' numOctaves='3' seed='7' result='n'/>
      <feDisplacementMap in='SourceGraphic' in2='n' scale='7'/>
    </filter>
    <filter id='rough2' x='-10%' y='-10%' width='120%' height='120%'>
      <feTurbulence type='fractalNoise' baseFrequency='0.09' numOctaves='2' seed='3' result='n'/>
      <feDisplacementMap in='SourceGraphic' in2='n' scale='5'/>
    </filter>
    <pattern id='halftone' width='9' height='9' patternUnits='userSpaceOnUse' patternTransform='rotate(25)'>
      <circle cx='4.5' cy='4.5' r='1.9' fill='#262b3a'/>
    </pattern>
  </defs>

  <g filter='url(#rough)'>
    <!-- swing path arcs -->
    <g fill='none' stroke='#b9d5d9' stroke-linecap='round' opacity='.85'>
      <path d='M 318 408 Q 128 380 118 235' stroke-width='7' stroke-dasharray='26 20'/>
      <path d='M 345 425 Q 96 398 88 222' stroke-width='5' stroke-dasharray='18 16' opacity='.6'/>
    </g>

    <g fill='#b9d5d9'>
      <!-- rear leg -->
      <path d='M 296 250 L 336 258 L 334 340 L 330 424 L 300 424 L 306 338 Z'/>
      <!-- front leg -->
      <path d='M 268 248 L 306 254 L 296 342 L 286 424 L 256 424 L 250 338 Z'/>
      <!-- rear shoe -->
      <path d='M 298 410 L 334 410 L 342 430 L 292 430 Z'/>
      <!-- front shoe -->
      <path d='M 252 410 L 288 410 L 284 430 L 232 430 L 240 418 Z'/>
      <!-- torso, slight backward lean -->
      <path d='M 278 132 L 330 140 L 336 200 L 330 262 L 268 254 L 272 196 Z'/>
      <!-- head -->
      <circle cx='306' cy='96' r='31'/>
      <!-- cap brim facing left -->
      <path d='M 268 88 L 306 78 L 308 94 L 270 100 Z'/>
      <!-- neck -->
      <path d='M 292 118 L 318 122 L 316 142 L 290 138 Z'/>
      <!-- upper arm pair extended to the left -->
      <path d='M 282 148 L 292 172 L 186 192 L 180 168 Z'/>
      <path d='M 286 160 L 292 182 L 190 202 L 186 182 Z' opacity='.92'/>
      <!-- hands / grip -->
      <path d='M 168 164 L 196 168 L 194 206 L 166 202 Z'/>
      <!-- kettlebell handle -->
      <path d='M 128 176 Q 152 148 178 172 L 170 188 Q 152 172 138 190 Z'/>
      <!-- kettlebell body -->
      <circle cx='138' cy='228' r='47'/>
    </g>

    <!-- halftone shading clipped inside main shapes -->
    <g fill='url(#halftone)' opacity='.32'>
      <path d='M 278 132 L 330 140 L 336 200 L 330 262 L 268 254 L 272 196 Z'/>
      <circle cx='138' cy='228' r='47'/>
      <path d='M 296 250 L 336 258 L 334 340 L 330 424 L 300 424 L 306 338 Z'/>
      <path d='M 268 248 L 306 254 L 296 342 L 286 424 L 256 424 L 250 338 Z'/>
      <circle cx='306' cy='96' r='31'/>
    </g>
  </g>

  <!-- chalk splatter -->
  <g fill='#b9d5d9' filter='url(#rough2)'>
    <circle cx='90' cy='150' r='4'/><circle cx='70' cy='260' r='3'/><circle cx='108' cy='300' r='5'/>
    <circle cx='210' cy='120' r='3'/><circle cx='388' cy='120' r='4'/><circle cx='402' cy='210' r='3'/>
    <circle cx='420' cy='320' r='5'/><circle cx='380' cy='400' r='3'/><circle cx='170' cy='330' r='3'/>
    <circle cx='60' cy='190' r='2.4'/><circle cx='452' cy='170' r='2.6'/><circle cx='196' cy='262' r='2.6'/>
    <circle cx='352' cy='70' r='2.6'/><circle cx='240' cy='60' r='3.4'/><circle cx='140' cy='96' r='2.8'/>
    <circle cx='430' cy='260' r='2.4'/><circle cx='330' cy='448' r='3'/><circle cx='210' cy='440' r='2.6'/>
  </g>

  <!-- ground streaks -->
  <g stroke='#b9d5d9' stroke-linecap='round' filter='url(#rough2)' opacity='.8'>
    <line x1='190' y1='444' x2='400' y2='444' stroke-width='7'/>
    <line x1='150' y1='456' x2='300' y2='456' stroke-width='5' opacity='.6'/>
    <line x1='330' y1='458' x2='430' y2='458' stroke-width='4' opacity='.5'/>
  </g>
</svg>
"""

FOOTER = """
<div class='footer'>
  <span class='stars'>★ ★ ★ ★</span>
  <span class='brand'>klyo</span>
  <span class='site'>TRYKLYO.IO</span>
  <span class='stars'>★ ★ ★ ★</span>
</div>
"""

# ---------------- SLIDE 1 (cover) ----------------
SLIDE1 = f"""
<div class='slide'>
  {GRAIN}

  <!-- arched brand -->
  <svg width='1080' height='260' viewBox='0 0 1080 260' style='position:absolute;top:30px;left:0;'>
    <defs><path id='arc' d='M 110 235 Q 540 80 970 235'/></defs>
    <text fill='#b9d5d9' font-family='Suez One' font-size='92' letter-spacing='5'>
      <textPath href='#arc' startOffset='50%' text-anchor='middle'>★ קליו מציגים ★</textPath>
    </text>
  </svg>

  <div class='slab' style='position:absolute; top:255px; width:100%; text-align:center; font-size:200px; line-height:1; white-space:nowrap;' >
    חוקי הברזל
  </div>

  <!-- quote right (RTL start side) -->
  <div style='position:absolute; top:590px; right:48px; width:290px; transform:rotate(6deg); text-align:center; font-weight:500; font-size:35px; line-height:1.34;'>
    ״שרירים לא נבנים<br>בחדר כושר.<br>הם נבנים<br>במטבח״
  </div>

  <!-- collab left -->
  <div style='position:absolute; top:620px; left:56px; width:240px; text-align:center;'>
    <div style='font-weight:500; font-size:26px; letter-spacing:.12em;'>בשיתוף</div>
    <div class='slab' style='font-size:50px; margin-top:6px;'>klyo</div>
    <div style='font-family:Heebo; font-weight:400; font-size:20px; letter-spacing:.2em; opacity:.85;'>NUTRITION</div>
  </div>

  <!-- illustration -->
  <div style='position:absolute; top:480px; left:50%; transform:translateX(-50%); width:545px; height:493px;'>
    {HERO_SVG}
  </div>

  <div class='slab' style='position:absolute; top:975px; width:100%; text-align:center; font-size:86px;'>
    6 חוקים שבונים
  </div>
  <div class='slab' style='position:absolute; top:1080px; width:100%; text-align:center; font-size:86px;'>
    ★ תוצאות ★
  </div>

  <div style='position:absolute; bottom:38px; left:0; right:0; text-align:center;'>
    <div style='font-weight:500; font-size:32px; letter-spacing:.02em;'>
      חלבון. דלק. תזמון. שינה. מים. מעקב. בלי קיצורי דרך.
    </div>
    <div style='margin-top:16px; font-size:24px; letter-spacing:13px; direction:ltr;'>
      ★ ★ ★ ★ ★ &nbsp; <span style='letter-spacing:.18em; font-size:24px; font-weight:500;'>החליקו&nbsp;להמשך</span> &nbsp; ★ ★ ★ ★ ★
    </div>
  </div>
</div>
"""

# ---------------- tip item template ----------------
def tip(num, title, body, top):
    return f"""
    <div style='position:absolute; top:{top}px; right:70px; left:70px;'>
      <div style='display:flex; align-items:baseline; gap:42px;'>
        <div style='font-family:Heebo; font-weight:400; font-size:56px; opacity:.92; min-width:96px;'>{num}</div>
        <div class='slab' style='font-size:92px; line-height:1;'>{title}</div>
      </div>
      <div style='margin-top:26px; margin-right:138px; font-weight:400; font-size:41px; line-height:1.42; color:var(--ink-dim); max-width:830px;'>{body}</div>
    </div>
    """

SLIDE2 = f"""
<div class='slide'>
  {GRAIN}
  {tip('01', 'חוק החלבון',
       'חלבון זה לא רק שייק אחרי אימון. פזרו אותו על פני היום — 3–4 מנות שוות בונות שריר טוב יותר מכל בומבה אחת בסוף האימון.', 90)}
  {tip('02', 'חוק הדלק',
       'פחמימה לפני אימון היא לא פינוק — היא דלק. בננה או פרוסת לחם 30–60 דקות לפני, ותרגישו את ההבדל בסטים האחרונים.', 500)}
  {tip('03', 'חוק החלון',
       '״החלון האנבולי״ לא נסגר אחרי 30 דקות. מה שקובע זה הסך היומי — אבל ארוחה מסודרת עד שעתיים מהאימון היא מהלך חכם.', 890)}
  {FOOTER}
</div>
"""

SLIDE3 = f"""
<div class='slide'>
  {GRAIN}
  {tip('04', 'חוק השינה',
       'פחות מ־7 שעות שינה פוגע בבניית השריר ומגביר חשק למתוק. שינה היא המכשיר הכי חזק בחדר הכושר — והיא בחינם.', 90)}
  {tip('05', 'חוק המים',
       'ירידה של 2% בנוזלים = ירידה בכוח ובריכוז. בקבוק מים לפני הקפה של הבוקר, ועוד אחד ליד הספסל.', 500)}
  {tip('06', 'חוק המעקב',
       'מה שלא מודדים — לא משתפר. שבוע אחד של מעקב אמיתי אחרי מה שאתם אוכלים שווה יותר מעשר תוכניות תזונה.', 890)}
  {FOOTER}
</div>
"""

# ---------------- SLIDE 4 (conversion, WHEN/WHERE/HOW grid) ----------------
SLIDE4 = f"""
<div class='slide'>
  {GRAIN}

  <div style='position:absolute; top:74px; left:64px; right:64px; bottom:210px; border:3px solid rgba(185,213,217,.85); border-radius:34px;'>

    <div style='position:absolute; top:0; right:0; left:0; height:26%; border-bottom:2px solid rgba(185,213,217,.7); padding:56px 58px;'>
      <div style='display:flex; gap:44px;'>
        <div class='slab' style='font-size:74px; letter-spacing:.04em; flex:0 0 220px;'>מתי:</div>
        <div style='flex:1 1 0; text-align:right; font-weight:400; font-size:47px; line-height:1.38; padding-top:14px;'>היום.<br>לא מיום ראשון הקרוב.</div>
      </div>
    </div>

    <div style='position:absolute; top:26%; right:0; left:0; height:40%; border-bottom:2px solid rgba(185,213,217,.7); padding:56px 58px;'>
      <div style='display:flex; gap:44px;'>
        <div class='slab' style='font-size:74px; letter-spacing:.04em; flex:0 0 220px;'>איפה:</div>
        <div style='flex:1 1 0; text-align:right; font-weight:400; font-size:43px; line-height:1.45; padding-top:16px;'>בכיס שלכם. קליו עושה את המעקב בשבילכם — בלי לשקול אוכל ובלי לנחש קלוריות.</div>
      </div>
    </div>

    <div style='position:absolute; top:66%; right:0; left:0; bottom:0; padding:52px 58px;'>
      <div class='slab' style='font-size:74px; letter-spacing:.04em;'>איך מתחילים:</div>
      <div style='font-weight:400; font-size:47px; line-height:1.38; margin-top:24px;'>ת.ת.ק.<br>(תורידו ת׳קליו — חינם, בלי כרטיס אשראי)</div>
    </div>

  </div>

  <div style='position:absolute; bottom:118px; left:0; right:0; text-align:center; font-weight:500; font-size:31px; letter-spacing:.03em;'>
    שמרו את הפוסט ★ ושתפו עם החבר שגורר אתכם לחדר כושר
  </div>

  {FOOTER.replace("bottom:52px", "bottom:34px")}
</div>
"""

PAGE = """<!doctype html>
<html lang='he'>
<head><meta charset='utf-8'><style>{css}</style></head>
<body>{body}</body>
</html>"""

slides = [SLIDE1, SLIDE2, SLIDE3, SLIDE4]
for i, s in enumerate(slides, 1):
    with open(os.path.join(BASE, f'slide{i}.html'), 'w') as f:
        f.write(PAGE.format(css=CSS, body=s))
print('built', len(slides), 'slides')
