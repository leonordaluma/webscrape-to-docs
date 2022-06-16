from pprint import pprint
import requests
from bs4 import BeautifulSoup

res = requests.get(
    "https://www.professormesser.com/free-a-plus-training/220-1001/220-1000-training-course/")
contents = res.text
soup = BeautifulSoup(contents, "html.parser")
video_url = {}

all = soup.select(
    "h1, .entry-content h1, h2, .entry-content h2, h3, .entry-content h3, h4, .entry-content h4, h5, .entry-content h5, h6, .entry-content h6, .site-title, .site-title a",
    limit=220)

for a in all:
    if a.name == "h4":
        links = a.find_all("a")
        for link in links:
            video_url[a.getText()] = f"https://www.professormesser.com{link.get('href')}"

print(video_url)