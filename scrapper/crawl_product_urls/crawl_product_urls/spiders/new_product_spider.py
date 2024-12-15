import scrapy
from urllib.parse import urljoin
import re


class ProductSpider(scrapy.Spider):
    name = 'product_urls_new'

    start_urls = [
        "https://amazon.in"
        "https://myfrido.com/collections/cushions",
        "https://flipkart.com"
    ]

    domain_names_visited = set()
    visited_urls = set()

    product_url_pattern = re.compile(
        r'(?:/product(?:s)?/|/item/|/p/|/buy/|/shop/|/cushion/)'
    )

    def parse(self, response):
        """
        Parse the response and identify product URLs.
        """
        domain = response.url.split('/')[2]
        self.logger.info(f'Crawling domain: {domain}')

        self.domain_names_visited.add(domain)
        product_urls = set()

        for link in response.css('a::attr(href)').getall():
            absolute_url = urljoin(response.url, link)
            if absolute_url in self.visited_urls:
                continue
            self.visited_urls.add(absolute_url)
            if self.product_url_pattern.search(absolute_url):
                product_urls.add(absolute_url)
                continue
            if domain in absolute_url:
                yield scrapy.Request(
                    absolute_url,
                    callback=self.parse
                )

        if product_urls:
            yield {
                "domain": domain,
                "product_urls": list(product_urls),
            }
