import datetime
import os
import requests
import shutil

DIR = os.path.dirname(os.path.abspath(__file__))
HELIOVIEWER_API_PREFIX = "https://api.helioviewer.org/v2/getJP2Image/?"


def build_helioview_url(params):
    """
    Take dictionary of URL params to turn into proper format
    
    :params: dictionary with the fields year, month, day, hour, minute, second, sourceId
    """
    date_string = (
        datetime.datetime(
            int(params["year"]),
            int(params["month"]),
            int(params["day"]),
            int(params["hour"]),
            int(params["minute"]),
            int(params["second"]),
        ).isoformat()
        + "Z"
    )  # Z added to indicate "Zulu" (UTC) timezone

    source_id = str(params["sourceId"])

    return "date={}&sourceId={}".format(date_string, source_id)


def get_helioview_image(params):
    """
    retrieve raw image data from helioviewer URL

    :params: Query parameters
    """
    url = build_helioview_url(params)
    r = requests.get(HELIOVIEWER_API_PREFIX + url, stream=True)
    if r.status_code == 200:
        r.raw.decode_content = True
        return r.raw


def download_file(filename, data):
    """
    Save raw image data as file

    :filename: name to save file data as (excluding file extension)
    :data: raw image data to save
    """
    with open(os.path.join(DIR, filename + ".jp2"), "wb") as f:
        shutil.copyfileobj(data, f)
