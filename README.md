# Keyword Detector

## Install
```
pip install scrapy
pip install bs4
```

## Run

```bash
cd keyword_detector
scrapy crawl webcrawler -t csv -o client_text_matches.csv -a sitemap_url=https://client.test/sitemap.xml -a keywords="term1 term2"
```
