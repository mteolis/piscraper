import constants
from urllib.request import urlopen
from lxml import etree


class Canakit():
  notify = {}
  CANAKIT_KEY = 'canakit.com'
  CANAKIT_URLS = [
      'https://www.canakit.com/raspberry-pi-4-2gb.html',
      'https://www.canakit.com/raspberry-pi-4-4gb.html',
      'https://www.canakit.com/raspberry-pi-4-8gb.html'
  ]

  def parse(self):
    print(f'parsing {self.CANAKIT_KEY} ...')

    for url in self.CANAKIT_URLS:
      print(f'parsing "{url}" ...')

      response = urlopen(url=url)
      tree = etree.parse(response, etree.HTMLParser())
      add_to_cart_button = self.get_add_to_cart_button(tree)

      print(f'checking if pi is in stock...')

      if 'sold out' in add_to_cart_button and False:
        print(f"it's sold out, so you're outta luck.")
      else:
        self.notify[constants.URL_KEY] = url
        self.notify[constants.NAME_KEY] = self.get_name(tree)
        self.notify[constants.RAM_KEY] = self.get_ram(tree)
        # self.notify[constants.PRICE_KEY] = self.get_price(tree)
        # TODO: fix fetching price
        print(f'notify: {self.notify}')

  def get_add_to_cart_button(self, tree):
      print(f'fetching stock...')

      add_to_cart_button_xpath = '//*[@id="ProductAddToCartDiv"]/a/span'
      add_to_cart_button = tree.xpath(add_to_cart_button_xpath)
      add_to_cart_button = add_to_cart_button[0].text

      return add_to_cart_button.lower()

  def get_name(self, tree):
    print(f'fetching name...')

    name_xpath = '//*[@id="MainContent_ProdName"]'
    name = tree.xpath(name_xpath)
    name = name[0].text

    return name

  def get_ram(self, tree):
    print(f'fetching ram...')

    ram_xpath = '//*[@id="MainContent_ProdName"]'
    ram = tree.xpath(ram_xpath)
    ram = ram[0].text
    ram = ram.split()[-1]

    return ram

  def get_price(self, tree):
    print(f'fetching price...')

    price_xpath = '//*[@id="MainContent_PricingDiv"]/table/tbody/tr[1]/td[2]/span'
    price = tree.xpath(price_xpath)
    print(f'price: {price}')
    print(f'type price: {type(price)}')

    return price

