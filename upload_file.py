import os 
from selenium import webdriver
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'pop.txt') 
driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/file_input.html")
fields = driver.find_elements_by_class_name("form-control")
for i in fields:
    i.send_keys("123@qwe.qwe")
driver.find_element_by_id("file").send_keys(file_path )
driver.find_element_by_class_name("btn-primary").click()