import bs4
import requests

content = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/").text


soup = bs4.BeautifulSoup(content, "html.parser")
# print(soup.prettify())
movies = soup.find_all(name="section", class_="gallery__content-item")
with open("top100.txt", "a") as file:
    for m in reversed(movies):
        file.write(m.find(name="h3", class_="title").getText())
        file.write("\n")