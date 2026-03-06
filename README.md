# Rubik's Cube Solver — Deployment Guide

## Stack
- **Backend**: Python/Flask → deployed on [Render](https://render.com) (free tier)
- **Frontend**: HTML/JS/Three.js → deployed on [Vercel](https://vercel.com) (free tier)

---

## Step 1 — Deploy the Backend on Render

1. Push the `backend/` folder to a GitHub repo (or the whole project).
2. Go to [render.com](https://render.com) → **New** → **Web Service**.
3. Connect your GitHub repo and select the **backend** folder as the root directory (or set it in the settings).
4. Render will auto-detect the settings from `render.yaml`, but confirm:
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
5. Click **Deploy**. Wait for it to go live.
6. Copy your live URL — it will look like:
   ```
   https://rubiks-solver-api.onrender.com
   ```

> ⚠️ **Free tier note**: Render free instances spin down after 15 min of inactivity.
> The first solve after idle may take ~30 seconds to wake up. This is normal.

---

## Step 2 — Update the Frontend with Your Render URL

Open `frontend/index.html` and find this line near the top of the `<script type="module">` block:

```js
const API_URL = 'https://YOUR-RENDER-APP.onrender.com/solve';
```

Replace it with your actual Render URL:

```js
const API_URL = 'https://rubiks-solver-api.onrender.com/solve';
```

Save the file.

---

## Step 3 — Deploy the Frontend on Vercel

1. Push the updated `frontend/` folder to GitHub (same or separate repo).
2. Go to [vercel.com](https://vercel.com) → **Add New Project**.
3. Import your GitHub repo. If the frontend is in a subfolder, set the **Root Directory** to `frontend/`.
4. Framework preset: **Other** (no framework needed).
5. Click **Deploy**. Done!

Your app will be live at something like:
```
https://rubiks-cube-solver.vercel.app
```

---

## Project Structure

```
rubiks-cube-web/
├── backend/
│   ├── app.py            ← Flask API (PORT-aware for Render)
│   ├── requirements.txt  ← includes gunicorn
│   ├── Procfile          ← gunicorn start command
│   ├── render.yaml       ← Render auto-config
│   └── runtime.txt       ← Python 3.11
└── frontend/
    ├── index.html        ← Full app (update API_URL here)
    ├── Rubik.png         ← Favicon
    └── vercel.json       ← SPA routing rewrite
```

---

## Troubleshooting

| Problem | Fix |
|---|---|
| "Failed to fetch" on solve | Check API_URL in index.html matches your Render URL exactly |
| Solve takes ~30s first time | Normal — Render free tier cold start. Subsequent calls are fast. |
| CORS error in browser console | Make sure `flask-cors` is installed and `CORS(app)` is in app.py |
| Render deploy fails | Check that root directory is set to `backend/` in Render settings |
