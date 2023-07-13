import yt_dlp
import argparse

parser = argparse.ArgumentParser(description='Download YouTube videos using yt-dlp')
parser.add_argument('url', type=str, help='YouTube video URL')
args = parser.parse_args()

ydl_opts = {}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([args.url])
