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

print(current_user["id"], "token saved in '.cache' file.")