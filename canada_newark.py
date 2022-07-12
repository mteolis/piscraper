import constants
from urllib.request import urlopen
from lxml import etree


class CanadaNewark():
    notify = {}
    CANADA_NEWARK_KEY = 'canada.newark.com'
    CANADA_NEWARK_URLS = [
        'https://canada.newark.com/raspberry-pi/rpi4-modbp-8gb/raspberry-pi-4-model-b-8gb/dp/64AH2041',
        'https://canada.newark.com/raspberry-pi/rpi4-modbp-4gb/raspberry-pi-4-model-b-4gb-rohs/dp/02AH3164',
        'https://canada.newark.com/raspberry-pi/rpi4-modbp-2gb/raspberry-pi-4-model-b-2gb-rohs/dp/02AH3162'
    ]

    def parse(self):
        print(f'parsing {self.CANADA_NEWARK_KEY} ...')

        for url in self.CANADA_NEWARK_URLS:
            print(f'parsing "{url}" ...')

            response = urlopen(url=url)
            print(f'after response')

            tree = etree.parse(response, etree.HTMLParser())
            print(f'after etree')
            self.get_name(tree)
            print(f'after getname')
            # TODO: finish parsing function

    def get_name(self, tree):
        print(f'fetching name...')

        name_xpath = '//*[@id="pdpSection_pdpProductRange"]/div[1]/h2'
        name = tree.xpath(name_xpath)
        name = name[0].text
        print(f'name: {name}')
