import requests
from bs4 import BeautifulSoup
import json
from pytube import YouTube 

def scrape_youtube(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    video_data = []

    for video in soup.select('.yt-simple-endpoint.style-scope.ytd-grid-video-renderer'):
        title = video.select_one('.title-and-badge style-scope ytd-video-renderer').text.strip()
        link = 'https://www.youtube.com' + video['href']
        video_data.append({'title': title, 'link': link})

    return video_data

url = 'https://www.youtube.com/results?search_query=your+search+query'
video_info = scrape_youtube(url)

with open('videos.json', 'w') as json_file:
    json.dump(video_info, json_file, indent=2)


def download_videos(video_data):
    for video in video_data:
        yt = YouTube(video['link'])
        stream = yt.streams.get_highest_resolution()
        print(f'Downloading {video["title"]}...')
        stream.download(output_path='downloads')

download_videos(video_info)
