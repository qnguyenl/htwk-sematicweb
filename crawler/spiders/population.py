import scrapy
import urllib.parse as urlparse
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from crawler.items import Brand
from selenium import webdriver

class PopulationCrawler(scrapy.Spider):
	"""docstring for MobileCrawler"""
	name = "population"
	allowed_domains = ['statistik-portal.de']
	start_urls = ['http://www.statistik-portal.de/Statistik-Portal/de_jb01_jahrtab1.asp']

	def parse(self,response):
		print(response.url)
		brands = response.css('table#tblde tbpdy').extract()
		print(brands)
		