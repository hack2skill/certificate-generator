# Importing the PIL library
#refered from gfg
import os
from xmlrpc.client import Boolean
from PIL import Image, ImageDraw, ImageFont
from certificate import config

def generate(path, name, certificate_id):


# def generate(path, list_of_names, list_of_cert_number, edited_path) -> Boolean :
#     n = len(list_of_names)
    
#     for i in range(n):
#         # Open an Image
#         name = list_of_names[i]
#         certificate_number = list_of_cert_number[i]
      img = Image.open(path)
        
#         # Call draw Method to add 2D graphics in an image
      I1 = ImageDraw.Draw(img)
        
#         # Custom font style and font size
      myFont = ImageFont.truetype('arial.ttf', 75)
#         print(myFont)
        # Add Text to an image
      I1.text((700, 800), name, font=myFont, fill =(255, 255, 255))
      I1.text((1000, 1200), certificate_id, font=myFont, fill =(255, 255, 255))
#         # I1.text((100, 120), "Nice kitty", fill =(255, 0, 0))
        
#         # Display edited image
      img.show()
      return img
#         # Save the edited image
#         #img.save(f'{edited_path}/{name}-edited-image.png')
#     return True
    