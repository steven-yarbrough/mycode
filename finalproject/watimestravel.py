#! usr/bin/env python3

import feedparser
import notify2

# Parse the RSS feed
rss_url = 'https://www.washingtontimes.com/rss/headlines/culture/travel/'
feed = feedparser.parse(rss_url)

# Get all the top stories about travel
travel_stories = [story for story in feed.entries]

# Parse the stories to an XML format
xml_stories = []
for story in travel_stories:
    xml_story = f'<title>{story.title}</title><link>{story.link}</link>'
    xml_stories.append(xml_story)

# Display the information as a desktop notification using notify2
notify2.init('Travel News')
for story in xml_stories:
    n = notify2.Notification(story.title, story.link)
    n.show()

