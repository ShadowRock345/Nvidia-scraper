from scrapy import cmdline
import scrapy
#cmdline.execute("scrapy shell ""https://api.nvidia.partners/edge/product/search?page=1&limit=9&locale=de-de&category=GPU&gpu=RTX%203060%20Ti&manufacturer=NVIDIA".split())

class PostsSpider(scrapy.Spider):
    name = "posts"

    with open(r"C:\Users\Jonas\Documents\Python Projekte\selenium\postscrape\karte.txt", "r") as f1:
        text123 = f1.read()

    start_urls = [
        text123
    ]

    def parse(self, response):
        page = response.url.split('/')[-1]
        filename = 'posts-%s.html' % page
        with open("api.txt", 'wb') as file:
            file.write(response.body)