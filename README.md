# AI Web Scraper

This project is an AI-powered web scraper built using Streamlit, BeautifulSoup, and Ollama's Llama 3.1 model for parsing content. The app allows users to input a website URL, scrape its HTML content, and perform targeted parsing based on user-defined instructions.

## Features

- **Scrape Website Content**: Input any URL, and the app will fetch and display the main content of the page.
- **Cleaned Content Display**: Scripts, styles, and unnecessary tags are removed for easier readability.
- **Content Parsing with AI**: Use Ollama’s Llama 3.1 model to extract specific information based on a custom description or query.

## Prerequisites

- **Python 3.8+**
- **Streamlit**: For building the web app interface.
- **BeautifulSoup**: For HTML content parsing.
- **Ollama with Llama 3.1 Model**: Note that Llama 3.1 must be installed **locally** to support the AI parsing feature.
  
> **Note**: This project requires **Ollama’s Llama 3.1 model to be installed locally** to function fully. Users deploying this app on a remote server will need to install Ollama on the server or access a cloud service that can provide the model's inference.

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   
2. Install Required Python Packages
    ```bash
   pip install -r requirements.txt\
    
3. Install Ollama and Llama 3.1 Locally
  - Follow Ollama’s documentation to install Ollama and set up the Llama 3.1 model locally.
  - Ensure that Ollama is correctly configured to allow local usage of the Llama 3.1 model with your Python environment.

4. Configure Environment Variables
  - Create a .env file in the root directory.
  - Add your SCRAPER_API_KEY for web scraping (ScraperAPI or similar).
  ```bash
   SCRAPER_API_KEY=your_scraper_api_key
  ```
5. Run the Application
   ```bash
   streamlit run main.py

## **Usage**
1. Enter a URL you want to scrape.
2. Click on "Scrape Site" to fetch the main content.
3. View the cleaned DOM content in the expandable section.
4. Enter a description for parsing and click "Parse Content" to extract specific information with Llama 3.1.
5. 
## **Limitations**
1. Requires Local Installation of Ollama and Llama 3.1: Users must install Ollama’s Llama 3.1 model locally. This means the app will not work out-of-the-box on platforms that do not support local installations of this model.
2. Hosting: Deploying on cloud services will require a server with Ollama support.
