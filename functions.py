# Dependencies
import os

from splinter import Browser
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Load Environment Variables
load_dotenv()

# Path to the 'web_scraper' firefox profile with Metamask for web3 support.
profile_path = os.environ.get('WEB_SCRAPER')

# URL for the Gods Unchained Trial of the Gods pack sales page.
buy_packs_url = 'https://godsunchained.com/buy-packs'

# Function to scrape the html from a target website.
def scrape_html(target_url):
    
    # Instantiate firefox browser using the 'web_scraper' profile for web3 support.
    browser = Browser('firefox', profile=profile_path)
    # Navigate to the target URL.
    browser.visit(target_url)
    # Store the browser html.
    html = browser.html
    # Close the browser.
    browser.quit()
    # Return the html variable.
    return html
    
    
