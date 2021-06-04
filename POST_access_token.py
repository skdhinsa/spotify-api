import requests, json
from pip._vendor.distlib.compat import raw_input
from secrets import client_id, client_secret, redirect_uri


def auth_code_access_token(scope):
    authorize_url = 'https://accounts.spotify.com/authorize'
    token_url = "https://accounts.spotify.com/api/token"
    authorization_redirect_url = authorize_url + '?client_id=' + client_id + '&response_type=code&scope=' + scope + '&redirect_uri=' + redirect_uri

    print("go to the following url on the browser and enter the code from the returned url: ")
    print("---  " + authorization_redirect_url + "  ---")
    authorization_code = raw_input('code: ')

    # Exchange authorization code for an access token
    payload = {'grant_type': 'authorization_code', 'redirect_uri': redirect_uri, 'code': authorization_code}
    access_token_response = requests.post(token_url, data=payload, verify=False, allow_redirects=False,
                                          auth=(client_id, client_secret))

    token = json.loads(access_token_response.text)
    # token = access_token_response.json()
    access_token = token['access_token']
    # refresh_token = tokens['refresh_token']
    return access_token


def client_cred_access_token():
    auth_url = 'https://accounts.spotify.com/api/token'
    payload = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
    }
    auth_response = requests.post(auth_url, data=payload)

    auth_response_data = auth_response.json()
    return auth_response_data['access_token']
