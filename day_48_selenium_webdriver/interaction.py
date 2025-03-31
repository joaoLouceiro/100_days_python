from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

driver.find_element(By.NAME, "fName").send_keys("nana")
driver.find_element(By.NAME, "lName").send_keys("pipi")
driver.find_element(By.NAME, "email").send_keys("nanan@pipi.com")
driver.find_element(By.TAG_NAME, "form").submit()




driver.quit()
