# main.py
import streamlit as st
from scrape import (
    scrape_website,
    extract_body_content,
    clean_body_content,
    split_dom_content,
)
from parse import parse_with_ollama

st.title("AI Web Scraper")
url = st.text_input("Enter a Website URL:")

# Step 1: Scrape the Website
if st.button("Scrape Site"):
    if url:
        st.write("Scraping Website...")
        
        # Get raw HTML from the scrape_website function
        html_content = scrape_website(url)
        
        if isinstance(html_content, dict) and "error" in html_content:
            st.error(f"Error: {html_content['error']}")
        else:
            body_content = extract_body_content(html_content)
            cleaned_content = clean_body_content(body_content)

            # Store the cleaned DOM content in Streamlit session state
            st.session_state.dom_content = cleaned_content
            st.session_state.parse_results = None  # Reset parse results on new scrape

            # Display the cleaned DOM content in an expandable text box
            with st.expander("View DOM Content"):
                st.text_area("DOM Content", cleaned_content, height=300)

# Check if there's DOM content in session state
if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse?")

    # Parse content if the button is clicked and description is provided
    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content")
            
            # Check if parse_results already exists to avoid re-parsing
            if st.session_state.parse_results is None:
                # Split DOM content into chunks
                dom_chunks = split_dom_content(st.session_state.dom_content)
                result = parse_with_ollama(dom_chunks, parse_description)
                
                # Store parsed results in session state
                st.session_state.parse_results = result

    # Display parsed results if available
    if st.session_state.parse_results:
        st.subheader("Parsed Results")
        st.write(st.session_state.parse_results)
