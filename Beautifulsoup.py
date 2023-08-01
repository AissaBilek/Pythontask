import requests
from bs4 import BeautifulSoup
import pandas as pd
class Beautifuloupclasse:

    def _init_(self,link):
        self.link= link

    


html_page = requests.get('https://www.infraxcode.com/')

services_providing=requests.get('https://www.infraxcode.com/fournisseur-de-solutions-dautomatisation/')
print(services_providing)

html = BeautifulSoup(services_providing.content, 'html.parser')

infraXcode_services=html.select(".elementor-widget-wrap.elementor-element-populated h2 a")
for item in infraXcode_services:
    print(item.text)
    print('***')


   



