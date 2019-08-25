import os
import requests
from utils import get_image_extension, get_image, save_image


def get_image_ids(collection):
    url = "http://hubblesite.org/api/v3/images"
    payload = {"pages": "all", "collection_name": collection}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return [record["id"] for record in response.json()]


def get_image_url(image_id):
    url = "http://hubblesite.org/api/v3/image/"
    response = requests.get(f"{url}{image_id}")
    response.raise_for_status()
    records = response.json()["image_files"]
    return f"http:{records[-1]['file_url']}"


def get_pictures(dir_name, collection):
    image_ids = get_image_ids(collection)
    for image_id in image_ids:
        url = get_image_url(image_id)
        picture_name = f"hubble{image_id}.{get_image_extension(url)}"
        file_path = os.path.join(dir_name, picture_name)
        save_image(get_image(url), file_path)


if __name__ == "__main__":
    dir_name = "images"
    collection = "wallpaper"
    try:
        os.mkdir(dir_name)
    except FileExistsError:
        pass

    get_pictures(dir_name, collection)
