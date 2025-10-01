from pytubefix import YouTube, Playlist
import os

download_folder = r"C:\Users\lenovo\OneDrive\Documents\VS Code\Youtube Video Downloader"

def download_video(url):
    yt = YouTube(url)

    title = yt.title
    views = yt.views

    stream = yt.streams.get_highest_resolution()
    file_size_mb = stream.filesize / (1024 * 1024)  # Convert bytes to MB

    filepath = stream.download(download_folder)
    return {
        "title": title,
        "views": views,
        "file_size_mb": file_size_mb,
        "filepath": filepath
    }

def download_playlist(url):
    play_list = Playlist(url)
    results = []
    for video_url in play_list.video_urls:
        result = download_video(video_url)
        results.append(result)
    return {
        "playlist_title": play_list.title,
        "videos": results
    }
