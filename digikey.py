import constants
from urllib.request import urlopen
from lxml import etree


class Digikey():
  notify = {}
  DIGIKEY_KEY = 'digikey.ca'
  DIGIKEY_URLS = [
      'https://www.digikey.ca/en/products/detail/raspberry-pi/RASPBERRY-PI-4-MODEL-B-8G/12159401',
      'https://www.digikey.ca/en/products/detail/raspberry-pi/Raspberry-Pi-4B-4GB/10258781',
      'https://www.digikey.ca/en/products/detail/raspberry-pi/Raspberry-Pi-4B-2GB/10258782'
  ]

  def parse(self):
    print(f'parsing {self.DIGIKEY_KEY} ...')

    for url in self.DIGIKEY_URLS:
      print(f'parsing "{url}" ...')

      response = urlopen(url=url)
      tree = etree.parse(response, etree.HTMLParser())
      stock = self.get_stock(tree)
      # TODO: finish implementing parse

      print(f'checking if pi is in stock...')

  def get_stock(self, tree):
      print(f'fetching stock...')

      stock_xpath = '//*[@id="__next"]/main/div/div[1]/div[2]/div/div/div[1]/div/div/span'
      stock = tree.xpath(stock_xpath)
      # TODO: fix fetching stock xpath
      print(f'stock: {stock}')
      print(f'type stock: {type(stock)}')
      stock = stock[0].text
      print(f'stock: {stock}')

      return stock.lower()
