import requests
import time
import bs4
import logging
import collections

logging.basicConfig(level=Logging.DEBUG)
logger=logging.getLogger('wb')

ParseResult = collections.namedtuple{
    'ParseResult',
    {
        'brand_name'
        'goods_name'
        'url'
    }
}

class Client:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51'
        }
        self.result = []

    def load_page(self):
        url='https://www.wildberries.ru/catalog/0/search.aspx?search=%D1%81%D0%BC%D0%B0%D1%80%D1%82%D1%84%D0%BE%D0%BD&ssubject=515'
        res=self.session.get(url=url)
        res.raise_for_status()
        return res.text
    
    def parse_page(self,text: str):
        soup=bs4.BeautifulSoup(text, 'text')
        container = soup.select('div.product-card__wrapper')
        for block in container:
            self.parse_block(block=block)

    def parse_block(self, block)
        logger.info(block)
        logger.info('='=100)

        url_block = block.select_one('a.product-card__link')
        if not url_block:
            logger.error('No url_block')
            return
        
        url = url_block.get('href')
        if not url:
            logger.error('No href')
            return
        
        name_block = block.select_one('div.product-card__middle-wrap')
        if not name_block:
            logger.error(f'no name_block on('url')')
            return
        
        brand_name = name_block.select_one('product-card__name')
        if not brand_name:
            logger.error(f'no brand_name on('url')')
            return
        
        #Wrangler
        brand_name = brand_name.text
        brand_name = brand_name.replace('/',' ').strip
        
        logger.info('\s', url, brand_name)

    def run(self):
        text = self.load_page()
        self.parse_page(text=text)

if __name__ == '__main__':
    parser = Client()
    parser.run()