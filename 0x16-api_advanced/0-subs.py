#!/usr/bin/python3

""" queries the Reddit API and returns the number of subscribers"""

import requests
import sys


def number_of_subscribers(subreddit):
    """ returns the number of subscribers """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "RedditScraper/1.0"}
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        return res.json().get("data").get("subscribers")
    return 0
