import requests
import POST_access_token

base_url = 'https://api.spotify.com/v1/'


#  1. Get array of followed artists id
def get_followed_artists():
    artists_list = []
    access_token = POST_access_token.auth_code_access_token(scope='user-follow-read')
    api_call_headers = {'Authorization': 'Bearer ' + access_token}

    r = requests.get(base_url + 'me/following?type=artist&limit=50', headers=api_call_headers)
    d = r.json()

    for artist in d['artists']['items']:
        artist_id = artist['id']

        if artist_id in artists_list:
            continue
        artists_list.append(artist_id)

    return artists_list
