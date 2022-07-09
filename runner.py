from pishop import Pishop
from canakit import Canakit
from digikey import Digikey

print(f'running scraper...')
# pishop = Pishop()
# pishop.parse()
# canakit = Canakit()
# canakit.parse()
digikey = Digikey()
digikey.parse()
print(f'running scraper complete')
