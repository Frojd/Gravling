# Grävling

Grävling is a web crawler that lets you search for terms across a website and saves them as a report in a format of your choosing.

## Features
- Search through human readable text
- Search page markup
- Supports both crawling by sitemap of by following links
- Get reports as either csv, json or xml

## Requirements

- python 3.6+
- pip

## Install

```bash
pip install -r requirements.txt
```

## Usage

### Gather urls for pages that contains a certain text by crawling sitemap

This command will scrape all pages in the sitemap and return the matching text and the url where text was found. By default it will only search the human readable text.

```bash
cd gravling
scrapy crawl sitemap -o matches.csv -a url=https://client.test/sitemap.xml -a keywords="Lynx"
```

Will generate a list that looks like this:

```csv
text,url
Tomorrow. Lynx browser is,https://example.com/about
 is easy. Lynx is quick a,https://example.com/installation
```

### Gather urls for pages that has markup that contains a certain text, by crawling sitemap

This command will only search page source markup and return any matches it finds.

```bash
cd gravling
scrapy crawl sitemap -o matches.csv -a url=https://client.test/sitemap.xml -a keywords="Lynx" -a search_html=1 -a search_text=0
```

Will generate a list that looks like this:

```csv
text,url
orrow. <b>Lynx</b> brows,https://example.com/credits
. <strong>Lynx</strong> ,https://example.com/unix
```


### Gather urls for pages that contains a certain text by following links

```bash
cd gravling
scrapy crawl website -o matches.csv -a domain=lynx.browser.org -a keywords="lynx Lynx"
```

Will generate a list that looks like this:

```csv
text,url
 write to lynx-dev@nongn,https://lynx.browser.org
d by  web@lynx.browser.o,https://lynx.browser.org
```

## Security

If you believe you have found a security issue with any of our projects please email us at [security@frojd.se](security@frojd.se).
