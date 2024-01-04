A simple YouTube web scraper using Python with BeautifulSoup for extracting video information and downloading videos. 
This script will enable you to store video info and download videos in the highest resolution available. 

The provided Python code utilizes BeautifulSoup and pytube libraries for web scraping YouTube video information and downloading videos in high resolution.

Scraping Video Information:

The scrape_youtube function sends a request to a YouTube search results page and uses BeautifulSoup to extract video details such as title and link.
The extracted information is stored in a list of dictionaries called video_data.
Saving Video Information to JSON:

The extracted video information is then written to a JSON file named videos.json using the json.dump function.
Downloading Videos:

The download_videos function utilizes the pytube library to download videos in the highest resolution available.
Videos are saved in a folder named 'downloads'.
Usage:

Modify the url variable with your desired YouTube search query.
Ensure you have installed the required libraries (beautifulsoup4 and pytube) using pip install beautifulsoup4 pytube.

