from flask import Flask, render_template, request, redirect, url_for
import datetime
from utils import get_helioview_image, download_file

def get_date_ranges(start_date, end_date):
    # start_date = datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
    # end_date = datetime.strptime(end, "%Y-%m-%d %H:%M:%S")
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
    # resolution = request.args.get("resolution")
    source_id = request.args.get("sourceId")

    print(start_datetime, end_datetime, wavelength)

    for ind, target in enumerate(get_date_ranges(start_datetime, end_datetime)):
        print(target)
        params = {
            "year": target.year,
            "month": target.month,
            "day": target.day,
            "hour": target.hour,
            "minute": target.minute,
            "second": target.second,
            "sourceId": source_id
        }
        raw = get_helioview_image(params)
        download_file(str(ind), raw)

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()