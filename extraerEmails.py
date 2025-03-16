from bs4 import BeautifulSoup
import requests

# URL de la página
url = "http://127.0.0.1:8000/victima.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Encontrar todas las etiquetas <a>
tags = soup.find_all("a")

# Iterar sobre las etiquetas <a> y extraer correos electrónicos de mailto
for tag in tags:
    if tag.has_attr("href") and tag['href'].startswith('mailto:'):
        # Extraer el correo electrónico y mostrarlo
        email = tag['href'][7:]  # Eliminar "mailto:" del inicio
        print(email)

