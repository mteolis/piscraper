from pishop import Pishop
from canakit import Canakit
from digikey import Digikey
from canada_newark import CanadaNewark

print(f'running scraper...')
pishop = Pishop()
pishop.parse()
canakit = Canakit()
canakit.parse()
digikey = Digikey()
digikey.parse()
# canada_newark = CanadaNewark()
# canada_newark.parse()
print(f'running scraper complete')
