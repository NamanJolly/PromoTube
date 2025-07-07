import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")

def get_video_description(video_url):
    video_id = video_url.split("v=")[-1].split("&")[0]
    url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    if not data["items"]:
        return None
    return data["items"][0]["snippet"]["description"]
