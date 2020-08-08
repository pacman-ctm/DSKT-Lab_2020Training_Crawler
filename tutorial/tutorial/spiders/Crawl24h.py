import scrapy

visited_links = set()

class Crawl24h(scrapy.Spider):
    name = "Crawl24h"
    allowed_domains = ['24h.com.vn']

    start_urls = ['https://www.24h.com.vn/bong-da/tran-dau-hang-tram-trieu-do-cho-ngua-o-dau-mu-o-ngoai-hang-anh-c48a1170417.html', ]

    def parse(self, response):
        if response.url not in visited_links:
            visited_links.add(response.url)
            f = open('crawl24h.txt', 'a', encoding='utf8')
            f.write(str(len(visited_links)) + ':\n * Crawling from: ' + response.url)

            title = response.css('h1.clrTit::text').get()
            keywords = response.css('meta[name="keywords"]::attr("content")').get()
            time = response.css('div.updTm::text').get()
            summary = response.css('h2.ctTp::text').get()
            source = response.css('span.txtFull::text').get()

            data = {
                'content': '\n '.join(['\n'.join(c.css('*::text').getall())
                    for c in response.css('section.enter-24h-cate-article p')
                ]),
            }

            f.write('\n * Title: ' + title + '\n * Keywords: ' + keywords + '\n * Time: ' + time + '\n * Content: ' + data['content'] + '\n * Summary: ' + summary + '\n')

            next_link = response.css('span.nwsTit > a::attr(href)').getall()
            for link in next_link:
                if next_link is not None:
                    yield response.follow(link, self.parse)