from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"

page = urlopen(url)
html = page.read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")

print(soup.get_text())

images = soup.find_all("img")

for img in images:
    print(img["src"])

print(soup.title)

print(soup.title.string)

dionysus_img = soup.find_all("img", src="/static/dionysus.jpg")
print(dionysus_img)