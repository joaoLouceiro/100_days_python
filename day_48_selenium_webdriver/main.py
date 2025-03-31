import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(4)

gdrp_button = driver.find_element(By.CLASS_NAME, "fc-button")
if gdrp_button is not None:
    gdrp_button.click()

time.sleep(2)
lang_button = driver.find_element(By.CLASS_NAME, "langSelectButton")
if lang_button is not None:
    lang_button.click()

big_cookie = driver.find_element(By.ID, "bigCookie")
cookie_count = driver.find_element(By.ID, "cookies")
time.sleep(2)

while time.time() < time.time() + 60 * 5:
    big_cookie.click()
    products = driver.find_element(By.ID, "products").find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")
    store= driver.find_element(By.ID, "upgrades").find_elements(By.CSS_SELECTOR, ".crate.upgrade.enabled")

    if store:
        for el in store:
            el.click()
    if products:
        for el in products:
            el.click()


driver.quit() # termina o web browser