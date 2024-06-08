""""

Principales funciones

By Id
By Name 
By Xpath
By selector 
By class 

Me permite manejar el DOOM DE UNA PÁGINA WEB

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
url="https://www.linkedin.com/login/es"
user="arleycastaneda22@gmail.com"
password="Ja00002444205086"
driver.get(url)




iu='//*[@id="username"]'
ip='//*[@id="password"]'


i1=driver.find_element(By.XPATH, iu)
i2=driver.find_element(By.XPATH, ip)

i1.send_keys(user)
i2.send_keys(password)




