from flask import Blueprint, render_template, request
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from src import decoder
import binascii

views = Blueprint('views', __name__)


class UploadFileForm(FlaskForm):
    file = FileField("File")
    submit = SubmitField("Upload File")

@views.route("/", methods=["POST", "GET"])
def index():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        file_bytes = file.read()
        file.seek(0)
        decoder.decrypt_file(file_bytes)
    return render_template("index.html", form=form)

