import scrapy


class LightnewparsSpider(scrapy.Spider):
    name = "lightnewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = [f"https://www.divan.ru/category/svet/page-{i}" for i in range(1, 8)]
    # Генерация URL-адресов для всех 7 страниц с освещением на сайте

    def parse(self, response):
        lights = response.css("div._Ud0k")
        for light in lights:
            name = light.css("div.lsooF span::text").get(),
            price = light.css("div.pY3d2 span::text").get(),
            url = light.css("a").attrib['href']

            print(f"Name: {name}, Price: {price}, URL: {url}")

            yield {
                "name": name,
                "price": price,
                "url": url
            }
