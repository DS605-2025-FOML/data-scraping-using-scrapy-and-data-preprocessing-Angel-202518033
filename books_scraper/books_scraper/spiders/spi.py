import scrapy
from ..items import BooksItem

class BookSpider(scrapy.Spider):
    name = "Books"
    start_urls = ["https://books.toscrape.com/catalogue/page-1.html",]

    def parse(self,response):

        all_li_books = response.css('article.product_pod')
        
       

        for li_book in all_li_books:

            items = BooksItem()

            rating= li_book.css('p.star-rating::attr(class)').get()
            name = li_book.css('h3 a::attr(title)').get()
            price = li_book.css('div.product_price p.price_color::text').extract_first()
            stock = li_book.css('p.instock.availability::text').extract()[-1].strip()

            items['rating']= rating
            items['name']= name
            items['price']= price
            items['stock']=stock

            yield items 

        next_page = response.css('li.next a::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)




                               

