import requests
from bs4 import BeautifulSoup
import pandas as pd
class Beautifuloupclasse:
#a constructor  of the class
    def __init__(self,link):
        self.link= link
#adding a new method to extract data from the website
    def extractData(self):
        services_providing=requests.get(self.link)
        print(services_providing)
        html = BeautifulSoup(services_providing.content, 'html.parser')
        infraXcode_services=html.select(".elementor-widget-wrap.elementor-element-populated h2 a")
        return infraXcode_services
#second method to store data on excel file
    def createExcelSheet(self):
        services=[]
        data=self.extractData()
        for item in data:
         services.append({'titre':item.text})
        print(services)   
        df=pd.DataFrame(services)
        file_name = "BS.xlsx"
   # Write the DataFrame to the Excel file
        df.to_excel(file_name, sheet_name='BS.xlsx',index=False)
   

   






   



