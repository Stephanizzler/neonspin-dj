"""Draws the NeonSpin DJ app icons into site/icons/."""
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import math, os
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"site","icons")
def draw(size,safe):
    S=1024;img=Image.new("RGBA",(S,S),(7,8,11,255));c=S/2;R=S*0.5*safe
    cyan=(34,211,238,255);mag=(255,63,164,255)
    def ring(d,r,w,col):d.ellipse([c-r,c-r,c+r,c+r],outline=col,width=int(w))
    glow=Image.new("RGBA",(S,S),(0,0,0,0));ring(ImageDraw.Draw(glow),R*0.86,R*0.10,cyan)
    img=Image.alpha_composite(img,glow.filter(ImageFilter.GaussianBlur(S*0.03)));d=ImageDraw.Draw(img)
    ring(d,R*0.86,R*0.07,cyan)
    d.ellipse([c-R*0.74,c-R*0.74,c+R*0.74,c+R*0.74],fill=(17,19,24,255))
    for k in range(9):
        r=R*(0.40+k*0.04);ring(d,r,max(2,R*0.006),(42,46,56,255))
    for a0 in(-60,60,180):d.arc([c-R*0.86,c-R*0.86,c+R*0.86,c+R*0.86],a0,a0+28,fill=(255,255,255,235),width=int(R*0.035))
    d.arc([c-R*0.80,c-R*0.80,c+R*0.80,c+R*0.80],200,320,fill=mag,width=int(R*0.05))
    d.ellipse([c-R*0.34,c-R*0.34,c+R*0.34,c+R*0.34],fill=mag)
    f=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",int(R*0.30))
    w=d.textlength("DJ",font=f);d.text((c-w/2,c-R*0.19),"DJ",font=f,fill=(7,8,11,255))
    a=math.radians(-35);d.line([c+math.cos(a)*R*0.38,c+math.sin(a)*R*0.38,c+math.cos(a)*R*0.72,c+math.sin(a)*R*0.72],fill=(255,255,255,255),width=int(R*0.03))
    return img.convert("RGB").resize((size,size),Image.LANCZOS)
os.makedirs(OUT,exist_ok=True)
for name,size,safe in[("icon-512",512,0.96),("icon-192",192,0.96),("icon-maskable-512",512,0.74),("apple-touch-icon",180,0.86),("favicon",64,0.96)]:
    draw(size,safe).save(os.path.join(OUT,name+".png"))
print("icons written to",OUT)
