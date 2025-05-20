import csv
import json

# Convert CSV to JSON with only 'title' and 'article' keys
with open('articles_5.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = [
        {"title": row.get("title", ""), "article": row.get("article", "")}
        for row in csv_reader
    ]

with open('articles_5.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=2)