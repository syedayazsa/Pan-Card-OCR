import cv2
import numpy as np
import requests
import io
import json
import pandas as pd
from io import StringIO


print("--------------------------")

print("\n Entracting Info from local Image\n\n")
print("Enter the jpg file name: ")

fname = input()



def str_to_text(strng):
    text_file = open("temp.txt", "w")
    text_file.write(strng)
    text_file.close()


img = cv2.imread(fname)
height, width, _ = img.shape
roi = img

# Ocr
url_api = "https://api.ocr.space/parse/image"
_, compressedimage = cv2.imencode(".jpg", roi, [1, 90])
file_bytes = io.BytesIO(compressedimage)

result = requests.post(url_api,
              files = {"screenshot.jpg": file_bytes},
              data = {"apikey": "76a3497f1188957",
                      "language": "eng"})

result = result.content.decode()
result = json.loads(result)

parsed_results = result.get("ParsedResults")[0]
text_detected = parsed_results.get("ParsedText")


str_to_text(text_detected)

print("--------------------------\n\n")
print("READ INFO FROM PAN CARD")
print("--------------------------\n\n")

import textformatting
