import os
from flask import Flask, jsonify

import tensorflow as tf
from tensorflow import keras
from keras.applications import xception
from keras.preprocessing import image


app = Flask(__name__)

model = keras.models.load_model("trained_recycled_model_h5.h5")


@app.route("/")
def get_health():
    
    info = dict(
        status='OK',
        model=model.layers[0].input_shape
    )

    return jsonify(info)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)

