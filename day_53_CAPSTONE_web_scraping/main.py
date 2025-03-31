from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from os import getenv as env
import requests
import re


URL_FORM = env("HOUSE_PRICES_SHEET")
URL_ZILLOW_CLONE = "https://appbrewery.github.io/Zillow-Clone/"

content = requests.get(URL_ZILLOW_CLONE).text

soup = BeautifulSoup(content, "html.parser")
houses = soup.find_all(name="article", class_="StyledPropertyCard-c11n-8-84")

parsed_houses = [{
    "address": house.find(name="address").getText().strip(),
    "link": house.find(name="a", class_="property-card-link").get("href"),
    "price": re.sub("[^$\d,]", "", house.find(attrs={"data-test": "property-card-price"}).get_text().split(" ")[0])
} for house in houses]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL_FORM)

wait = WebDriverWait(driver, 10)

for house in parsed_houses:
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "form")))
    form = driver.find_element(By.TAG_NAME, "form")
    fields = form.find_elements(By.CLASS_NAME, "whsOnd.zHQkBf")
    fields[0].send_keys(house["price"])
    fields[1].send_keys(house["address"])
    fields[2].send_keys(house["link"])
    driver.find_element(By.XPATH, "//span[text()='Enviar']").click()
    wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Enviar outra")))
    driver.find_element(By.PARTIAL_LINK_TEXT, "Enviar outra").click()

driver.quit()