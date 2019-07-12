#!/usr/bin/python
# coding=utf-8

import pytesseract
from PIL import Image

image = Image.open('/Users/zq1/Downloads/string2.png')

vcode = pytesseract.image_to_string(image)

print (vcode)