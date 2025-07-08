import os, requests
from dotenv import load_dotenv
import streamlit as st
api_key = st.secrets["YOUTUBE_API_KEY"]
load_dotenv()


def search_videos(query, max_results=5):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "maxResults": max_results,
        "key": api_key
    }
    resp = requests.get(url, params=params).json()
    results = []
    for item in resp.get("items", []):
        video_id = item.get("id", {}).get("videoId")
        if video_id:
            results.append((
                f"https://www.youtube.com/watch?v={video_id}",
                item["snippet"]["title"]
            ))
    return results
