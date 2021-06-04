import requests
from secrets import discover_playlist

base_url = 'https://api.spotify.com/v1/'


def get_recent_releases(access_token):
    api_call_headers = {'Authorization': 'Bearer ' + access_token}
    r = requests.get(base_url + "playlists/{}/tracks".format(discover_playlist), headers=api_call_headers)
    d = r.json()

    releases_list = {}
    for track in d['items']:
        artist_uri = track['track']['album']['artists'][0]['id']
        track_uri = track['track']["uri"]

        if artist_uri in releases_list:
            continue
        releases_list[artist_uri] = track_uri

    return releases_list
