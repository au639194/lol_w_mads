# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 00:05:51 2023

@author: LordL
"""

import requests
import time
from bs4 import BeautifulSoup


# EA forum threads scape
ea_threads = []
for page in range(1, 11):
    url = f'https://forum.effectivealtruism.org/allPosts?page={page}'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        for thread in soup.find_all('a', class_='post-title'):
            ea_threads.append(thread.get('href'))
    else:
        print(f"Failed to scrape {url}, status code {response.status_code}")
    time.sleep(1)


# Scrape 80000 Hours articles
eighty_thousands_articles = []
url = 'https://80000hours.org/articles/'
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'lxml')
    for article in soup.find_all('a', class_='content-box-link'):
        eighty_thousands_articles.append(article.get('href'))
else:
    print(f"Failed to scrape {url}, status code {response.status_code}")

# Combine all URLs to scrape
urls = ea_threads + eighty_thousands_articles

    
    # Scrape text from each URL
texts = []
for url in urls:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        text = ' '.join([p.get_text() for p in soup.find_all('p')])
        texts.append(text)
    else:
        print(f"Failed to scrape {url}, status code {response.status_code}")
    time.sleep(1)


#Save the scraped text to a file
with open('corpus.txt', 'w') as f:
    for text in texts:
        f.write(text + '\n')