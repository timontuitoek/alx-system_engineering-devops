#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API.
    """
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get
    (f"https://www.reddit.com/r/{subreddit}/about.json",
        headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    return response.json()['data']['subscribers']
