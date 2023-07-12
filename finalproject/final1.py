#! usr/bin/env python3

from pytube import YouTube
import time
from tqdm import tqdm

for i in tqdm(range(100), desc="Progress Bar"):
    time.sleep(0.009)

yt = YouTube('https://www.youtube.com/watch?v=cedJhvVS1Wk&t=7s')

#print title of YouTube video
print(yt.title)

#print how many views of video
print(yt.views)

#print a thumbnail url for referance
print(yt.thumbnail_url)

