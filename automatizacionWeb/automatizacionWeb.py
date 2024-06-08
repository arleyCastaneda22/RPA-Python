from selenium import webdriver
"""
Estamos abriendo linkedin 
"""
# browser= webdriver.Chrome()

url= "https://www.linkedin.com";

# browser.maximize_window();

# browser.get(url);



opciones= webdriver.ChromeOptions()

opciones.add_experimental_option("excludeSwitches",['enable-automation'])
driver= webdriver.Chrome(options=opciones)

driver.maximize_window()
driver.get(url);