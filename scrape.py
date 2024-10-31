import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    API_KEY = '0e57bba54d84c384f8a9b7e03fc7ba8d'
    try:
        response = requests.get(
            f'http://api.scraperapi.com',
            params={'api_key': API_KEY, 'url': url, 'render': 'true'}
        )
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        return {
            "title": soup.title.string if soup.title else "No title found",
            "headings": [heading.text for heading in soup.find_all('h1')],
            "paragraphs": [p.text for p in soup.find_all('p')]
        }

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
