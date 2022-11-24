import random
import cv2
from english_words import english_words_set
import numpy as np 
from PIL import ImageFont, ImageDraw, Image 
import glob
from config import config

image_size, words_qty, img_fraction, percent_variation = config()

def image_process(image_size):
    h, w = image_size
    blank = 255*np.ones((h, w)).astype(np.uint8)
    image_pil = Image.fromarray(blank)
    draw = ImageDraw.Draw(image_pil)
    return blank, image_pil, draw

def fonts_resizer(palavra, img_fraction, w):
    fontsize = 1
    fonts = glob.glob("/TTF/*")
    font = random.choice(fonts)
    font_pil = ImageFont.truetype(font, fontsize)
    while font_pil.getsize(palavra)[0] < img_fraction*w:
        fontsize += 1
        font_pil = ImageFont.truetype(font, fontsize)
    fontsize -= 1
    font_pil = ImageFont.truetype(font, fontsize)
    return font_pil

def dimension(palavra, draw, image_size, font_pil, low_percent, high_percent):
    w, h = image_size
    aw = ah = random.randint(low_percent, high_percent)/100
    textsize = draw.textsize(palavra, font= font_pil)
    textw = int((w - textsize[0])/2)
    texth = int((h - textsize[1])/2)
    rw = int((w*aw) + w)
    rh = int((h*ah) + h)
    x = int(textw + (aw*w))
    y = int(texth + (ah* h))
    dim = (rw, rh)
    coord = (x, y)
    return dim, coord

def text(coord, dim, palavra, font_pil, image_pil, draw, words_qty):
    palavras = (random.sample(english_words_set, words_qty))
    for palavra in palavras:
        draw.text(coord, palavra, font = font_pil, align="center")
        processed = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)
        cv2.resize(processed, dim)
        cv2.imwrite(f'{palavra}.png', processed)
if  __name__ == "__text__":
    text()
