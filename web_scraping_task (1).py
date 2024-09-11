# -*- coding: utf-8 -*-
"""web_scraping_task

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SLDQhjCbO8JuDtia6pdTiBkP-rWzvAfN
"""

import os
import requests
from bs4 import BeautifulSoup

url = "https://medium.com/some-article-url"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    paragraphs = soup.find_all('p')
    article_text = "\n".join([para.get_text() for para in paragraphs])

    if not os.path.exists('scraped_articles'):
        os.makedirs('scraped_articles')

    file_path = os.path.join('scraped_articles', 'medium_article.txt')
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(article_text)

    print(f"Article text saved to {file_path}")