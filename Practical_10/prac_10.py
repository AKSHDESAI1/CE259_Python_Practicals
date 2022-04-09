# Aim: Generate PDF file of your 3rd Semester Mark-sheet.

# Name: Aksh k Desai
# Id: 20CE020
# Github Repository Link: https://github.com/AKSHDESAI1/CE259_Python_Practicals.git

from PIL import Image

# Path for your image where it is
image_1 = Image.open(
    r'C:\Geeky Shows\cwh_regex\js\marksheet.png')

# Converting it into pdf
im_1 = image_1.convert('RGB')

# Path where your PDF file will bw saved
im_1.save(r'C:\Geeky Shows\cwh_regex\js\marksheet.pdf')
# im_1.save(r'F:\Sem 4\CE259-PIP\PIP_Practical 10\PIP_Practical 10.pdf')
