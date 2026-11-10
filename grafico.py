import webbrowser

import pandas as pd
import plotly.express as px

artistas = [
    "Taylor Swift", "Bad Bunny", "Drake", "The Weeknd", "BTS",
    "Billie Eilish", "Ariana Grande", "Post Malone", "Dua Lipa", "Travis Scott",
]

cores = {
    "Taylor Swift": "#FF2D92",
    "Bad Bunny": "#FFD400",
    "Drake": "#00C2FF",
    "The Weeknd": "#8A2BE2",
    "BTS": "#FF6B6B",
    "Billie Eilish": "#39FF14",
    "Ariana Grande": "#FF7F50",
    "Post Malone": "#C0C0C0",
    "Dua Lipa": "#FF1493",
    "Travis Scott": "#1E90FF",
}

# Reproduções (em milhões) por artista e ano (2015-2024)
dados = {
    "Taylor Swift": [1.2, 1.5, 1.8, 2.1, 2.4, 2.8, 3.5, 4.2, 5.1, 6.3],
    "Bad Bunny": [0.2, 0.4, 0.8, 1.2, 1.8, 2.5, 3.4, 4.5, 5.8, 7.2],
    "Drake": [2.2, 2.5, 2.8, 3.0, 3.4, 3.6, 3.8, 3.9, 4.0, 4.1],
    "The Weeknd": [1.5, 1.8, 2.1, 2.5, 2.7, 2.9, 3.2, 3.5, 3.8, 4.0],
    "BTS": [1.0, 1.8, 3.0, 4.5, 4.2, 3.5, 2.8, 2.2, 1.8, 1.5],
    "Billie Eilish": [0.0, 0.0, 0.1, 0.8, 1.5, 2.2, 3.0, 3.8, 4.5, 5.0],
    "Ariana Grande": [1.2, 1.4, 1.7, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2],
    "Post Malone": [0.5, 0.8, 1.1, 1.5, 1.9, 2.3, 2.7, 3.1, 3.5, 3.9],
    "Dua Lipa": [0.3, 0.5, 0.7, 1.0, 1.4, 1.9, 2.5, 3.2, 4.0, 4.8],
    "Travis Scott": [0.8, 1.1, 1.4, 1.8, 2.1, 2.4, 2.8, 3.2, 3.6, 4.2],
}

anos = list(range(2015, 2025))

linhas = []
for artista in artistas:
    for ano, valor in zip(anos, dados[artista]):
        linhas.append({"Ano": ano, "Artista": artista, "Reproducoes": valor})

df = pd.DataFrame(linhas)

fig = px.bar(
    df,
    x="Reproducoes",
    y="Artista",
    color="Artista",
    animation_frame="Ano",
    orientation="h",
    range_x=[0, df["Reproducoes"].max() * 1.15],
    color_discrete_map=cores,
    labels={"Reproducoes": "Reproduções (milhões)", "Artista": "Artista"},
    title="Bar Chart Race — Artistas Mais Tocados (2015-2024)",
)

fig.update_traces(
    text=df["Reproducoes"].map(lambda v: f"{v:.1f}M"),
    textposition="outside",
)

fig.update_layout(
    xaxis_title="Reproduções (milhões)",
    yaxis_title="",
    height=600,
    width=1000,
    template="plotly_dark",
    legend_title_text="Artista",
)

fig.update_yaxes(autorange="reversed")

fig.write_html("artistas_mais_tocados.html")
webbrowser.open("artistas_mais_tocados.html")
