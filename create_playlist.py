import requests

#print(sys.path)
# ctrl-shift-P then command Python:select interpreter, go to python.exe file inside virtual environment path
# https://code.visualstudio.com/docs/python/environments

SPOTIFY_CREATE_PLAYLIST_URL = '	https://api.spotify.com/v1/users/kvkvk/playlists'
ACCESS_TOKEN = 'BQCA9Hti-W9g_0OOXB_b3GqAFw61J1Y5ys2KEtyEpvH7TIg9M42QQcKt-c8U4J8T49Y3alqgLfTLLLvih8ox2VJ7OAtyloFC39i3NaMPm3cynoeqaYs_kegIg1oRsZtjVkbmvquCvHYzmMjfWpp5i9Vmnh0JXVjkqBpEcO0cOhJBzqFEabtSDRN1Du6lCp-LKGciKidTSh19w-0IgCFWJVnSI6Ssg2rAgkKBbQ'

# https://developer.spotify.com/console/post-playlists/

def create_playlist_on_spotify(name, public):
    response = requests.post(
        SPOTIFY_CREATE_PLAYLIST_URL, #sending request out to the developer endpoint
        headers = {
            "Authorization": f"Bearer {ACCESS_TOKEN}" #passing in authorization details
        },
        json = {
            "name": name,
            "public" : public
        }
    )
    json_resp = response.json() # make the request (response variable) into json format

    return json_resp


def main():
    playlist = create_playlist_on_spotify(
        name = "Created Test Playlist" ,
        public = False
    )
    print(f"Playlist: {playlist}")

if __name__=='__main__':
    main()