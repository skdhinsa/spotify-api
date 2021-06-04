import requests
import POST_access_token
from secrets import user_id, new_playlist_id


def create_playlist(playlist_name):
    access_token = POST_access_token.auth_code_access_token(scope='playlist-modify-public')
    api_call_headers = {'Authorization': 'Bearer ' + access_token, 'Content-Type': 'application/json'}
    base_url = 'https://api.spotify.com/v1/'
    r = requests.post(base_url + 'users/{user_id}/playlists'.format(user_id=user_id), json={'name': '{}'.format(playlist_name)},
                      headers=api_call_headers)
    return r.json()


def add_song_to_playlist(track):
    access_token = POST_access_token.auth_code_access_token(scope='playlist-modify-public')
    api_call_headers = {'Authorization': 'Bearer ' + access_token, 'Content-Type': 'application/json'}
    base_url = 'https://api.spotify.com/v1/'
    params = {
        "uris": [
            "{}".format(track)
        ]
    }
    r = requests.post(base_url + 'playlists/{}/tracks'.format(new_playlist_id), json=params,
                      headers=api_call_headers)
    return r.json()

