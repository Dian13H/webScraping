from bs4 import BeautifulSoup
import requests

url = "http://127.0.0.1:8000/victima.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

tags = soup.find_all("a")

for tag in tags:
    if tag.has_attr("href") and tag['href'].startswith('mailto:'):
        email = tag['href'][7:]
        print(email)

