import requests
from bs4 import BeautifulSoup

class Scrapper:
    def __init__(self, url, headers=None):
        if headers is None:
            headers = {}
        web_page = requests.get(url, headers=headers).text
        self.scrapper = BeautifulSoup(web_page, "html.parser")

    def scrape_tracks(self) -> list:
        scraped_tracks = self.scrapper.find_all(name="div", class_="o-chart-results-list-row-container")
        tracks = []
        for row in scraped_tracks:
            li = row.find(name="li", class_="lrv-u-width-100p")
            track_name = li.find(name="h3", id="title-of-a-story").getText().replace("\n", "").replace("\t", "")
            artist = li.find(name="span", class_="c-label").getText().replace("\n", "").replace("\t", "")
            tracks.append({"artist": artist, "name": track_name})

        return tracks