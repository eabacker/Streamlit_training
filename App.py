import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Streamlit pagina-instellingen
st.set_page_config(page_title="Snoepprijzen Dashboard", layout="centered")

# Titel
st.title("📈 Prijstrends van Snoepsoorten in 2024")

# Snoepsoorten
snoepsoorten = ["Gummy Bears", "Chocolade Repen", "Drop"]

# Maanden van 2024
maanden = pd.date_range(start="2024-01-01", end="2024-12-31", freq="M").strftime('%B')

# Genereer random prijsdata
np.random.seed(42)
data = []
for snoep in snoepsoorten:
    prijzen = np.round(np.random.uniform(0.5, 2.5, size=12), 2)  # random prijzen tussen 0.50 en 2.50
    for maand, prijs in zip(maanden, prijzen):
        data.append({"Snoepsoort": snoep, "Maand": maand, "Prijs (€)": prijs})

df = pd.DataFrame(data)

# Filter
gekozen_snoep = st.selectbox("Selecteer een snoepsoort om te bekijken:", snoepsoorten)

# Filter de dataframe
filtered_df = df[df["Snoepsoort"] == gekozen_snoep]

# Lijngrafiek
fig, ax = plt.subplots()
ax.plot(filtered_df["Maand"], filtered_df["Prijs (€)"], marker='o')
ax.set_title(f"Prijsontwikkeling van {gekozen_snoep} in 2024")
ax.set_xlabel("Maand")
ax.set_ylabel("Prijs (€)")
ax.tick_params(axis='x', rotation=45)

st.pyplot(fig)
