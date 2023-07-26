
import streamlit as st
import pandas as pd
import os


df_songs = pd.read_csv(r"songs_transformed_2023-07-24 19_11_08.262787.csv")
df_albums = pd.read_csv(r"album_transformed_2023-07-24 19_11_08.537227.csv")
df_artists = pd.read_csv(r"artist_transformed_2023-07-24 19_11_08.582112.csv")

# Changing the index to start from 1 instead of 0 in the dataframe
df_songs.index += 1
df_albums.index += 1
df_artists.index += 1


chart_type = st.sidebar.selectbox("Select Chart Type", ['Top Songs', 'Top Albums', 'Top Artists'])

chart_data = {
    'Top Songs': df_songs,
    'Top Albums': df_albums,
    'Top Artists': df_artists
}

if chart_type in chart_data:
    st.title(chart_type)
    st.write(chart_data[chart_type])





# Footer
st.markdown("---")
st.markdown("\U0001F4AA by vijay krishna chilukuri")
st.markdown("© All rights reserved to the person who \U00002764 me.")
