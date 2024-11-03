# scrape.py
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def scrape_website(url):
    # Retrieve API key from the environment variable
    API_KEY = os.getenv("SCRAPER_API_KEY")
    
    if not API_KEY:
        return {"error": "API Key not found. Ensure it's set in your .env file."}
    
    try:
        # Make request to ScraperAPI with proper parameters
        response = requests.get(
            'http://api.scraperapi.com',
            params={'api_key': API_KEY, 'url': url, 'render': 'true'}
        )
        
        response.raise_for_status()  # Raise an error if the request failed
        
        # Return the full HTML content if the request succeeds
        return response.text

    except requests.exceptions.RequestException as e:
        # Return the error message in case of a request exception
        return {"error": str(e)}

# Other functions remain unchanged

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    # Remove scripts and style tags for clean body text
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    # Clean and format content
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]
