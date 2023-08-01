
from selenium import webdriver
from selenium.webdriver.common.by import By
#configuration te3 webdriver
from selenium.webdriver.chrome.options import Options


# Create a Chrome WebDriver instance
options = Options()
options.add_argument("--headless")
#creature d'instance "options" on l'utilise pour des différents options pour google chrome

driver = webdriver.Chrome(options=options)


# Navigate to the webpage
URL = "https://www.infraxcode.com/fournisseur-de-solutions-dautomatisation/"
driver.get(URL)
# this is the css classes for the services container
service_class_name = ".elementor-widget-wrap.elementor-element-populated"

# css selector
css_selector = f"{service_class_name} h2 a"

# Find an element by its XPath and extract its text content
elements = driver.find_elements(By.CSS_SELECTOR, css_selector)
for element in elements:
    print(element.text)
# Close the WebDriver
driver.quit()