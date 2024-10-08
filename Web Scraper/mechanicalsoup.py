import time
import mechanicalsoup

browser = mechanicalsoup.Browser()

for i in range(4):
    page = browser.get("http://olympus.realpython.org/dice")
    tag = page.soup.select("#result")[0]
    result = tag.text
    print(f"The result of your dice roll is: {result}")

    if i < 3:
        time.sleep(10)

url = "http://olympus.realpython.org/login"

login_page = browser.get(url)
login_html = login_page.soup

form = login_html.select("form")[0]

form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

profiles_page = browser.submit(form, login_page.url)

links = profiles_page.soup.select("a")

base_url = "http://olympus.realpython.org"

for link in links:
    address = base_url + link["href"]
    text = link.text
    print(f"{text}: {address}")