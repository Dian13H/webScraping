import requests
from bs4 import BeautifulSoup, Comment
from urllib.parse import urljoin, urlparse
import re

class WebCrawler:
    def __init__(self, base_url, max_depth=2):
        self.base_url = base_url
        self.max_depth = max_depth
        self.visited_urls = set()
        self.comments = []  
        self.emails = []  
        self.links = []  # Variable para almacenar los enlaces

    def crawl(self, url, depth=0):
        if depth > self.max_depth or url in self.visited_urls:
            return

        print(f"[{depth}] Crawling: {url}")
        self.visited_urls.add(url)

        try:
            response = requests.get(url, timeout=5)
            if response.status_code != 200:
                return

            soup = BeautifulSoup(response.text, "html.parser")

            self.extract_comments(soup)

            self.extract_emails(soup)

            self.extract_links(soup)

            for link in soup.find_all("a", href=True):
                full_url = urljoin(url, link["href"])
                if self.is_valid_url(full_url):
                    self.crawl(full_url, depth + 1)

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    def extract_emails(self, soup):
        for tag in soup.find_all("a", href=True):
            if tag['href'].startswith('mailto:'):
                email = tag['href'][7:]
                self.emails.append(email)

    def extract_comments(self, soup):
        comments = soup.find_all(string=lambda text: isinstance(text, Comment))
        for comment in comments:
            self.comments.append(comment.strip())

    def extract_links(self, soup):
        for link in soup.find_all("a", href=True):
            self.links.append(link["href"])

    def is_valid_url(self, url):
        parsed = urlparse(url)
        return parsed.netloc == urlparse(self.base_url).netloc and url not in self.visited_urls

    def print_results(self):
        # Imprime los enlaces
        if self.links:
            print("\n".join(self.links))
        
        # Agrega un salto de línea solo si hay comentarios
        if self.links and self.comments:
            print()  # Este es el salto de línea entre los enlaces y los comentarios

        # Imprime los comentarios
        if self.comments:
            print("\n".join(self.comments))
        
        # Agrega un salto de línea solo si hay correos electrónicos
        if self.comments and self.emails:
            print()  # Este es el salto de línea entre los comentarios y los correos electrónicos

        # Imprime los correos electrónicos
        if self.emails:
            print("\n".join(self.emails))


if __name__ == "__main__":
    start_url = "http://127.0.0.1:8000/victima.html"
    crawler = WebCrawler(start_url, max_depth=2)
    crawler.crawl(start_url)
    crawler.print_results()

