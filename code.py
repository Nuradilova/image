from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as np
import matplotlib.pyplot as plt

img = Image.open(r"C:\Users\user\Pictures\Camera Roll\dog.jpeg")


bw_image = img.convert('L')
bw_image.show()

cropped = img.crop((0, 0, 1080, 1080))
cropped.show()
img.show()  

  
watermark_image = img.copy()
  
draw = ImageDraw.Draw(watermark_image)
title_font = ImageFont.truetype("arial.ttf", 80)
title_text = "My Dog"
img_editable = ImageDraw.Draw(img)
img_editable.text( (100, 100), title_text, (150, 230, 212), font = title_font )
img.show()


