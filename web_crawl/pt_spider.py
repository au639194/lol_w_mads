# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 19:56:52 2023

@author: Bruger
"""

import scrapy
import csv

class PsychologyTodaySpider(scrapy.Spider):
    name = 'psychologytoday'
    allowed_domains = ['psychologytoday.com']
    start_urls = ['https://www.psychologytoday.com/intl/blog/balanced/202304/air-pollution-and-depression']

    custom_settings = {
        'FEED_URI': 'file:///D:/lol_w_mads/web_crawl/psych_art.csv',
        'FEED_FORMAT': 'csv'
    }

    def parse(self, response):
        title = response.css('#block-pt-content > article > div.blog-entry--header > div.blog-entry--header-second > h1::text').get()
        author = response.css('#block-pt-content > article > div.blog-entry--header > div.blog-entry--header-first > div > div.profile-card__profile-copy > div.h3.profile-card__profile-name > a::text').get()
        date = response.css('#block-pt-content > article > div.blog-entry--header > div.blog-entry--header-second > p > span.blog_entry--date::text').get()
        content = response.css('#block-pt-content > article > div.blog-entry--body > div.blog-entry--body-second::text').getall()

        yield {
            'title': title,
            'author': author,
            'date': date,
            'content': content
        }

        # Save the results into a CSV file
        with open('psychologytoday.csv', mode='a', encoding='utf-8', newline='') as csv_file:
            fieldnames = ['title', 'author', 'date', 'content']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            if csv_file.tell() == 0:
                writer.writeheader()

            writer.writecolumn({
                'title': title,
                'author': author,
                'date': date,
                'content': ' '.join(content)
            })
            