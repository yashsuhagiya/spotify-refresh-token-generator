import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import dotenv_values
import json

# Load configuration from .env file
config = dotenv_values(".env")

# Initialize Spotify client
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=config["SPOTIFY_CLIENT_ID"],
        client_secret=config["SPOTIFY_CLIENT_SECRET"],
        redirect_uri=config["SPOTIFY_REDIRECT_URI"],
        scope="user-read-playback-state,user-read-currently-playing",
    )
)

# Get current user information
current_user = sp.current_user()

# Ensure the current user data is not None
assert current_user is not None

# Save user data to a JSON file
with open("current_user_data.json", "w") as json_file:
    json.dump(current_user, json_file, indent=4)

print(f"Information saved in 'spotify-info.json' file.")