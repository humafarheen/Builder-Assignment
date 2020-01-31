from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.item import Item

class AmazonCrawler(CrawlSpider):
    name = 'word_crawl'
    allowed_domains = ["www.amazon.com"]
    start_urls = ["http://www.amazon.com"]
    rules = [Rule(LinkExtractor(), follow=True, callback = 'find_words')]
    words = [
        "Virtue",
        "signalling",
        "is",
        "society's",
        "version",
        "of",
        "Proof",
        "of",
        "Stake",
    ]
    def find_words(self, response):
        url = response.url
        contenttype = response.headers.get("content-type", "").decode("utf-8").lower()
        data = response.body.decode("utf-8")
        for w in self.words:
            if w in data:
                print(w + ":"+url)
                self.words.remove(w)
        return Item()

    def _requests_to_follow_(self, response):
        if getattr(response, "encoding", None) != None:
            return CrawlSpider._requests_to_follow_(self.response)
        else:
            return []