import scrapy
import json
import urllib.parse as urlparse
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from crawler.items import Car

class MobileCrawler(CrawlSpider):
	"""docstring for MobileCrawler"""
	name = "mobile"

	allowed_domains = ['mobile.de']
	onlineSince = 365
	minPrice = 50000
	start_urls = []
	with open('data/mobile_de_brand/mobile_de_brand.json') as json_data:
		brands = json.load(json_data)
		for brand in brands:
			url = 'https://suchen.mobile.de/fahrzeuge/search.html?cn=DE&damageUnrepaired=NO_DAMAGE_UNREPAIRED&daysAfterCreation=%d&isSearchRequest=true&makeModelVariant1.makeId=%s&maxPowerAsArray=PS&minPowerAsArray=PS&minPrice=%d&scopeId=C&usage=NEW' % (onlineSince,brand['id'],minPrice)
			start_urls.append(url)
	rules = (
		Rule(LinkExtractor(allow=(),restrict_css=('.rbt-page-forward',),tags=('span'),attrs=('data-href',)),callback="parse_item",follow=True),
		)

	def parse_start_url(self,response):
		return self.parse_item(response)

	def parse_item(self,response):
		item_links = response.css('.cBox-body--topResultitem > a::attr(href)').extract() + response.css('.result-item::attr(href)').extract()
		for a in item_links:
			yield scrapy.Request(a,callback=self.parse_car_detail)
		print('Processing..'+response.url)

	def parse_car_detail(self,response):
		query = urlparse.parse_qs(urlparse.urlparse(response.url).query)
		address = response.css('#rbt-seller-address::text').extract()
		if 'id' in query:
			item = Car()
			item['id'] = query['id'][0]
			item['brandId'] = query['makeModelVariant1.makeId'][0]
			item['name'] = response.css('#rbt-ad-title::text').extract()[0].strip()
			item['price'] = response.css('span.rbt-prime-price::text').extract()[0].split()[0]
			item['location'] = response.css('#rbt-seller-address::text').re(r'DE-([0-9]{5})')[0]
			yield item

