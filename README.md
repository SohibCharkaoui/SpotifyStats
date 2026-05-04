# Statify — Spotify Stats Web App

A clean, public-facing web app where anyone can log in with their Spotify account and instantly see their top 50 tracks and top 50 artists across different time ranges.

---

## Features

- Login with any Spotify account (OAuth 2.0)
- Top 50 tracks with album art
- Top 50 artists with photos and genres
- Switch between 3 time ranges: Last 4 Weeks / 6 Months / All Time
- Click any track or artist to open in Spotify
- Zero data stored — sessions expire automatically

---

## Setup

### 1. Create a Spotify App

1. Go to [developer.spotify.com/dashboard](https://developer.spotify.com/dashboard)
2. Click **Create App**
3. Fill in a name (e.g. "Statify") and description
4. Set **Redirect URI** to `http://localhost:5000/callback` (for local) or your deployed URL
5. Copy your **Client ID** and **Client Secret**

### 2. Configure Environment

```bash
cp .env.example .env
```

Edit `.env` and fill in your credentials:

```
SPOTIPY_CLIENT_ID=your_client_id_here
SPOTIPY_CLIENT_SECRET=your_client_secret_here
SPOTIPY_REDIRECT_URI=http://localhost:5000/callback
FLASK_SECRET_KEY=any_random_string_you_make_up
```

### 3. Install & Run

```bash
pip install -r requirements.txt
python app.py
```

Visit `http://localhost:5000` in your browser.

---

## Deploy Publicly (Render)

1. Push this project to a GitHub repo
2. Go to [render.com](https://render.com) and create a new **Web Service**
3. Connect your GitHub repo
4. Set the start command to: `gunicorn app:app`
5. Add your environment variables in Render's dashboard
6. Update your Spotify app's redirect URI to `https://your-app-name.onrender.com/callback`
7. Also update `SPOTIPY_REDIRECT_URI` in your Render env vars

Add gunicorn to requirements:
```
flask
spotipy
python-dotenv
gunicorn
```

---

## Project Structure

```
spotify-stats/
├── app.py              # Flask backend + Spotify OAuth logic
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variable template
├── .env                # Your credentials (never commit this!)
└── templates/
    ├── index.html      # Landing page
    └── stats.html      # Stats display page
```

---

## Tech Stack

- **Python / Flask** — Backend server
- **Spotipy** — Spotify API wrapper
- **Spotify OAuth 2.0** — User authentication
- **Vanilla HTML/CSS** — No framework needed, fast and clean
