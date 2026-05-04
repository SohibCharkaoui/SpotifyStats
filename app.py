import os
from flask import Flask, redirect, request, session, render_template, url_for
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "supersecretkey123")

SCOPE = "user-top-read"
REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI", "http://localhost:8888/callback")

def get_spotify_oauth():
    return SpotifyOAuth(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        redirect_uri=REDIRECT_URI,
        scope=SCOPE,
        cache_handler=spotipy.cache_handler.MemoryCacheHandler()
    )

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    sp_oauth = get_spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route("/callback")
def callback():
    sp_oauth = get_spotify_oauth()
    code = request.args.get("code")
    token_info = sp_oauth.get_access_token(code)
    session["token_info"] = token_info
    return redirect(url_for("stats"))

@app.route("/stats")
def stats():
    token_info = session.get("token_info")
    if not token_info:
        return redirect(url_for("index"))

    sp_oauth = get_spotify_oauth()
    if sp_oauth.is_token_expired(token_info):
        token_info = sp_oauth.refresh_access_token(token_info["refresh_token"])
        session["token_info"] = token_info

    sp = spotipy.Spotify(auth=token_info["access_token"])

    time_range = request.args.get("time_range", "medium_term")

    user = sp.current_user()
    top_tracks = sp.current_user_top_tracks(limit=50, time_range=time_range)
    top_artists = sp.current_user_top_artists(limit=50, time_range=time_range)

    tracks = []
    for i, item in enumerate(top_tracks["items"]):
        tracks.append({
            "rank": i + 1,
            "name": item["name"],
            "artist": item["artists"][0]["name"],
            "album": item["album"]["name"],
            "image": item["album"]["images"][1]["url"] if len(item["album"]["images"]) > 1 else item["album"]["images"][0]["url"],
            "url": item["external_urls"]["spotify"]
        })

    artists = []
    for i, item in enumerate(top_artists["items"]):
        artists.append({
            "rank": i + 1,
            "name": item["name"],
            "genres": ", ".join(item["genres"][:2]) if item["genres"] else "—",
            "image": item["images"][1]["url"] if len(item["images"]) > 1 else (item["images"][0]["url"] if item["images"] else ""),
            "url": item["external_urls"]["spotify"],
            "followers": f"{item['followers']['total']:,}"
        })

    return render_template("stats.html",
        user=user,
        tracks=tracks,
        artists=artists,
        time_range=time_range
    )

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
