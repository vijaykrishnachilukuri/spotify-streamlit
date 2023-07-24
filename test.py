
import streamlit as st
import pandas as pd
import os

import boto3
from io import StringIO

# Create a Boto3 session
session = boto3.Session()

# Specify the S3 bucket and folder path
bucket_name = 'spotify-etl-project-vijay'
folder_path = 'path/to/your/folder/'

# Create an S3 client using the session
s3_client = session.client('s3', aws_access_key_id = 'AKIATNNGKZCO4VQVF2MD',
                           aws_secret_access_key = 'wijBUcbR17nPxuxtt252y8Vp7Ep7nogDqLXDXSbs')

# Get the list of objects in the specified folder
response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=folder_path)

buckets = s3_client.list_buckets()
# Print the names of all buckets
for bucket in buckets:
    print(bucket)



df_songs = pd.read_csv(r"D:\ISBA\capstone\songs_transformed_2023-07-19 21_05_59.102705.csv")
df_albums = pd.read_csv(r"D:\ISBA\capstone\album_transformed_2023-07-17 20_01_54.281846.csv")
df_artists = pd.read_csv(r"D:\ISBA\capstone\artist_transformed_2023-07-17 20_01_54.367685.csv")

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
