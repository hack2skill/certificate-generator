# Importing the PIL library
#refered from gfg
import os
from xmlrpc.client import Boolean
from PIL import Image, ImageDraw, ImageFont
from certificate import config


# def generate(path, name, certificate_id, variableData):
def generate(user):
      image_path = user['image_path']
      variableData = user['variableData']
      
      # print(type(vData),vData)
      # variableData = json.loads(vData)
      print(type(variableData),variableData)
      path = f"uploads_folder/{image_path}"
# font = 'arial.ttf', font_size = 175, 
#                   name_origin_coordinates =(700, 800),  name_font_color=(0, 0, 0), 
#                   certificate_id_origin_coordinates = (1000, 1200), certificate_id_font_color = (0, 0, 0)):


# def generate(path, list_of_names, list_of_cert_number, edited_path) -> Boolean :
#     n = len(list_of_names)
    
#     for i in range(n):
#         # Open an Image
#         name = list_of_names[i]
#         certificate_number = list_of_cert_number[i]
      img = Image.open(path)

#         # Call draw Method to add 2D graphics in an image
      I1 = ImageDraw.Draw(img)
      # print(I1)
        
#         # Custom font style and font size
      variables = variableData['variables']
      fonts = variableData['fonts']
      colors = variableData['colors']
      sizes = variableData['sizes']
      aligns = variableData['aligns']
      lefts = variableData['lefts']
      tops = variableData['tops']
      for i in range(len(variables)):
            vary = user[variables[i]]
            # print(vary, int(sizes[i].split('p')[0]),f'{fonts[i]}.ttf')
            myFont = ImageFont.truetype('arial.ttf', int(sizes[i].split('p')[0])) #TODO: changing fonts
      #         print(myFont)
            # Add Text to an image
            # color_list = colors[i][1:-1].split(',')
            # print(color_list)
            # color_tuple = []
            # for color in color_list:
            #       col = color.strip()
            #       print(col)
            #       color_tuple.append(int(col))
            # fill_color = tuple(color_tuple)
            # print(fill_color)
            I1.text((int(lefts[i]),int(tops[i])), vary, font=myFont, fill =(0,0,0)) #TODO: changing colors
      # I1.text(certificate_id_origin_coordinates, certificate_id, font=myFont, fill =certificate_id_font_color)
#         # I1.text((100, 120), "Nice kitty", fill =(255, 0, 0))
        
#         # Display edited image
      img.show()
      print(img.info)
      return img
#         # Save the edited image
#         #img.save(f'{edited_path}/{name}-edited-image.png')
#     return True
    