import datetime
import json
import os
import requests
import shutil
import tempfile
import xmltodict


DIR = os.path.dirname(os.path.abspath(__file__))
HELIOVIEWER_API_PREFIX = "https://api.helioviewer.org/v2/getJP2Image/?"

HELIOVIEWER_API_PREFIX = "https://api.helioviewer.org/v2/{}/?"
GET_IMAGE_PREFIX = HELIOVIEWER_API_PREFIX.format("getJP2Image")
GET_CLOSEST_IMAGE_PREFIX = HELIOVIEWER_API_PREFIX.format("getClosestImage")
GET_METADATA_PREFIX = HELIOVIEWER_API_PREFIX.format("getJP2Header")


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

    source_id = str(params["source_id"])

    return "date={}&sourceId={}".format(date_string, source_id)


def get_helioview_image(params):
    """
    retrieve raw image data from helioviewer URL

    :params: Query parameters
    """
    url = build_helioview_url(params)
    r = requests.get(GET_IMAGE_PREFIX + url, stream=True)
    if r.status_code == 200:
        r.raw.decode_content = True
        return r.raw


def get_image_id(params):
    """
    retrieve image id from helioviewer URL

    :params: Query parameters
    """
    url = build_helioview_url(params)
    r = requests.get(GET_CLOSEST_IMAGE_PREFIX + url, stream=True)
    if r.status_code == 200:
        return r.json()["id"]


def get_image_metadata(id):
    """
    retrieve image metadata from image ID

    :id: unique ID of jp2 image (retrieved from get_image_id)
    """
    url = GET_METADATA_PREFIX + "id=" + id
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        r.raw.decode_content = True
        return json.dumps(xmltodict.parse(r.text))


def download_file(params):
    """
    Save raw image data as file

    :params: Query parameters
    """
    temp = tempfile.NamedTemporaryFile()
    try:
        raw_data = get_helioview_image(params)
        shutil.copyfileobj(raw_data, temp)
    finally:
        temp.close()
    return temp.name


def remove_file(filename):
    os.remove(filename)


def build_query_dict(year, month, day, hour, minute, second, source_id):
    return {
        "year": year,
        "month": month,
        "day": day,
        "hour": hour,
        "minute": minute,
        "second": second,
        "source_id": source_id,
    }

def make_filename(header_date_time):
    filename = header_date_time.split('T')
    date_parts = filename[0].split('-')
    time_parts = filename[1].split(':')
    date_parts.append('00')
    date_parts.extend(time_parts)
    return '_'.join(date_parts)
