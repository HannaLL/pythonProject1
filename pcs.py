
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://qasvus.wordpress.com")
driver.maximize_window()
driver.implicitly_wait(5)

print(driver.find_element(By.LINK_TEXT,"https://qasvus.wordpress.com").get_attribute("href"))
print(driver.find_element(By.LINK_TEXT,"https://qasvus.wordpress.com").get_attribute("src"))
assert "California Real Estate-QA at Silicon Valley Real Estate" in driver.title
print("California Real Estate-QA at Silicon Valley Real Estate Title is :" , driver.title)
driver.find_element(By.ID,"g2-name").send_keys("Hanna")
driver.find_element(By.ID,"g2-email").send_keys("hannaliubakova88@gmail.com")
driver.find_element(By.ID,"contact-form-comment-g2-message").send_keys("Hello")
driver.find_element(By.CLASS_NAME,"pushbutton-wide").click()
driver.find_element(By.NAME,"go back")
print(driver.find_element(By.NAME,"submit").get_attribute("type"))
