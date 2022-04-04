from PIL import Image
from PIL import ImageFilter
from PIL import ImageFont
from PIL import ImageDraw

# Text font import 
textfont = ImageFont.truetype('arial.ttf', size=85)

# Read image and convert to RGB
image=Image.open("petra_Qaisieh.jpg").convert('L')

# Blur Image and then convert to 'L' mode
blurred_img = image.filter(ImageFilter.BoxBlur(radius=11))
print(blurred_img.mode)

# Create Frame to Contain Image and Text 
canvas = Image.new(blurred_img.mode, (image.width, image.height + 300))
canvas.paste(blurred_img, (0,0))

# Caption (Text) Details
photo_author = 'Ahmad Qaisieh'
platform = "Unsplash"
transmethod = 'BoxBlur'
location = "Petra"
country = 'Jordan'
caption = """Location: {},{}. 
PIL filter: {}.
Credits/Attribution: Photo by {} on {}.""".format(location, country, transmethod,photo_author, platform)


# Draw Text on to Canvas 
drawing_object=ImageDraw.Draw(canvas)
drawing_object.text((30,image.height + 10), spacing= 3, fill='white', text=caption, font=textfont)

canvas.show()





