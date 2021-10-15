from flask import Flask, jsonify
# from flask import (
#     Blueprint, flash, redirect, render_template, request, url_for, jsonify
# )
import tensorflow as tf
from tensorflow import keras
from keras.applications import xception
from keras.preprocessing import image


app = Flask(__name__)

# bp = Blueprint('api', __name__)
#os.path.abspath(os.path.dirname(__name__)) + 

graph = tf.compat.v1.get_default_graph()
with graph.as_default():
    model = keras.models.load_model("trained_recycled_model_h5.h5")



@app.route("/")
def get_health():
    
    info = dict(
        status='OK',
        model=model.summary()
    )

    return jsonify(info)


if __name__ == "__main__":
    app.run(debug=False)
