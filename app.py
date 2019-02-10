from flask import Flask, render_template, request, redirect, url_for, send_file
import datetime
from utils import get_helioview_image, download_file, get_image_id, get_image_metadata, make_filename, remove_file, make_zip_file
import json
import os

app = Flask(__name__)

@app.route("/")
def index():
    if os.path.exists('sun_data.zip'):
        os.remove('sun_data.zip')
    return render_template("index.html")

@app.route("/sun")
def sun():
    start_datetime = datetime.datetime.strptime(f"{request.args.get('start_date')} {request.args.get('start_time')}", "%Y-%m-%d %H:%M:%S")
    end_datetime = datetime.datetime.strptime(f"{request.args.get('end_date')} {request.args.get('end_time')}", "%Y-%m-%d %H:%M:%S")
    source_id = request.args.get("sourceId")

    make_zip_file(start_datetime, end_datetime, source_id)

    return send_file('sun_data.zip', attachment_filename='sun_data.zip', as_attachment=True)

if __name__ == "__main__":
    app.run()