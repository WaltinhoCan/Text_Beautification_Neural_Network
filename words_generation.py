words_qty = 10
fontsize = 1
image_size = 100, 400
img_fraction = 0.3
palavras =  (random.sample(english_words_set, words_qty))
for palavra in palavras:
	palavra = str(palavra)
	h, w = image_size
	low_percent, high_percent = -5, 5
	blank = 255*np.ones((h, w)).astype(np.uint8)
	image_pil = Image.fromarray(blank)
	draw = ImageDraw.Draw(image_pil)
	fonts = glob.glob("/fontes/*")
	font = random.choice(fonts)
	font_pil = ImageFont.truetype(font, fontsize)
	while font_pil.getsize(palavra)[0] < img_fraction*w:
		fontsize += 1
		font_pil = ImageFont.truetype(font, fontsize)
	fontsize -= 1
	font_pil = ImageFont.truetype(font, fontsize)
	textsize = draw.textsize(palavra, font= font_pil)
	textw = int((w - textsize[0])/2)
	texth = int((h - textsize[1])/2)
	aw = ah = random.randint(low_percent, high_percent)/100
	x = int(textw + (aw*w))
	y = int(texth + (ah*h))
	rw = int((w*aw) + w)
	rh = int((h*ah) + h)
	dim = (rw, rh)
	draw.text((x, y), palavra, font = font_pil, align="center")
	processed = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)
	cv2.resize(processed, dim)
	cv2.imwrite(f'{palavra}.png', processed)
