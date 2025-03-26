import os
import re
import requests
import bs4
import smtplib

PRICE_LIMIT = 100

with open("product_urls.txt") as url_file:
    url_list = url_file.readlines()

if url_list is None:
    print("No products on your list")
    exit(0)

html_content = requests.get(url_list[0], headers={"accept-language": "en-US,en;q=0.9","accept-encoding": "gzip, deflate, br","User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:136.0) Gecko/20100101 Firefox/136.0"}).text

soup = bs4.BeautifulSoup(html_content, "html.parser")
title = soup.find(id="productTitle").getText().strip()
price = soup.find(class_="a-section a-spacing-none aok-align-center aok-relative").getText().strip().split(" ")[0]

if float(re.sub("[^\d.]", "", price)) < PRICE_LIMIT:
    smtp = smtplib.SMTP(host=os.getenv("SMTP_HOST"), port=int(os.getenv("SMTP_PORT")))
    smtp.starttls()
    smtp.login(user=os.getenv("SMTP_MAIL"), password=os.getenv("SMTP_PASS"))
    smtp.sendmail(from_addr=os.getenv("SMTP_MAIL"), to_addrs="***REMOVED***", msg="Subject: Damn price\n\n"
                                                                                        f"A product on your wishlist is super cheap:"
                                                                                        f"{title}"
                                                                                        f"is at just {price}!".encode())
