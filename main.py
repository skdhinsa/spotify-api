import GET_followed_artists
import GET_recent_releases
import POST_access_token
import POST_playlists

#  1. Get list of followed artists
followed_artists = GET_followed_artists.get_followed_artists()
#  2. Get access token to Get recent track releases
client_cred_access_token = POST_access_token.client_cred_access_token()
recent_releases = GET_recent_releases.get_recent_releases(client_cred_access_token)

# 3. From recent releases, add any from followed artists to new playlist
for artist, track in recent_releases.items():
    if artist in followed_artists:
        POST_playlists.add_song_to_playlist(track)
