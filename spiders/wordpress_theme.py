from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from themeforest_sample.items import ThemeforestSampleItem
import urlparse

class MySpider(CrawlSpider):
  name = "wordpress_theme"
  allowed_domains = ["wordpress.org"]
  start_urls = ["https://wordpress.org/themes/"]
  rules = [Rule(LinkExtractor(allow=('themes/'),deny=('log/','browser/','theme/')),follow=True,callback='parse_link')]
    	# r'page/\d+' : regular expression for http://isbullsh.it/page/X URLs
    	#Rule(LinkExtractor(allow=(r'item/'),deny=(r'compatible_with',r'platform=', r'user/' r'tags/',),allow_domains=('themeforest.net')), callback='parse_link')]
    	# r'\d{4}/\d{2}/\w+' : regular expression for http://isbullsh.it/YYYY/MM/title URLs
  def abs_url(url, response):
      """Return absolute link"""
      base = response.xpath('//head/base/@href').extract()
      if base:
        base = base[0]
      else:
        base = response.url
      return urlparse.urljoin(base, url)

  def parse_link(self, response):
      hxs = HtmlXPathSelector(response)
      titles = hxs.select('/html')
      items = []
      
      for titles in titles:
          item = ThemeforestSampleItem()
          #base_url = get_base_url(response)
          #relative_url = titles.select("//a/@href").extract()
          #item ["link"] = urljoin_rfc(base_url,relative_url)
          item["link"] = titles.select('head/link[@rel="canonical"]/@href').extract()
          item ["short_link"] = titles.select('head/link[@rel="shortlink"]/@href').extract()
          item["name"] = titles.select('//*[@class="theme-name entry-title"]/text()').extract()
          item["author"] = titles.select('//*[@class="author"]/text()').extract()
          item["updated"] = titles.select('//*[@class="theme-meta-info"]/p/strong/text()').extract()
          #item["ratings"] = titles.select('//*[@itemprop="ratingValue"]/text()').extract()
          item["theme_website"] = titles.select('//*[@class="theme-meta-info"]/a/@href').extract()
          item["downloads"] = titles.select('//*[@class="total-downloads"]/strong/text()').extract()
          items.append(item)
      return items
