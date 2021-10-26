import os
from io import BytesIO
import base64
from flask import Flask, jsonify, request

import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.applications import xception
from keras.preprocessing import image

import time


IMAGE_WIDTH = 320    
IMAGE_HEIGHT = 320
LABELS = {
    "battery": 0,
    "biological": 1,
    "brown-glass": 2,
    "cardboard": 3,
    "clothes": 4,
    "green-glass": 5,
    "metal": 6,
    "paper": 7,
    "plastic": 8,
    "shoes": 9,
    "trash": 10,
    "white-glass": 11
}
LABELS_INV = {v: k for k, v in LABELS.items()}

app = Flask(__name__)

model = keras.models.load_model("trained_recycled_model_h5.h5")


def remove_file(file):
    if os.path.exists(file):
        os.remove(file)


@app.route("/")
def get_health():
    testfile = '/tmp/test_file'
    info = dict()
    try:
        info = dict(input_shape=model.layers[0].input_shape)
    except:
        status = 'Bad (1)'
    else:
        status = 'Ok'
    
    try:
        with open(testfile, 'w') as f:
            f.write('this is a test')
    except:
        status = 'Bad (2)'
    else:
        status = 'Ok'
        remove_file(testfile)

    info = dict(
        status=status,
        info=info
    )

    return jsonify(info)


@app.route('/predict/', methods=['POST'])
def detect_material():
    filepath = '/tmp/' + str(int(time.time()))
    print(filepath)
    with open(filepath, 'wb') as f:
        f.write(base64.b64decode(request.form['b64'])) 

    # BytesIO(base64.b64decode(request.form['b64']))
    img = image.img_to_array(
        image.load_img(filepath, target_size=(IMAGE_WIDTH, IMAGE_WIDTH))
    ) / 255.
    img = np.expand_dims(img, axis=0)

    preds = model.predict(img)
    preds = preds.argmax(1)
    preds = [LABELS_INV[item] for item in preds]

    remove_file(filepath)

    return jsonify(preds)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)

