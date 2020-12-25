import praw
import os
import requests
from frame_to_Video import convert_frames_to_video

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

reddit = praw.Reddit(client_id = CLIENT_ID,
                      client_secret = CLIENT_SECRET,
                      user_agent = "Discord Meme Bot",
                      username = "fakebot3")

def get_meme_image():
	subreddit = reddit.subreddit('memes')

	top_5 = subreddit.top(limit = 5)
	top_4 = subreddit.top(limit = 4)
	top_3 = subreddit.top(limit = 3)
	top_2 = subreddit.top(limit = 2)
	top_1 = subreddit.top(limit = 1)
	
	for submission in top_5:
	 meme_5 = submission
	 response = requests.get(meme_5.url)
	 file = open("frames/5.png", "wb")
	 file.write(response.content)
	 file.close()

	for submission in top_4:
	 meme_4 = submission
	 response = requests.get(meme_4.url)
	 file = open("frames/4.png", "wb")
	 file.write(response.content)
	 file.close()

	for submission in top_3:
	 meme_3 = submission
	 response = requests.get(meme_3.url)
	 file = open("frames/3.png", "wb")
	 file.write(response.content)
	 file.close()
	for submission in top_2:
	 meme_2 = submission
	 response = requests.get(meme_2.url)
	 file = open("frames/2.png", "wb")
	 file.write(response.content)
	 file.close()

	for submission in top_1:
	 meme_1 = submission
	 response = requests.get(meme_1.url)
	 file = open("frames/1.png", "wb")
	 file.write(response.content)
	 file.close()

#get_meme_image()

convert_frames_to_video('frames/', 'video', 1)