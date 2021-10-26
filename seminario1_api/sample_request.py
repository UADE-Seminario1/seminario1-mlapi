# importing the requests library
import argparse
import base64

import requests

API_ENDPOINT = "http://localhost:5000/predict/"

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path of the image")
args = vars(ap.parse_args())

image_path = args['image']
b64_image = ""
with open(image_path, "rb") as imageFile:
    b64_image = base64.b64encode(imageFile.read())

data = {'b64': b64_image}

r = requests.post(url=API_ENDPOINT, data=data)

print("{}".format(r.text))
