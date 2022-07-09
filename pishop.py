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

    def parse(self):
        print(f'parsing {self.PISHOP_KEY} ...')

        for url in self.PISHOP_URLS:
            print(f'parsing "{url}" ...')

            response = urlopen(url=url)
            tree = etree.parse(response, etree.HTMLParser())
            add_to_cart_button = self.get_add_to_cart_button(tree)

            print(f'checking if pi is in stock...')

            for item in add_to_cart_button.items():
                if item[0] == 'value':
                    if item[1] == 'Out of stock':
                        print(f"it's {item[1]}, so you're outta luck.")
                    else:
                        self.notify[constants.URL_KEY] = url
                        self.notify[constants.NAME_KEY] = self.get_name(tree)
                        self.notify[constants.RAM_KEY] = self.get_ram(tree)
                        self.notify[constants.PRICE_KEY] = self.get_price(tree)
                        print(f'notify: {self.notify}')
                        print(f"it's not Out of stock, QUICK GO BUY!")

        print(f'parsing {self.PISHOP_KEY} complete')

    def get_add_to_cart_button(self, tree):
        print(f'fetching stock...')

        add_to_cart_button_xpath = '//*[@id="form-action-addToCart"]'
        add_to_cart_button = tree.xpath(add_to_cart_button_xpath)
        add_to_cart_button = add_to_cart_button[0]

        return add_to_cart_button

    def get_name(self, tree):
        print(f'fetching name...')

        name_xpath = '//*[@id="product-listing-container"]/div/div[2]/section[2]/div/h1'
        name = tree.xpath(name_xpath)
        name = name[0].text

        return name

    def get_ram(self, tree):
        print(f'fetching ram...')

        ram_xpath = '//*[@id="product-listing-container"]/div/div[2]/section[2]/div/h1'
        ram = tree.xpath(ram_xpath)
        ram = ram[0].text
        ram = ram.split('/')[-1]

        return ram

    def get_price(self, tree):
        print(f'fetching price...')

        price_xpath = '//*[@id="product-listing-container"]/div/div[2]/section[2]/div/div[2]/div/span'
        price = tree.xpath(price_xpath)
        price = price[0].text

        return price
    
