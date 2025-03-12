# Save the all_links to a csv file
import logging


def save_links_to_csv(all_links, name='links_article_1.csv'):
    import csv
    with open(name, mode='a+') as file:
        writer = csv.writer(file)
        writer.writerow(['title', 'link'])
        for link in all_links:
            writer.writerow([link['title'], link['link']])

# Save the title and content to a csv file
def save_article_to_csv(article_data, filename="articles.csv"):
    import csv
    try:
        with open(filename, mode='a+', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            #writer.writerow(['title', 'content'])
            writer.writerow([article_data["title"], article_data["content"]])
    except IOError as e:
        logging.error(f"Failed to write to file {filename}: {str(e)}")