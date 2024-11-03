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

#Examples
![Screenshot](https://private-user-images.githubusercontent.com/145309558/382586363-eb176c0c-24d7-41ec-bf59-5dd67d8d9cca.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzA2NTA1NzksIm5iZiI6MTczMDY1MDI3OSwicGF0aCI6Ii8xNDUzMDk1NTgvMzgyNTg2MzYzLWViMTc2YzBjLTI0ZDctNDFlYy1iZjU5LTVkZDY3ZDhkOWNjYS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQxMTAzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MTEwM1QxNjExMTlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT04MWIxYmVkZDdhNzBkM2ZhZDdjZTcwODk5M2ZlOWQ2ZjRmODYwZmZmODAxM2I5NDQ2MDc0OGM1NWI5NjY4NWYyJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.64hdYJG617uYXSO4kYHpZ52VYX48yn6_cwyDnvbOYKg)
![Screenshot](https://private-user-images.githubusercontent.com/145309558/382586367-745ac07a-df46-4ba3-82b9-33f270712165.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzA2NTA1NzksIm5iZiI6MTczMDY1MDI3OSwicGF0aCI6Ii8xNDUzMDk1NTgvMzgyNTg2MzY3LTc0NWFjMDdhLWRmNDYtNGJhMy04MmI5LTMzZjI3MDcxMjE2NS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQxMTAzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MTEwM1QxNjExMTlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0yNjAxMTljYjVmNjk2Yjk4M2RlMTM0ZWRiODVhZjgyMGNkNGVlOTdmYzI5YmY4YjYzMDQ5Mzk3YWMxZmM0NDU5JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.eNnjmu7V82BYWEhForcNXEwE1DcHesVAM8YWzqQxHDg)
![Screenshot](https://private-user-images.githubusercontent.com/145309558/382586369-d6ec9bf5-5f74-4b5d-9669-764dda35a460.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzA2NTA1NzksIm5iZiI6MTczMDY1MDI3OSwicGF0aCI6Ii8xNDUzMDk1NTgvMzgyNTg2MzY5LWQ2ZWM5YmY1LTVmNzQtNGI1ZC05NjY5LTc2NGRkYTM1YTQ2MC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQxMTAzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MTEwM1QxNjExMTlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT01OTY2NjI1NTRkOTlmOGI2MzQ4YzYwOTA5MzZkYzliOWQ2ODMzODNjYWIyZWU5ZTlhYzIzOWU1YTcxODc2ODY1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.B25lgej5z1Y4bJgwYBugcaBP_wZz7ggd32Sqb-uRf-M)
![Screenshot](https://private-user-images.githubusercontent.com/145309558/382586369-d6ec9bf5-5f74-4b5d-9669-764dda35a460.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzA2NTA1NzksIm5iZiI6MTczMDY1MDI3OSwicGF0aCI6Ii8xNDUzMDk1NTgvMzgyNTg2MzY5LWQ2ZWM5YmY1LTVmNzQtNGI1ZC05NjY5LTc2NGRkYTM1YTQ2MC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQxMTAzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MTEwM1QxNjExMTlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT01OTY2NjI1NTRkOTlmOGI2MzQ4YzYwOTA5MzZkYzliOWQ2ODMzODNjYWIyZWU5ZTlhYzIzOWU1YTcxODc2ODY1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.B25lgej5z1Y4bJgwYBugcaBP_wZz7ggd32Sqb-uRf-M)
![Screenshot](https://private-user-images.githubusercontent.com/145309558/382586371-a781eabd-8f41-48b9-9fd4-27e13464afb5.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzA2NTA1NzksIm5iZiI6MTczMDY1MDI3OSwicGF0aCI6Ii8xNDUzMDk1NTgvMzgyNTg2MzcxLWE3ODFlYWJkLThmNDEtNDhiOS05ZmQ0LTI3ZTEzNDY0YWZiNS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQxMTAzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MTEwM1QxNjExMTlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1hZTZhM2YzMjMxNWY2MGQxYTI4N2QyNmMxZDNhZDI0NWQ4MmI0ZjhmZDA2YWE5ZTIzZDZjNzA1ZjNhZWQ3MjNlJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.1SyMKTL4uOhNP0eLjtoplENrUibeTBP7RTF5Cea5pf0)
