import re
from io import StringIO
from functools import partial

from bs4 import BeautifulSoup
import scrapy
from scrapy.http import Request
from scrapy.spiders import SitemapSpider, Rule
from scrapy.item import Item


class MatchItem(scrapy.Item):
    text = scrapy.Field()
    url = scrapy.Field()


def find_all_substrings(string, sub):
    starts = [match.start() for match in re.finditer(re.escape(sub), string)]
    return starts


def extract_terms_and_context_from_text(needle, text):
    text_len = len(text)

    matches = []
    for m in re.finditer(needle, text):
        start = m.start()-10
        start = start if start > 0 else 0
        end = m.end()+10
        end = end if end <= text_len else text_len
        matches.append(text[start:end])

    return matches


class WebsiteSpider(SitemapSpider):
    name = "webcrawler"

    def __init__(self, sitemap_url='http://example.test', keywords=None):
        super().__init__()

        self.sitemap_urls = [sitemap_url]
        self.keywords = keywords.split()

    def parse(self, response):
        self.logger.info(f"Scraping url {response.url}")

        soup = BeautifulSoup(response.text, 'html.parser')
        document_plain_text = soup.get_text()

        matches = []

        for keyword in self.keywords:
            keyword_matches = extract_terms_and_context_from_text(
                keyword, document_plain_text
            )
            matches = [
                *matches,
                *keyword_matches,
            ]

        for match in matches:
            match = match.replace('\n','')
            yield MatchItem(text=match, url=response.url)
