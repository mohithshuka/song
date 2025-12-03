import streamlit as st
from ytmusicapi import YTMusic

yt = YTMusic()

st.set_page_config(page_title="Music App 🎶", layout="wide")
st.title("🎵 My  Music App")
st.caption("Created by Mohith Shuka")
query = st.text_input("Search any song...")

if query:
    results = yt.search(query, filter="songs")

    for song in results[:5]:
        title = song.get('title')
        artist = song['artists'][0].get('name')
        video_id = song.get('videoId')
        thumbnail = song.get('thumbnails', [{}])[-1].get('url')

        # Layout
        col1, col2 = st.columns([1, 2])

        with col1:
            if thumbnail:
                st.image(thumbnail, width=150)

        with col2:
            st.subheader(f"{title} - {artist}")
            st.video(f"https://www.youtube.com/watch?v={video_id}")

        st.markdown("---")
