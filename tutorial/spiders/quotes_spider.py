import scrapy


class QuotesSpider(scrapy.Spider):
    name = "srihari"
    start_urls = [
        'https://www.houseofindya.com/gold-stacked-pendant-necklace-with-black-drop-23/iprdt',
        #'http://quotes.toscrape.com/page/2/',
    ]

    custom_settings = {
        'FEED_URI' : 'data.csv'
    }
#<i class="fal fa-rupee-sign"></i>
#<div id="tab-1" class="prodecbox current"><p></p><p>This minimalist gold stacked necklace will help elevate your everyday basics. Features oval shaped motifs with a black drop<br> <br> Style Tip: Sophisticated and minimal, this gold toned neckpiece can be paired with anything in your work wear closet.</p></div>
    def parse(self, response):
        for quote in response.css('h4'):
            yield {
                'price': quote.css('span::text')[0].get(),
                #'author': quote.css('small.author::text').get(),
                #'tags': quote.css('div.tags a.tag::text').getall(),
            }
            break

        for quote in response.css('div.prodecCntr'):
            yield {
                'description': quote.css('p::text').get(),
            }
#response.css('img').xpath('@src').getall()
        for quote in response.css('div.prodLeft'):
            images = quote.css('img::attr(data-original)').extract()

            for  item in zip(images):
                yield {
                    'image_urls': [item[0]]
                }
