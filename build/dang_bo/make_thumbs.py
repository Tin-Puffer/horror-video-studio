"""Thumbnails (YouTube 1280x720) + TikTok covers (1080x1920) for "Lá bùa dưới gối ông" P1-P3."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance, ImageOps
B='assets/backgrounds/'; P='assets/characters/props/'; OUT='build/dang_bo/'
RED=(205,22,22)
def font(s): return ImageFont.truetype('C:/Windows/Fonts/seguibl.ttf', s)
def fit(t, s, maxw):
    while font(s).getlength(t) > maxw: s-=4
    return font(s)
def txt(img, xy, t, f, fill=(240,240,240), stroke=7, anchor='la', glow=None, r=16):
    if glow:
        lay=Image.new('RGBA', img.size, (0,0,0,0)); d=ImageDraw.Draw(lay)
        d.text(xy, t, font=f, fill=glow+(255,), anchor=anchor, stroke_width=stroke+8, stroke_fill=glow+(255,))
        img.alpha_composite(lay.filter(ImageFilter.GaussianBlur(r)))
    ImageDraw.Draw(img).text(xy, t, font=f, fill=fill, anchor=anchor, stroke_width=stroke, stroke_fill=(0,0,0))
def prop(img, name, h, xy, angle=0, glow=(255,40,20)):
    p=Image.open(P+name).convert('RGBA'); p=p.resize((int(p.width*h/p.height), h), Image.LANCZOS).rotate(angle, expand=True, resample=Image.BICUBIC)
    g=Image.new('RGBA', p.size, glow+(0,)); g.putalpha(p.split()[3].point(lambda v: 255 if v>20 else 0))
    pad=60; gl=Image.new('RGBA', (p.width+2*pad, p.height+2*pad), (0,0,0,0)); gl.paste(g, (pad,pad), g)
    gl=gl.filter(ImageFilter.GaussianBlur(26))
    for _ in range(2): img.alpha_composite(gl, (xy[0]-pad, xy[1]-pad))
    img.alpha_composite(p, xy)
def base(bg, box, size):
    im=Image.open(B+bg).convert('RGB').crop(box).resize(size, Image.LANCZOS)
    return ImageEnhance.Color(ImageEnhance.Contrast(im).enhance(1.25)).enhance(1.1).convert('RGBA')
def shade(img, side, width, strength=240):
    W,H=img.size; vertical = side in ('top','bottom'); n = H if vertical else W
    g=Image.new('L',(1,n) if vertical else (n,1))
    for i in range(n):
        u = i/n if side in ('left','top') else 1-i/n
        v=int(strength*max(0,1-u/width)**1.2); g.putpixel((0,i) if vertical else (i,0), v)
    sh=Image.new('RGBA',(W,H),(0,0,0,255)); sh.putalpha(g.resize((W,H))); img.alpha_composite(sh)
def vignette(img, s=170):
    W,H=img.size; m=Image.new('L',(W,H),0); ImageDraw.Draw(m).ellipse((-W*0.15,-H*0.25,W*1.15,H*1.25), fill=255)
    m=ImageOps.invert(m.filter(ImageFilter.GaussianBlur(120))).point(lambda v: int(v*s/255))
    sh=Image.new('RGBA',(W,H),(0,0,0,255)); sh.putalpha(m); img.alpha_composite(sh)
def series(img, part, x, y=30, s=30):
    d=ImageDraw.Draw(img); bw=int(s*4.4)
    d.rectangle((x, y, x+bw, y+int(s*1.6)), fill=RED); d.text((x+bw//2, y+int(s*0.8)), f'PHẦN {part}', font=font(int(s*0.93)), fill='white', anchor='mm')
    d.text((x+bw+12, y+int(s*0.8)), 'LÁ BÙA DƯỚI GỐI ÔNG', font=font(s), fill=(235,235,235), anchor='lm', stroke_width=3, stroke_fill=(0,0,0))

PARTS = {
 1: dict(bg='bgL3c_coffin_face_smile.png', yt_box=(0,0,2200,1238), side='left',
         small='3 GIỜ SÁNG', big=('ÔNG MỈM CƯỜI','TRONG QUAN TÀI'), prop=('LB2_talisman_open.png',190,-12,(255,170,30)),
         tt_box=(900,0,1764,1536)),
 2: dict(bg='bgL19_mirror_ong_behind_mom.png', yt_box=(1000,120,2300,851), side='right',
         small='TRONG GƯƠNG', big=('ÔNG ĐỨNG','SAU LƯNG MẸ'), prop=('LF2_bowl_upright_steaming.png',200,0,(255,60,30)), label='Bát cơm thứ hai',
         tt_box=(1150,0,2014,1536)),
 3: dict(bg='bgL55o_ghost_at_ong_grave.png', yt_box=(700,120,2250,992), side='right',
         small='BÁT CƠM THỨ BA', big=('KHẮC TÊN','CỦA TÔI'), prop=('LF3_chopsticks_khoa.png',300,-72,(255,40,20)),
         tt_box=(800,0,1664,1536)),
}
for n, c in PARTS.items():
    # ---- YouTube
    im=base(c['bg'], c['yt_box'], (1280,720)); right = c['side']=='right'
    shade(im, 'right' if right else 'left', 0.55 if right else 0.62); vignette(im)
    x, a = (1245, 'ra') if right else (36, 'la')
    series(im, n, 1280-36-int(font(30).getlength('LÁ BÙA DƯỚI GỐI ÔNG'))-144 if right else 36)
    txt(im, (x, 165), c['small'], fit(c['small'], 74, 560), anchor=a)
    txt(im, (x, 250), c['big'][0], fit(c['big'][0], 116, 580), (255,235,235), 9, a, RED)
    txt(im, (x, 370), c['big'][1], fit(c['big'][1], 116, 580), (255,235,235), 9, a, RED)
    pn, ph, pa, pg = c['prop']
    if n == 1: prop(im, pn, ph, (40, 510), pa, pg)
    if n == 2:
        prop(im, pn, ph, (1105, 505), pa, pg); txt(im, (1085, 655), c['label'], font(44), (230,230,230), 5, 'rm')
    if n == 3: prop(im, pn, ph, (880, 520), pa, pg)
    im.convert('RGB').save(f'{OUT}p{n}_thumbnail_youtube.jpg', quality=93)
    # ---- TikTok cover
    tt=base(c['bg'], c['tt_box'], (1080,1920))
    shade(tt, 'top', 0.38, 245); shade(tt, 'bottom', 0.40, 245)
    series(tt, n, 60, 90, 40)
    txt(tt, (540, 300), c['small'], fit(c['small'], 90, 960), anchor='mm')
    txt(tt, (540, 1560), c['big'][0], fit(c['big'][0], 150, 1000), (255,235,235), 10, 'mm', RED)
    txt(tt, (540, 1730), c['big'][1], fit(c['big'][1], 150, 1000), (255,235,235), 10, 'mm', RED)
    tt.convert('RGB').save(f'{OUT}p{n}_cover_tiktok.jpg', quality=92)
print('ok')
