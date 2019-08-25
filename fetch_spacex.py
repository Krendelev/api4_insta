import os
import requests
from utils import get_image_extension, get_image, save_image


def get_image_urls(launch):
    url = f"https://api.spacexdata.com/v3/launches/{launch}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["links"]["flickr_images"]


def get_pictures(dir_name, launch):
    urls = get_image_urls(launch)
    for number, url in enumerate(urls, start=1):
        picture_name = f"spacex{number}.{get_image_extension(url)}"
        file_path = os.path.join(dir_name, picture_name)
        save_image(get_image(url), file_path)


if __name__ == "__main__":
    dir_name = "images"
    launch = "latest"
    try:
        os.mkdir(dir_name)
    except FileExistsError:
        pass

    get_pictures(dir_name, launch)
