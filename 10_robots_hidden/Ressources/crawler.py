import requests
from urllib.parse import urljoin
import re

BASE_URL = "http://10.12.200.36/.hidden/"
RED = "\033[38;2;170;0;0;1m"
GREEN = "\033[38;2;0;170;0;1m"
REALLY_DARK = "\033[38;2;43;43;43m"
DARK = "\033[38;2;63;63;63m"
RESET = "\033[0m"
HREF_RE = re.compile(r'href="([^"]+)"')

visited_urls = set()
session = requests.Session()

DICTIONARY = [
    "voisin",
    "toujours",
    "aide",
]

def analyse_readme(url):
    try:
        readme = session.get(url, timeout=5).text
        readme_lower = readme.lower()
        if not any(word in readme_lower for word in DICTIONARY):
            print(url, " -> ", GREEN, readme, RESET)
            return True
        else:
            print(REALLY_DARK, url, " -> ", DARK, readme, RESET)
    except Exception as e:
        print(f"{e}")
    return False

def analyse_file(file, url):
    for line in file.text.splitlines():
        match = HREF_RE.search(line)

        if not match:
            continue
        name = match.group(1)
        if name == "../":
            continue

        full_url = urljoin(url, name)

        if name == "README":
            return analyse_readme(full_url)
        elif name.endswith("/") and crawl(full_url):
            return True
    return False

def crawl(url):
    if url in visited_urls:
        return False
    visited_urls.add(url)

    try:
        file = session.get(url, timeout=5)
        if file.status_code != 200:
            return False

    except Exception as e:
        print(RED, e, RESET)
        return False

    return analyse_file(file, url)

if __name__ == "__main__":
    crawl(BASE_URL)