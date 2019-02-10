import datetime
import json
import os
import requests
import shutil
import tempfile
import xmltodict
import zipfile


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

def make_filename(header_date_time,source_id):
    filename = header_date_time.split('T')
    date_parts = filename[0].split('-')
    time_parts = filename[1].split(':')
    date_parts.append('_00')
    date_parts.extend(time_parts)
    date_parts.append(f'_{source_id})
    return '_'.join(date_parts)

def get_date_ranges(start_date, end_date):
    step = datetime.timedelta(minutes=15)

    target_times = []

    while start_date <= end_date:
        target_times.append(start_date)
        start_date += step
    return target_times

def make_zip_file(start_datetime, end_datetime, source_id):
    with zipfile.ZipFile('sun_data.zip','w', zipfile.ZIP_DEFLATED) as zipf:

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

            filename = make_filename(json.loads(image_headers)['meta']['fits']['DATE'], source_id)

            with open(f"{filename}.json", 'w') as file:
                file.write(image_headers)
            with open(f"{filename}.jp2", 'wb') as file:
                file.write(img)
            
            file_types = ['.json', '.jp2']

            for file_type in file_types:
                zipf.write(f"{filename}{file_type}")
                remove_file(f"{filename}{file_type}")