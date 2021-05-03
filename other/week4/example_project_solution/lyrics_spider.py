"""
Example of a scraper using the scrapy library

more sophisticated alternative to using requests + BS4
"""
import scrapy
from scrapy.http import Request


class LyricsSpider(scrapy.Spider):
    name = 'lyrics'
    allowed_domains = ['lyrics.com']
    start_urls = ['https://www.lyrics.com/artist/Dire-Straits/4101']  # !! no slash

    def get_filename(self, path, url):
        suffix = url.split('/')[-1]
        fn = path + '/' + suffix.replace('+', '_') + '.html'
        return fn

    def parse(self, response):
        """find song pages"""
        urls = response.xpath('//td[@class="tal qx"]/strong/a/@href').extract()
        for next_page_url in urls:
            url = response.urljoin(next_page_url)
            print(url)
            yield Request(url)

        print('-' * 40)

        song = response.xpath('//pre[@id="lyric-body-text"]//text()').extract()
        # last slash matters for recursing deeper tags!!!
        if song:
            filename = self.get_filename('direstraits', response.url)
            text = '\n'.join(song)
            open(filename, 'w').write(text)
            print(filename, len(text))
