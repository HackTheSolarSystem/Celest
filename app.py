from flask import Flask, render_template, request, redirect, url_for
import datetime
from utils import get_helioview_image, download_file, get_image_id, get_image_metadata, make_filename
import json


def get_date_ranges(start_date, end_date):
    step = datetime.timedelta(minutes=15)

    target_times = []

    while start_date <= end_date:
        target_times.append(start_date)
        start_date += step
    return target_times

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sun")
def sun():
    start_datetime = datetime.datetime.strptime(f"{request.args.get('start_date')} {request.args.get('start_time')}", "%Y-%m-%d %H:%M:%S")
    end_datetime = datetime.datetime.strptime(f"{request.args.get('end_date')} {request.args.get('end_time')}", "%Y-%m-%d %H:%M:%S")
    source_id = request.args.get("sourceId")

    for ind, target in enumerate(get_date_ranges(start_datetime, end_datetime)):
        params = {
            "year": target.year,
            "month": target.month,
            "day": target.day,
            "hour": target.hour,
            "minute": target.minute,
            "second": target.second,
            "source_id": source_id
        }

        image_id = get_image_id(params)
        image_headers = get_image_metadata(image_id)

        raw = get_helioview_image(params)
        img = raw.read()

        filename = make_filename(json.loads(image_headers)['meta']['fits']['DATE'])
        print(filename)
        

        with open(f"{filename}.json", 'w') as file:
            file.write(image_headers)
        with open(f"{filename}.jp2", 'wb') as file:
            file.write(img)

        

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()