import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# # Pagina-instellingen
# st.set_page_config(page_title="Snoepprijzen Dashboard", layout="centered")

# # 🎨 Donkere achtergrond + zachte tekstkleur via CSS
# st.markdown("""
#     <style>
#         body {
#             background-color: #1e1e1e;
#             color: #ffc4de;
#         }
#         .stApp {
#             background-color: #1e1e1e;
#         }
#         .css-18e3th9, .css-1d391kg {
#             background-color: #2e2e2e;
#             color: #ffc4de;
#         }
#         label, .stSelectbox, .stMarkdown, .stText {
#             color: #ffc4de !important;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # Titel
# st.markdown("<h1 style='color: #ffc4de;'>📈 Prijstrends van Snoepsoorten in 2024</h1>", unsafe_allow_html=True)

# # Snoepsoorten
# snoepsoorten = ["Gummy Bears", "Chocolade Repen", "Drop"]

# # Nederlandse maandafkortingen
# maanden = ["Jan", "Feb", "Mrt", "Apr", "Mei", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Dec"]

# # Genereer random prijsdata
# np.random.seed(42)
# data = []
# for snoep in snoepsoorten:
#     prijzen = np.round(np.random.uniform(0.5, 2.5, size=12), 2)
#     for maand, prijs in zip(maanden, prijzen):
#         data.append({"Snoepsoort": snoep, "Maand": maand, "Prijs (€)": prijs})

# df = pd.DataFrame(data)

# # Filter
# gekozen_snoep = st.selectbox("Selecteer een snoepsoort om te bekijken:", snoepsoorten)

# # Filter de dataframe
# filtered_df = df[df["Snoepsoort"] == gekozen_snoep]

# # Lijngrafiek
# fig, ax = plt.subplots(figsize=(12.8, 7.2))  # 1280x720 pixels
# fig.patch.set_facecolor('#1e1e1e')
# ax.set_facecolor('#2e2e2e')

# lijnkleur = '#ff69b4'
# tekstkleur = '#ffc4de'

# ax.plot(filtered_df["Maand"], filtered_df["Prijs (€)"], marker='o', color=lijnkleur, linewidth=2.5)
# ax.set_title(f"Prijsontwikkeling van {gekozen_snoep} in 2024", color=tekstkleur, fontsize=16)
# ax.set_xlabel("Maand", color=tekstkleur)
# ax.set_ylabel("Prijs (€)", color=tekstkleur)
# ax.tick_params(axis='x', colors=tekstkleur, rotation=45)
# ax.tick_params(axis='y', colors=tekstkleur)
# for spine in ax.spines.values():
#     spine.set_color(tekstkleur)

# st.pyplot(fig)


# Pagina-instellingen
st.set_page_config(page_title="Schoenenverkoop Dashboard", layout="centered")

# 🎨 Donkere stijl met zachte accentkleur
st.markdown("""
    <style>
        body {
            background-color: #1e1e1e;
            color: #ffc4de;
        }
        .stApp {
            background-color: #1e1e1e;
        }
        .css-18e3th9, .css-1d391kg {
            background-color: #2e2e2e;
            color: #ffc4de;
        }
        label, .stSelectbox, .stMarkdown, .stText {
            color: #ffc4de !important;
        }
    </style>
""", unsafe_allow_html=True)

# Titel
st.markdown("<h1 style='color: #ffc4de;'>👟 Verkoop van Schoenen per locatie in 2024</h1>", unsafe_allow_html=True)

# CSV Upload
uploaded_file = st.file_uploader("Upload hier je CSV-bestand met verkoopdata", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)

        # Vereiste kolommen checken
        vereiste_kolommen = {"Locatie", "Maand", "Verkoop"}
        if not vereiste_kolommen.issubset(df.columns):
            st.error("❌ De CSV moet deze kolommen bevatten: 'Locatie', 'Maand', 'Verkoop'")
        else:
            locaties = df["Locatie"].unique()
            gekozen_locatie = st.selectbox("Selecteer een locatie om te bekijken:", locaties)

            # Filteren op locatie
            filtered_df = df[df["Locatie"] == gekozen_locatie]

            # Zorg dat maanden in goede volgorde staan
            maand_volgorde = ["Jan", "Feb", "Mrt", "Apr", "Mei", "Jun", 
                              "Jul", "Aug", "Sep", "Okt", "Nov", "Dec"]
            filtered_df["Maand"] = pd.Categorical(filtered_df["Maand"], categories=maand_volgorde, ordered=True)
            filtered_df = filtered_df.sort_values("Maand")

            # Grafiek
            fig, ax = plt.subplots(figsize=(12.8, 7.2))
            fig.patch.set_facecolor('#1e1e1e')
            ax.set_facecolor('#2e2e2e')

            lijnkleur = '#ff69b4'
            tekstkleur = '#ffc4de'

            ax.plot(filtered_df["Maand"], filtered_df["Verkoop"], marker='o', color=lijnkleur, linewidth=2.5)
            ax.set_title(f"Verkoopcijfers in {gekozen_locatie} (2024)", color=tekstkleur, fontsize=16)
            ax.set_xlabel("Maand", color=tekstkleur)
            ax.set_ylabel("Aantal verkochte schoenen", color=tekstkleur)
            ax.tick_params(axis='x', colors=tekstkleur, rotation=45)
            ax.tick_params(axis='y', colors=tekstkleur)
            for spine in ax.spines.values():
                spine.set_color(tekstkleur)

            st.pyplot(fig)

    except Exception as e:
        st.error(f"⚠️ Er ging iets mis met het inlezen van de CSV: {e}")
else:
    st.info("⬆️ Upload een CSV-bestand met kolommen: 'Locatie', 'Maand', 'Verkoop'.")
