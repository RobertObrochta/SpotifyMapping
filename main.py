
import sys
import requests, json
import base64
import webbrowser

client_id = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
client_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

class SpotifyAPI(object):
    access_token = None
    client_id = None
    client_secret = None
    auth_code = None
    print("This project requests that you allow access to read your data. Accept this to proceed. You will be redirected to a website. \n\n")
    auth_url = "https://accounts.spotify.com/en/authorize?client_id=xxxxxxxxxxxxxxxxxxxxxxxxxxxx&scope=user-read-recently-played&response_type=code&show_dialog=true&redirect_uri=https%3A%2F%2Fdeveloper.spotify.com%2Fdocumentation%2Fweb-api%2Freference%2Fplayer%2Fget-recently-played%2F"
    webbrowser.open_new_tab(auth_url)
    token_url = "https://accounts.spotify.com/api/token"
    hist_url = "https://api.spotify.com/v1/me/player/recently-played?limit=50"
    
    def __init__(self, client_id, client_secret, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_id = client_id
        self.client_secret = client_secret

# returns a b64 encoded string
    def get_client_creds(self):
        client_id = self.client_id
        client_secret = self.client_secret
        if client_secret == None or client_id == None:
            raise Exception("client_id and cliet_secret are both required. ")
        client_creds = f"{client_id}:{client_secret}"
        client_creds_b64 = base64.b64encode(client_creds.encode())
        return client_creds_b64.decode()

    def get_token_headers(self):
        client_creds_b64 = self.get_client_creds()
        return {
            "Authorization": f"Basic {client_creds_b64}"
        }
    
    def place_auth_code(self):
        auth_code = input("Once accepted and redirected, scroll through the url to find a section that starts with 'code = '. \nCopy and paste that content here:\n--> ")
        return auth_code

    def get_token_data(self):
        auth_code = self.place_auth_code()
        return {
    "grant_type" : "authorization_code",
    "code" : f"{auth_code}",
    "redirect_uri" : "https://developer.spotify.com/documentation/web-api/reference/player/get-recently-played/"
    }

    def do_token(self):
        token_url = self.token_url
        token_data = self.get_token_data()
        token_headers = self.get_token_headers()
        req2 = requests.post(token_url, data = token_data, headers = token_headers)

        if req2.status_code not in range(200, 299):
            return False
        data = req2.json()
        access_token = data['access_token']
        self.access_token = access_token
        return True

    def get_playback_headers(self):
        access_token = self.access_token
        return {
    "Authorization" : f"Bearer {access_token}"
}

# all playback information as json
    def get_playback(self):
        hist_url = self.hist_url
        hist_headers = self.get_playback_headers()
        final_req = requests.get(hist_url, headers = hist_headers)
        history = final_req.json()
        self.history = history
        return True

# function to get parse out the info I want, and print it out line by line
    def artist_track_name(self):
        for i in range(len(spotify.history['items'])):
            track_name = spotify.history['items'][i]['track']['name']
            artist_name = spotify.history['items'][i]['track']['artists'][0]['name']
            print(artist_name + ' - ' + track_name + '\n')


spotify = SpotifyAPI(client_id, client_secret)
spotify.do_token()
spotify.get_playback()
spotify.artist_track_name()