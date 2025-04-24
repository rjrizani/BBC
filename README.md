# BBC Article Scraper

This project is designed for web scraping articles from the BBC website, specifically starting from the business section.

Articles was scraped with BeautifulSoup for parsing HTML content and curl_cffi for browser impersonation.

## Key Features:

1.  **Imports**:
    * Uses libraries such as `curl_cffi` for efficient HTTP requests.
    * Leverages `BeautifulSoup` for parsing HTML content.
    * Employs `random` to select user-agent strings for browser impersonation.
    * Utilizes custom modules (`src.convert_file` and `src.scraping_page`) for saving data and extracting article content.

2.  **Logging**:
    * Configured at the beginning to provide detailed logs of operations at various levels (INFO, ERROR) for monitoring and debugging.

3.  **Constants**:
    * `BASE_URL`: Defines the base URL of the BBC website (`https://www.bbc.com`).
    * `START_URL`: Specifies the initial page for scraping, set to the BBC Business section (`https://www.bbc.com/business`).

4.  **Functions**:
    * `process_article(link_data)`:
        * Accepts a dictionary `link_data` containing the title and URL of an article.
        * Extracts the main content of the article by calling `extract_article_content` from the `src.scraping_page` module.
        * Persists the extracted article data into a CSV file named `articles_4.csv` using the `save_article_to_csv` function from `src.convert_file`.
        * Includes error handling to catch and log any issues encountered during article processing.

    * `scrape_page(url)`:
        * Takes a URL as input and scrapes it for article links.
        * Performs an HTTP GET request to the given `url`, using a randomly chosen browser user-agent to mimic real browser traffic.
        * Parses the HTML response using BeautifulSoup to locate article links based on specific URL patterns (`/article/` or `/news/articles/`).
        * Saves all the discovered article links to a CSV file named `links_article_4.csv` for future reference or analysis.
        * Employs `ThreadPoolExecutor` to process each discovered article link in parallel, significantly speeding up the extraction and saving of article content.
        * Logs the total number of successfully and unsuccessfully processed articles to provide a summary of the scraping operation.

5.  **Main Execution**:
    * The script initiates the scraping process by calling the `scrape_page` function with the `START_URL`, beginning the crawl from the BBC Business section.

## Workflow:

1.  The script starts by fetching the HTML content of the specified starting page (`https://www.bbc.com/business`).
2.  It then parses this HTML to identify and extract all article links and their corresponding titles that match predefined URL patterns.
3.  The extracted article links are saved into the `links_article_4.csv` file.
4.  For each discovered link, the script concurrently extracts the full article content.
5.  The extracted content of each article is then saved into the `articles_4.csv` file.
6.  Throughout the entire process, detailed logs are recorded to monitor the script's progress and any errors that might occur.

## Error Handling:

* The script implements error handling to gracefully manage issues such as invalid HTTP status codes during web requests or exceptions encountered during the processing of individual articles. Any errors are caught and logged with informative messages, ensuring the scraping process is robust and provides insights into potential problems.

## Output:

The script generates two CSV files in the same directory where it is executed:

1.  `articles_4.csv`: This file contains the extracted content of the BBC articles, likely including fields such as title, body text, publication date, etc. (depending on the implementation in `src.scraping_page` and `src.convert_file`).
2.  `links_article_4.csv`: This file provides a list of all the article URLs that were discovered during the scraping process, starting from the initial `START_URL`.

This project offers an efficient and scalable solution for collecting articles from the BBC website, complete with logging and mechanisms to handle potential errors during the scraping process.
