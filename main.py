from curl_cffi import requests
from bs4 import BeautifulSoup
import random
from src.convert_file import save_article_to_csv, save_links_to_csv
from src.scraping_page import extract_article_content
import logging
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

BASE_URL = "https://www.bbc.com"
START_URL = f"{BASE_URL}/business"

def process_article(link_data):
    try:
        logging.info(f"Processing article: {link_data['title']}")
        article_data = extract_article_content(link_data['link'])
        
        if article_data:
            save_article_to_csv(article_data, filename="articles_4.csv")
            logging.info(f"Article saved: {article_data['title']}")
            return True
        return False
    except Exception as e:
        logging.error(f"Error processing article {link_data['link']}: {str(e)}")
        return False

def scrape_page(url):
    """
    Scrapes a single page for article links and extracts/saves article content.
    """
    try:
        browser = random.choice(["chrome", "firefox", "safari", "edge"])
        response = requests.get(url, impersonate=browser)
        response.raise_for_status()  # Raise an exception for bad status codes
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')

        all_links = []
        for a_tag in soup.find_all('a', href=True):
            link = a_tag['href']
            title = a_tag.get_text(strip=True)
            if title and ("/article/" in link or '/news/articles/' in link):  # only accept link with /article/
                full_link = link if link.startswith("http") else f"{BASE_URL}{link}"
                all_links.append({'title': title, 'link': full_link})
                logging.info(f"Found link: {title} - {full_link}")

                

        logging.info(f"Number of links found: {len(all_links)}")
        for i in range(min(5, len(all_links))):
            logging.info(all_links[i])

        # Extract article content from all links
        successful_extractions = 0
        failed_extractions = 0

        # Use ThreadPoolExecutor for parallel processing
        with ThreadPoolExecutor(max_workers=10) as executor:
            future_to_link = {executor.submit(process_article, link_data): link_data 
                            for link_data in all_links}
            
            for future in as_completed(future_to_link):
                link_data = future_to_link[future]
                try:
                    if future.result():
                        successful_extractions += 1
                    else:
                        failed_extractions += 1
                except Exception as e:
                    logging.error(f"Error processing article {link_data['link']}: {str(e)}")
                    failed_extractions += 1

        logging.info(f"Extraction complete. Successfully extracted {successful_extractions} articles.")
        logging.info(f"Failed to extract {failed_extractions} articles.")

        save_links_to_csv(all_links, name='links_article_4.csv')
        logging.info("Links saved to links_article_.csv")

    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching URL: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}", exc_info=True)

if __name__ == "__main__":
    scrape_page(START_URL)



