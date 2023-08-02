from Beautifulsoup import Beautifuloupclasse
link='https://www.infraxcode.com/fournisseur-de-solutions-dautomatisation/'
b=Beautifuloupclasse(link)
b.createExcelSheet()
#the 2st library file
from Selenium import Selenuimclass
s=Selenuimclass(link)
s.createExcelSheet()