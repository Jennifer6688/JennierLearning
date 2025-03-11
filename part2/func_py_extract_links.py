# func_py_extract_links.py
import requests
from bs4 import BeautifulSoup

def func_py_extract_links(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        return [a["href"] for a in soup.find_all("a", href=True)]
    return []

print(func_py_extract_links("https://example.com"))
