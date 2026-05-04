# SpotifyStats

A clean, public-facing web app where anyone can log in with their Spotify account and see their top 50 tracks and top 50 artists across different time ranges.

Live site: https://spotifystats-rnbr.onrender.com

---

## How It Works

1. User visits the site and clicks "Connect with Spotify"
2. Spotify OAuth authenticates them securely
3. Their top tracks and artists are fetched and displayed
4. Nothing is stored — sessions expire automatically

---

## Access

SpotifyStats is currently in limited beta due to Spotify API restrictions for individual developers. To get access:

1. Visit https://spotifystats-rnbr.onrender.com/request-access
2. Fill out the form with your name and Spotify email
3. You will be added within 24 hours

---

## Features

- Top 50 tracks with album art
- Top 50 artists with photos and genres
- Switch between 3 time ranges: Last 4 Weeks / 6 Months / All Time
- Click any track or artist to open in Spotify
- Request access form that sends email notifications
- Zero data stored

---

## Tech Stack

- Python / Flask — Backend server
- Spotipy — Spotify API wrapper
- Spotify OAuth 2.0 — User authentication
- Formspree — Access request form emails
- Render — Cloud deployment
- Vanilla HTML/CSS — Frontend

---

## Local Development

1. Clone the repo
2. Create a Spotify app at developer.spotify.com
3. Copy .env.example to .env and fill in your credentials
4. Run: pip install -r requirements.txt
5. Run: python app.py
6. Visit: http://127.0.0.1:5000

---

## Project Structure

files/
+-- app.py
+-- requirements.txt
+-- runtime.txt
+-- .env.example
+-- templates/
    +-- index.html
    +-- stats.html
    +-- request.html
