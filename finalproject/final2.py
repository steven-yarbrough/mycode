import os
import subprocess
from pytube import YouTube
import time
from tqdm import tqdm

def main():
    for i in tqdm(range(100), desc="Progress Bar"):
        time.sleep(0.009)

    yt = YouTube('https://www.youtube.com/watch?v=cedJhvVS1Wk&t=7s')

    #print title of YouTube video
    print(yt.title)

    #print how many views of video
    print(yt.views)

    #print a thumbnail url for referance
    print(yt.thumbnail_url)

    # URL of the video to be downloaded
    url = "https://www.youtube.com/watch?v=cedJhvVS1Wk&t=7s"

    # Directory where the video will be saved
    directory = "/home/student/mycode/finalproject"

    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Download the video
    os.system(f"yt-dlp -o '{directory}/%(title)s.%(ext)s' {url}")

    print("You have successfully RUN THE JEWELS...VANDAL")

    exit()

if __name__ == "__main__":
    main()

