import re

from bs4 import BeautifulSoup
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from gravling import items


class GravlingCrawlSpider(CrawlSpider):
    name = 'website'

    def __init__(self, domain=None, keywords=None, search_text="1", search_html="0"):
        self.allowed_domains = [domain]
        self.start_urls = [f"https://{domain}"]

        self.rules = (
            Rule(LinkExtractor(), callback='parse_start_url'),
        )
        self.keywords = keywords.split()

        self.search_text = search_text == "1"
        self.search_html= search_html == "1"

        super().__init__()

    def parse_start_url(self, response):
        self.logger.info(f"Scraping url {response.url}")
        matches = []

        if self.search_text:
            soup = BeautifulSoup(response.text, 'html.parser')
            document_plain_text = soup.get_text()


            for keyword in self.keywords:
                keyword_matches = extract_terms_and_context_from_text(
                    keyword, document_plain_text
                )
                matches = [
                    *matches,
                    *keyword_matches,
                ]

        if self.search_html:
            html_text = response.text

            for keyword in self.keywords:
                keyword_matches = extract_terms_and_context_from_text(
                    keyword, html_text
                )
                matches = [
                    *matches,
                    *keyword_matches,
                ]

        for match in matches:
            match = match.replace('\n','')
            yield items.GravlingItem(text=match, url=response.url)


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

