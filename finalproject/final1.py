from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=cedJhvVS1Wk&t=7s')


print(yt.title)

print(yt.views)

print(yt.thumbnail_url)

