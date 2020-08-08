import json

import scrapy

OUTPUT_FILENAME = 'crawl_sendo.txt'

class SendoSpider(scrapy.Spider):
    name = 'sendo'
    allowed_domains = ['sendo.vn']
    start_urls = ['https://www.sendo.vn']
    CRAWLED_COUNT = 0

    def parse(self, response):
        if response.status == 200 and response.css('body::attr("id")').get() == 'product-detail':
            print('Crawling from:', response.url)
            data = {
                'link': response.url,
                'name': response.css('h1::text').get(),
                'link_to_product': [', '.join(c.css('*::text').getall())
                                    for c in response.css('nav.breadcrumb_3hMt > ol > li > a.text_134z')],
                'description': response.css('meta[name="description"]::attr("content")').get(),
                'img_url': response.css('meta[property="og:image"]::attr("content")').get(),
                'keywords': response.css('meta[property="keywords"]::attr("content")').get(),
                'price_shop': response.css('meta[property="og:description"]::attr("content")').get(),
            }

            with open(OUTPUT_FILENAME, 'a', encoding='utf8') as f:
                f.write(json.dumps(data, ensure_ascii=False))
                f.write('\n')
                self.CRAWLED_COUNT += 1
                self.crawler.stats.set_value('CRAWLED_COUNT', self.CRAWLED_COUNT)
                print('SUCCESS:', response.url)

        yield from response.follow_all(css='a[href^="https://www.sendo.vn"]::attr(href), a[href^="/"]::attr(href)', callback=self.parse)
# This code works but no output file is written?

"""

import scrapy

visited_links = set()

class SendoSpider(scrapy.Spider):
    name = 'sendo'
    allowed_domains = ['sendo.vn']
    start_urls = ['https://www.sendo.vn']
    #start_urls = ['https://www.sendo.vn/vong-deo-tay-phong-thuy-nam-nu-cao-cap-go-dan-huong-do-an-do-5673320.html']
    CRAWLER_COUNT = 0

    def parse(self, response):
        if response.url not in visited_links:
            visited_links.add(response.url)
            f = open('crawl_sendo.txt', 'a', encoding='utf8')
            f.write(':\n * Crawling from: ' + response.url)


            link = response.url
            name = response.css('meta[name="og:title"]::attr("content")').get()
            name2 = response.css('h1::text').get()
            description = response.css('meta[name="description"]::attr("content")').get()
            img_url = response.css('meta[property="og:image"]::attr("content")').get()
            keywords = response.css('meta[property="keywords"]::attr("content")').get()
            # link_to_product = response.css('nav.breadcrumb_3hMt > ol > li > a.text_134z::text').getall()
            price = response.css('strong.currentPrice_2zpf::text').get()
            price_shop = response.css('meta[property="og:description"]::attr("content")').get()

            data = {
                'link_to_product': [', '.join(c.css('*::text').getall())
                                        for c in response.css('nav.breadcrumb_3hMt > ol > li > a.text_134z')],
            }

            f.write('\n * Name: ' + str(name2))
            if (keywords != ""):
                f.write('\n * Keywords: ' + keywords)
            else:
                f.write('\n * No keywords')
            #f.write('\n * Product location: ' + data['link_to_product'])
            f.write('\n * Description: ' + description)
            f.write('\n * Link image: ' + img_url)
            f.write('\n * Price & shop: ' + price_shop + '\n')

            #next_link = response.css('span.nwsTit > a::attr(href)').getall()
            #for link in next_link:
            #    if next_link is not None:
                    #yield response.follow(link, self.parse)
            yield from response.follow_all(css='a[href^="https://www.sendo.vn"]::attr(href), a[href^="/"]::attr(href)', callback=self.parse)"""
