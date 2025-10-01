import streamlit as st
from download import download_video, download_playlist

st.set_page_config(page_title="YouTube Video Downloader", layout='wide')
st.title("📥 YouTube Video / Playlist Downloader")

url = st.text_input("Enter YouTube video or playlist URL:")

if st.button("Download"):

    if "playlist" in url:
        st.info("Downloading playlist...")
        playlist_info = download_playlist(url)
        st.success(f"Playlist: {playlist_info['playlist_title']} downloaded!")

        for vid in playlist_info["videos"]:
            st.write(f"{vid['title']} | {vid['file_size_mb']:.2f} MB")
    else:

        st.info("Downloading video...")
        vid = download_video(url)
        st.success(f"Downloaded: {vid['title']}")
        st.write(f"Views: {vid['views']}")
        st.write(f"File Size: {vid['file_size_mb']:.2f} MB")
        st.write(f"Saved to: {vid['filepath']}")




