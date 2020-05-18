import re
from io import BytesIO
import requests 
from PIL import Image



def get_info(html):
    patt = '''<div\sclass="gt_cut.+?
(?P<url>http:.+?webp).+?
-?(?P<x>\d+)px\s-?(?P<y>\d+)px.+?
</div>'''
    com = re.compile(patt,re.X)
    l = []
    for m in com.finditer(html):
        l.append(m.groupdict())
    return l



def download_img(url):
    return Image.open(BytesIO(requests.get(url).content))


def get_img(img, location_pos):
    new_img = Image.new('RGB',(260,116))
    img_up = []
    img_down = []
    for im_info in location_pos:
        x = int(im_info['x'])
        y = int(im_info['y'])
        cut_img = img.crop((x,y,x+10,y+58))
        if y == 58:
            img_up.append(cut_img)
        else:
            img_down.append(cut_img)
        pos = 0
        for im in img_up:
            new_img.paste(im,(pos,0))
            pos += 10

        pos = 0    
        for im in img_down:
            new_img.paste(im,(pos,58))
            pos += 10
    return new_img

def get_slide_img(html):
    info = get_info(html)
    url = info[0]['url']
    img =download_img(url)
    return get_img(img,info)




def get_distance(img1,img2):
    for x in range(255):
        for y in range(112):
            if is_diff(img1,img2,x,y):
                return x
            
            
def is_diff(img1,img2,x,y):
    pix1 = img1.getpixel((x,y))
    pix2 = img2.getpixel((x,y))
    for i in range(3):
        if abs(pix1[i] - pix2[i])> 50:
            return True
    return False


def distance(html1,html2):
    
    fullbg = get_slide_img(html1)
    bg = get_slide_img(html2)
    return get_distance(fullbg,bg)