from datetime import datetime as date
import re

import spoty_manager
import track_scrapper

while not re.match("\d{4}-\d{2}-\d{2}", selected_date := input("Where do you want to travel to? YYYY-MM-DD: ")) or date.strptime(selected_date, "%Y-%m-%d") > date.now():
    print("invalid date")

selected_date =  "2025-03-29"

url = f"https://www.billboard.com/charts/hot-100/{selected_date}/"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

scrapper = track_scrapper.Scrapper(url, header)

track_list = [spoty_manager.Track(item["artist"], item["name"]) for item in scrapper.scrape_tracks()]

playlist_name = f"Top 100 tracks in {selected_date}"
pm = spoty_manager.PlaylistCreator(playlist_name, track_list)
pm.add_tracks_to_playlist()