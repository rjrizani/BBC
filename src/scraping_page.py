from curl_cffi import requests
from bs4 import BeautifulSoup
import random
from .convert_file import save_article_to_csv 

def extract_article_content(url):

    try:
        browser = random.choice(["chrome", "firefox", "safari", "edge"])
        response = requests.get(url, impersonate=browser)
        response.raise_for_status()  # Raise an exception for bad status codes

        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the title (this might need adjustment based on the exact structure)
        title_element = soup.find('h1')  # Find the main heading
        title = title_element.get_text(strip=True) if title_element else "Title not found"

        # Extract the main content text (this will likely need more refinement)
        content_elements = soup.find_all("div", {"data-component": "text-block"})  # Example: Find elements that might hold the content
        content = ""
        for element in content_elements:
            for p in element.find_all('p'):
                content += p.get_text(strip=True) + "\n"

        return {"title": title, "content": content}

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return None
    except Exception as e:
        print(f"Error parsing content: {e}")
        return None

"""# Example usage:
article_url = "https://www.bbc.com/future/article/20250306-the-future-of-conservation-might-be-in-vr-headsets"
article_data = extract_article_content(article_url)

if article_data:
    print("Article Title:", article_data["title"])
    print("\nArticle Content:\n", article_data["content"])
    save_article_to_csv(article_data, filename="articles.csv")
"""


