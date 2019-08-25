import requests


def get_image_extension(url):
    return url.split(".")[-1]


def get_image(url):
    response = requests.get(url, verify=False)
    response.raise_for_status()
    return response.content


def save_image(image, file_path):
    with open(file_path, "wb") as fh:
        fh.write(image)
