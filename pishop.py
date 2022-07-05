import constants
from urllib.request import urlopen
from lxml import etree


class Pishop():
    notify = {}
    PISHOP_KEY = 'pishop.ca'
    PISHOP_URLS = [
        'https://www.pishop.ca/product/raspberry-pi-4-model-b-8gb/',
        'https://www.pishop.ca/product/raspberry-pi-4-model-b-4gb/',
        'https://www.pishop.ca/product/raspberry-pi-4-model-b-2gb/'
    ]

    # pishop XPATH for add to cart:
    # //*[@id="form-action-addToCart"]
    def parse(self):
        add_to_cart_button_xpath = '//*[@id="form-action-addToCart"]'
        print(f'parsing {self.PISHOP_KEY} ...')

        for url in self.PISHOP_URLS:
            print(f'parsing "{url}" ...')
            response = urlopen(url=url)
            tree = etree.parse(response, etree.HTMLParser())
            add_to_cart_button = tree.xpath(add_to_cart_button_xpath)
            add_to_cart_button = add_to_cart_button[0]
            print(f'checking if pi is in stock...')
            for item in add_to_cart_button.items():
                if item[0] == 'value':
                    if item[1] == 'Out of stock':
                        print(f"it's {item[1]}, so you're outta luck.")
                    else:
                        print(f"it's not Out of stock, QUICK GO BUY!")

        print(f'parsing {self.PISHOP_KEY} complete')
