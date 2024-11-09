from dotenv import load_dotenv
import os
import requests

load_dotenv()
api_key = os.getenv("API_KEY")


def get_channel_id(channel_name):
  params = {
    'part': 'snippet',
    'forHandle': channel_name,
    'maxResults': 1,
    'key': api_key
  }
  response = requests.get('https://www.googleapis.com/youtube/v3/channels', params=params)
  items = response.json().get('items')
  if items:
    title = items[0]['snippet']['title']
    pfp = items[0]['snippet']['thumbnails']['default']['url']
    channel_id = items[0]['id']
    return title, pfp, channel_id



def get_upcoming_stream(channelId):
  params = {
    'part': 'snippet',
    'channelId': channelId, 
    'eventType': 'upcoming',
    'type': 'video',
    'key': api_key
  }
  response = requests.get('https://www.googleapis.com/youtube/v3/search', params=params)
