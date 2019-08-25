import os
import instabot
from dotenv import load_dotenv


def get_image_paths(dir_name):
    return [os.path.join(dir_name, name) for name in os.listdir(dir_name)]


if __name__ == "__main__":
    load_dotenv()
    dir_name = "images"
    image_paths = get_image_paths(dir_name)
    bot = instabot.Bot()
    bot.login(username=os.environ["INSTA_LOGIN"], password=os.environ["INSTA_PASS"])
    for image in image_paths:
        bot.upload_photo(image)
