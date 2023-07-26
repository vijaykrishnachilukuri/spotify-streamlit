
import streamlit as st
import pandas as pd
import os


df_songs = pd.read_csv(r"D:\ISBA\capstone\songs_transformed_2023-07-19 21_05_59.102705.csv")
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


@st.cache
def create_playlist():
    playlist = []
    return playlist


@st.cache_data
def create_playlist():
    playlist = []
    return playlist

def main():
    st.title("Music Playlist Creator")

    # Create an empty playlist
    playlist = create_playlist()

    # Display song selection
    selected_songs = st.multiselect("Select a song:", df_songs['song_name'])
    add_button = st.button("Add to Playlist")

    if add_button:
        for selected_song in selected_songs:
            selected_song_details = df_songs.loc[df_songs['song_name'] == selected_song]
            playlist.append(selected_song_details)
        st.success(f"Added {len(selected_songs)} songs to the playlist!")


    # Display the playlist
    if len(playlist) > 0:
        st.subheader("Playlist")
        for song in playlist:
            st.write(song['song_name'].values[0])
            remove_button = st.button("Remove", key=song.index[0])
            if remove_button:
                playlist = [item for item in playlist if item.index[0] != song.index[0]]
    else:
        st.info("Playlist is empty.")

    
if __name__ == '__main__':
    main()



# Footer
st.markdown("---")
st.markdown("\U0001F4AA by vijay krishna chilukuri")
st.markdown("© All rights reserved to the person who \U00002764 me.")
