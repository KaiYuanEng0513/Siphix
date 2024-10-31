# main.py
import streamlit as st
from scrape import scrape_website

st.title("AI Web Scraper")
url = st.text_input("Enter a Website URL:")

# Step 1: Scrape the Website
if st.button("Scrape Site"):
    if url:
        st.write("Scraping Website...")
        
        dom_content = scrape_website(url)

        if "error" in dom_content:
            st.error(f"Error: {dom_content['error']}")
        else:
            # Display scraped content
            st.subheader("Page Title")
            st.write(dom_content["title"])

            st.subheader("Headings")
            for heading in dom_content["headings"]:
                st.write(heading)

            st.subheader("Paragraphs")
            for paragraph in dom_content["paragraphs"]:
                st.write(paragraph)
    else:
        st.warning("Please enter a URL.")
