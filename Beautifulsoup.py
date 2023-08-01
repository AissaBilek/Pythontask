import requests
from bs4 import BeautifulSoup
import pandas as pd
class Beautifuloupclasse:
#a constructor method of the class
    def _init_(self,link):
        self.link= link
#adding a new method to extract data from the website
    def extractData(self):
        services_providing=requests.get(self.link)
        print(services_providing)
        html = BeautifulSoup(services_providing.content, 'html.parser')
        infraXcode_services=html.select(".elementor-widget-wrap.elementor-element-populated h2 a")
        return infraXcode_services
    




infraXcode_services=html.select(".elementor-widget-wrap.elementor-element-populated h2 a")
for item in infraXcode_services:
    print(item.text)
    print('***')


   



