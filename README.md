# Spotify Audio Analysis (1921-2020)

A Python project for exploring Spotify track data through an interactive Streamlit dashboard, data-preparation scripts, and standalone AI analysis examples.

## Dashboard features

The Streamlit app (`app.py`) has three pages:

- **Home Dashboard** — track and artist counts, average popularity, top song, top artists and songs, popularity trends, histograms, and a top-tracks table.
- **Music Explorer** — search tracks by name, filter by popularity, and view track details.
- **Audio Analysis** — explore correlations between audio features and view a histogram for a selected feature.

## Project structure

```text
.
├── app.py
├── data/
│   ├── artists.csv
│   ├── dict_artists.json
│   └── tracks.csv
├── level1_data_preparation/
│   ├── data_cleaning.py
│   └── feature_engineering.py
├── level2_dashboard/
│   ├── audio_analysis.py
│   ├── home_dashboard.py
│   └── music_explorer.py
├── level3_ai/
│   ├── ai_insights.py
│   ├── popularity_prediction.py
│   └── recommendation_system.py
├── requirements.txt
├── test_dataset.py
└── README.md
```

## Setup and run

Clone the repository and install its dependencies:

```bash
git clone https://github.com/zizou505/spotify-audio-analysis-1921-2020.git
cd spotify-audio-analysis-1921-2020
python -m venv .venv
```

Install the dependencies and start the dashboard from the repository root.
On Windows, call the virtual environment's Python directly; this avoids
PowerShell activation-policy issues.

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```

On macOS/Linux, activate the environment and run the same app:

```bash
source .venv/bin/activate
python -m pip install -r requirements.txt
streamlit run app.py
```

The app reads the track data from `data/tracks.csv`.

## Dataset inspection

Run this helper from the repository root to print the track dataset's columns and first five rows:

```bash
python test_dataset.py
```

## Level 3 AI examples

The scripts in `level3_ai/` are standalone examples; they are not dashboard pages. They expect a processed dataset at `data/processed/final_dataset.csv`, which is not included in the repository. The CSV should contain the columns used by each script: `decade`, `popularity`, `danceability`, `energy`, `tempo`, `valence`, and `acousticness`.

After providing that file, run a script from the `level3_ai` directory, for example:

```bash
cd level3_ai
python ai_insights.py
```

The other scripts can be run the same way using `popularity_prediction.py` or `recommendation_system.py`.
