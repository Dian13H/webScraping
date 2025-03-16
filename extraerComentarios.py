from bs4 import BeautifulSoup, Comment
import requests

url = "http://127.0.0.1:8000/victima.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

def iscomment(elem):
    return isinstance(elem, Comment)

comments = soup.find_all(string=iscomment)

for comment in comments:
    print(comment.strip())
