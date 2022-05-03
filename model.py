from flask import Flask, render_template,request
import os
from model.machine_translation import Translation
import logging
IMG_FOLDER = os.path.join('static', 'images')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMG_FOLDER
model_path = './model/translation_model.h5'
model = Translation(model_path)
logging.basicConfig(level=logging.INFO)

@app.route("/",  methods=['POST', 'GET'])
def index():
    params = dict(request.form)
    sentence = params.get('sentence', '')
    tr = Translation('model/translation_model.h5')
    translated_text = tr.final_predictions_model(sentence)

    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'banner.jpg')
    return render_template("home.html", banner_image = full_filename,translated_text = translated_text)
