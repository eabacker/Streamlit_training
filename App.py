import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Stel de pagina-instellingen in
st.set_page_config(page_title="Verkoop Dashboard", layout="wide")

# Lees het CSV-bestand in
df = pd.read_csv('exclusieve_schoenen_verkoop_met_locatie.csv')

# Zet de maand om naar datetime formaat (zorg ervoor dat de kolom "Maand" in de juiste indeling is)
df['maand'] = pd.to_datetime(df['aankoopdatum'], format='ISO8601')

# Maak een mooie titel voor de pagina
st.markdown(
    """
    <h1 style='text-align: center; color: #F5F5DC;'>Verkoop Analyse Dashboard 2024</h1>
    """, unsafe_allow_html=True)

# Zet de pagina op met een donkergrijze achtergrond en creme kleurige tekst
st.markdown(
    """
    <style>
    body {
        background-color: #2f2f2f;
        color: #F5F5DC;
    }
    </style>
    """, unsafe_allow_html=True)

# Multiselect om op locaties te filteren
locaties = df['Locatie'].unique()
selected_locaties = st.multiselect('Selecteer Locaties:', locaties, default=locaties)

# Filter de data op de geselecteerde locaties
filtered_df = df[df['Locatie'].isin(selected_locaties)]

# Lijn grafiek voor verkopen per merk over de maanden
fig, ax = plt.subplots(figsize=(12, 6))

# Groepeer de data per merk en maand
df_grouped = filtered_df.groupby(['Maand', 'Merk'])['Verkoop'].sum().reset_index()

# Maak de lijnen voor elk merk met pastelkleuren
merken = df_grouped['Merk'].unique()

# Pas pastelkleuren toe op de lijnen
colors = plt.cm.Pastel1.colors  # Je kunt hier andere pastelpaletten gebruiken

for i, merk in enumerate(merken):
    merk_data = df_grouped[df_grouped['Merk'] == merk]
    ax.plot(merk_data['Maand'], merk_data['Verkoop'], label=merk, color=colors[i % len(colors)])

# Zet de titel en labels
ax.set_title('Verkopen per Merk Over de Maanden in 2024', fontsize=14)
ax.set_xlabel('Maanden', fontsize=12)
ax.set_ylabel('Verkoop', fontsize=12)

# Draai de x-as labels om ze beter leesbaar te maken
plt.xticks(rotation=45)
ax.legend(title='Merken')

# Toon de grafiek in Streamlit
st.pyplot(fig)
