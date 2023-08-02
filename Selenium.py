from selenium import webdriver
from selenium.webdriver.common.by import By
#webdriver configuration
from selenium.webdriver.chrome.options import Options
import pandas as pd

class Selenuimclass:
    def __init__(self,link):
        self.link= link
    def extractElements(self):
        options = Options()
        options.add_argument("--headless")
        #options instance
        driver = webdriver.Chrome(options=options)
        driver.get(self.link)
        # this is the css classes for the services container
        service_class_name = ".elementor-widget-wrap.elementor-element-populated" 
       # css selector
        css_selector = f"{service_class_name} h2 a"
        # Find an element by its css selector and extract its text content
        elements = driver.find_elements(By.CSS_SELECTOR, css_selector)
        return elements
    def  createExcelSheet(self):
        services=[]
        elements=self.extractElements()
        for item in elements:
          services.append({'titre':item.text})
        print(services)
        df=pd.DataFrame(services)
        file_name = "Sel.xlsx"
   # Write the DataFrame to the Excel file
        df.to_excel(file_name, sheet_name='Sel.xlsx',index=False)
   
       
