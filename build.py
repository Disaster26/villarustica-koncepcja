import os
from PIL import Image
d=os.path.dirname(os.path.abspath(__file__))
r=lambda f:open(os.path.join(d,f),encoding='utf-8').read()
A=['Sypialnia z kratką i drewnianą belką','Sypialnia z jeleniem na poduszkach','Część dzienna z sofą i stołem','Salon z aneksem w apartamencie','Pokój z telewizorem i komodą','Aneks kuchenny z kaflami','Kącik przy stole z kwiatami','Łazienka z kabiną prysznicową','Aneks i szafa w stylu rustykalnym','Klatka schodowa z cegłą','Sypialnia w kratkę','Sypialnia z drewnianym łóżkiem','Ręczniki w łazience']
O=['Zielone grzbiety Bieszczad','Kamienisty szlak grzbietem','Szlak na połoninę','Zapora w Solinie','Jezioro wśród lasów','Kwitnąca wierzbówka na zboczach','Kładka w lesie przy szlaku','Jezioro Solińskie','Bieszczadzkie doliny','Widok z połoniny']
def kadry(pref,opis):
    out=[]
    for i,a in enumerate(opis,1):
        n=f'{pref}{i}'
        w,h=Image.open(os.path.join(d,'img',n+'-full.webp')).size
        lazy='' if (pref=='a' and i<=2) else ' loading="lazy"'
        out.append(f'      <button class="kad" type="button" data-lb="img/{n}-full.webp"><img src="img/{n}-600.webp" srcset="img/{n}-600.webp 600w, img/{n}-900.webp 900w" sizes="(min-width:1700px) 25vw, (min-width:1280px) 33vw, (min-width:900px) 42vw, (min-width:600px) 66vw, 84vw" width="900" height="675" alt="{a}"{lazy} decoding="async"></button>')
    return '\n'.join(out)
s=r('src.html').replace('{{BADGE_STYLE}}',r('badge_style.part').replace('<style>','').replace('</style>','').strip()).replace('{{BADGE_LINK}}',r('badge_link.part').strip()).replace('{{LOGO}}',r('logo.part')).replace('{{KADRY_A}}',kadry('a',A)).replace('{{KADRY_O}}',kadry('o',O))
assert '{{' not in s
open(os.path.join(d,'index.html'),'w',encoding='utf-8').write(s)
