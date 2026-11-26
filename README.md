# spotify
# 🎵 Spotify Analytics Dashboard

A professional Business Intelligence and Data Analytics platform built with **Python**, **Pandas**, **Plotly**, and **Streamlit** to explore and analyze more than **600,000 Spotify tracks**.

This project transforms raw Spotify data into interactive dashboards that help users discover music trends, top artists, popular songs, and key streaming insights.

---

## 🚀 Features

### 📊 Executive Dashboard
- Total Tracks Overview
- Total Artists
- Total Albums
- Average Popularity Score
- Dataset Health Metrics
- Interactive KPIs

### 🎤 Artist Analytics
- Top 100 Artists by Popularity
- Most Productive Artists
- Artist Popularity Distribution
- Artist Ranking System

### 🎶 Song Analytics
- Top 200 Songs
- Top 300 Songs Interactive Table
- Most Popular Tracks
- Track Popularity Trends

### 📈 Popularity Analysis
- Popularity Histogram
- Popularity Distribution
- Popular vs Non-Popular Songs
- Trend Analysis

### 🔍 Advanced Filtering
Users can filter data by:

- Artist
- Song
- Album
- Release Year
- Popularity Range
- Genre (if available)

### 📉 Interactive Visualizations
Built using Plotly:

- Bar Charts
- Line Charts
- Histograms
- Pie Charts
- Scatter Plots
- Heatmaps

---

# 🏗️ Project Structure

```
spotify/
│
├── app.py
│
├── data/
│   └── tracks.csv
│
├── level1_data_preparation/
│   ├── data_cleaning.py
│   └── feature_engineering.py
│
├── level2_dashboard/
│   ├── home_dashboard.py
│   ├── music_explorer.py
│   └── audio_analysis.py
│
├── requirements.txt
│
└── README.md
```

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Core Development |
| Pandas | Data Processing |
| NumPy | Numerical Operations |
| Plotly | Interactive Visualizations |
| Streamlit | Web Interface |
| Matplotlib | Additional Charts |
| Seaborn | Statistical Graphs |

---

# 📦 Installation

Clone the repository:

```bash
git clone https://github.com/zizou505/spotify.git
cd spotify
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

### Linux / MacOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

Start the Streamlit dashboard:

```bash
streamlit run app.py
```

The application will open automatically in:

```
http://localhost:8501
```

---

# 📊 Dataset Information

Dataset contains approximately:

- 600,000 Spotify Tracks
- Artist Information
- Album Information
- Release Dates
- Popularity Scores
- Audio Metadata

Example fields:

| Column | Description |
|----------|----------|
| id | Track ID |
| name | Track Name |
| artists | Artist Name |
| album_name | Album |
| release_date | Release Date |
| popularity | Spotify Popularity Score |
| duration_ms | Song Duration |

---

# 🎯 Business Objectives

The dashboard helps answer questions such as:

- Who are the most popular artists?
- Which songs dominate Spotify popularity rankings?
- How does popularity evolve over time?
- What characteristics define successful tracks?
- Which artists produce the highest number of songs?

---

# 📸 Dashboard Preview

### Home Dashboard
- KPI Cards
- Top Artists
- Top Songs
- Dataset Summary

### Analytics Dashboard
- Popularity Analysis
- Trend Exploration
- Artist Rankings
- Song Rankings

### Interactive Filters
- Real-time filtering
- Dynamic visual updates

---

# 🔮 Future Improvements

- Recommendation Engine
- Machine Learning Popularity Prediction
- Genre Analytics
- Real-time Spotify API Integration
- User Authentication
- Export Reports (PDF/Excel)

---

# 👨‍💻 Author

**Mohamed Aziz Mejri**

Data Analytics & Business Intelligence Project

GitHub:
https://github.com/zizou505

---

# 📄 License

This project is intended for educational and portfolio purposes.