# Keyword Detector
This is a tool that helps you identify strings on a website and build reports.

## Requirements
- python 3.6+
- pip

## Install

```bash
pip install -r requirements.txt
```

## Usage

### Identifing keywords on a website

This command will scrape all pages in the sitemap and return the text 

```bash
cd keyword_detector
scrapy crawl webcrawler -t csv -o matches.csv -a sitemap_url=https://client.test/sitemap.xml -a keywords="Lynx"
```

Will generate a list that looks like this:

```csv
text,url
Tomorrow. Lynx browser is,https://example.com/about
 is easy. Lynx is quick a,https://example.com/installation
```

## Security
If you believe you have found a security issue with any of our projects please email us at [security@frojd.se](security@frojd.se).
