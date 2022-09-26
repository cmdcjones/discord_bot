import requests
import re

CHANNEL_REQUEST_URL = 'https://www.youtube.com/user/videogamedunkey/videos'

def get_newest_video():
  html = requests.get(CHANNEL_REQUEST_URL).text
  url = "https://www.youtube.com/watch?v=" + re.search('(?<="videoId":").*?(?=")', html).group()
  return url