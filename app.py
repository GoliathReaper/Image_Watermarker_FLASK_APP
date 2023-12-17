from flask import Flask, render_template, redirect, url_for, request, flash
from main import image_watermarker
# from flask_bootstrap import Bootstrap5
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'


@app.route("/", methods=['POST', 'GET'])
def home():
    return render_template("index.html")


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    img_location = f'uploads/' + file.filename
    file.save(img_location)
    copyright_text = request.form.get('fname')
    text_opacity = int(request.form.get('opacity'))
    image_watermarker(copyright_text, img_location, text_opacity)
    return 'File uploaded successfully!'


if __name__ == '__main__':
    app.run(debug=True)