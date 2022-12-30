import os
import random
from PIL import Image, ImageDraw, ImageFont
import pixabay.core


def create_name(slug):
    k = slug
    if " " in k:
        k = k.replace(" ", "-")
    return k

def create_thumb(name, text):
    api = pixabay.core("31414343-0a8a8b47952dd2e97e7b90a34")
    search = api.query(text)
    raname = random.randint(100000,999999)
    search[0].download(f"templates/{raname}.jpg", "largeImage")

    img = Image.open(f'templates/{raname}.jpg')
    imgname = create_name(name)
    drew = ImageDraw.Draw(img)
    logo = "quotesholy.com/"
   # font = ImageFont.truetype("comicbd.ttf", 30)
    drew.text((10,10), logo, fill=(255,255,255))
    img.thumbnail((640,426))
    img.save(f"thumbnail/{imgname}.jpg")
    return str(imgname)+'.jpg'

def twt(name, text):
    api = pixabay.core("31414343-0a8a8b47952dd2e97e7b90a34")
    search = api.query(text)
    raname = random.randint(100000,999999)
    dn = random.randint(1,10)
    search[dn].download(f"templates/{raname}.jpg", "largeImage")

    img = Image.open(f'templates/{raname}.jpg')
    imgname = create_name(name)
    img.thumbnail((640,426))
    img.save(f"thumbnail/{imgname}.jpg")
    return str(imgname)+'.jpg'