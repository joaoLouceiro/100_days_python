import spotipy
from spotipy.oauth2 import SpotifyOAuth

SCOPE = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE))
current_user = sp.current_user()

class Track:
    def __init__(self, artist, track):
        self.artist = artist
        self.song = track
        self.track_meta = sp.search(q=f"{artist} {track}", type="track", limit=1)
        self.id = self.track_meta['tracks']['items'][0]['id']

class PlaylistCreator:
    def __init__(self, name, track_list : list[Track]):
        self.user = current_user['id']
        self.name = name
        self.meta = sp.user_playlist_create(user=self.user, name=self.name, public=False)
        self.id = self.meta['id']
        self.track_list = track_list

    def add_tracks_to_playlist(self):
        track_ids = [t.id for t in self.track_list]
        sp.playlist_add_items(playlist_id=self.id, items=track_ids)




# print(sp.current_user())
# print()
