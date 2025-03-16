from bs4 import BeautifulSoup, Comment
import re
import requests

url = "http://127.0.0.1:8000/victima.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# extraer enlaces
links = [a["href"] for a in soup.find_all("a", href=True)]
for link in links:
    print(link.strip())
print()

# extraer comentarios HTML
comments = [comment for comment in soup.find_all(string=lambda text: isinstance(text, Comment))]
for comment in comments:
    print(comment.strip())
print()

# extraer correos electrónicos
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", response.text)
for email in emails:
    print(email.strip())
