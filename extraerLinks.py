import requests
from bs4 import BeautifulSoup

url = "http://127.0.0.1:8000/victima.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

links = [a["href"] for a in soup.find_all("a", href=True)]

for link in links:
    print(link.strip())

