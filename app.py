from style import *
import os

from werkzeug.utils import secure_filename
from flask import Flask, request, render_template, url_for, flash

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
# Make sure you set this!
app.config['UPLOAD_PATH'] = os.environ.get('UPLOAD_PATH')
app.secret_key = 'super secret key'

# Websites that really helped: (there were more)
# https://flask.palletsprojects.com/en/2.0.x/patterns/fileuploads/
# https://stackoverflow.com/questions/17541614/use-images-instead-of-radio-buttons
# https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask
# https://www.w3schools.com/howto/howto_js_collapse_sidebar.asp
# https://stackoverflow.com/questions/16351826/link-to-flask-static-files-with-url-for
# https://codepen.io/dcode-software/pen/xxwpLQo
# https://github.com/pytorch/examples/tree/master/fast_neural_style
# https://realpython.com/absolute-vs-relative-python-imports/
# https://www.computerhope.com/issues/ch000317.htm
# https://able.bio/rhett/how-to-set-and-get-environment-variables-in-python--274rgt5#:~:text=To%20set%20and%20get%20environment%20variables%20in%20Python%20you%20can,Get%20environment%20variables%20USER%20%3D%20os.

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # Gets style from form
        style = request.form.get("style")
        if style == "":
            flash("Did not select style")
            return render_template("index.html")
        # Gets model path and loads it
        model = "saved_models/" + style + ".pth"
        model = load_model(model)
        # Gets file
        uploaded_file = request.files['myFile']
        filename = secure_filename(uploaded_file.filename)
        if filename == "":
            flash('Did not select file')
            return render_template("index.html")
        if allowed_file(filename):
            uploadspot = app.config['UPLOAD_PATH'] + "/" + filename
            uploaded_file.save(uploadspot)
            # Needs input and output spots
            inputimagedir = "static/uploads/" + filename
            outputimagedir = "static/output/" + style + "-" + filename
            # Stylizes Image
            stylize(model, inputimagedir, outputimagedir)

            imgloc = url_for('static', filename='output/' + style + "-" + filename)
            return render_template("output.html", style=style, imgloc=imgloc)
    return render_template("index.html")
