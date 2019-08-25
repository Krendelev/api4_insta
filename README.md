# Space Instagram

Scripts that help you get pictures from [Hubble Space Telescope](https://hubblesite.org) and SpaceX launches and post them to [Instagram](https://instagram.com).

### How to install

Python3 should be already installed.
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Create your [Instagram](https://instagram.com) account and put `login` and `password` into the `.env` file in the working directory like this:

```
INSTA_LOGIN=myaccount
INSTA_PASS=mypassword
```
Run `fetch_hubble.py` and `fetch_spacex.py` to get pictures and `post_pictures.py` to post them.

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
