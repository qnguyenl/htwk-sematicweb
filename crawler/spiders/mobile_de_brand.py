import scrapy
import urllib.parse as urlparse
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from crawler.items import Brand
from selenium import webdriver
import time

class MobileBrandCrawler(scrapy.Spider):
	"""docstring for MobileCrawler"""
	name = "mobile_de_brand"
	allowed_domains = ['mobile.de']
	start_urls = ['https://suchen.mobile.de/fahrzeuge/search.html']

	def __init__(self):
		scrapy.Spider.__init__(self)
		# use any browser you wish
		self.browser = webdriver.Chrome()

	def __del__(self):
		self.browser.close()

	def parse(self,response):
		#query = urlparse.parse_qs(urlparse.urlparse(response.url).query)
		self.browser.get(response.url)
        # let JavaScript Load
		time.sleep(1)
		hxs = Selector(text=self.browser.page_source)
		brands = hxs.css('select.mmh-make-incl option')
		for brand in brands:
			id = brand.css('::attr(value)').extract_first().strip()
			name = brand.css('::text').extract_first().strip()
			if id:
				item = Brand()
				item['id'] = id
				item['name'] = name
				yield item