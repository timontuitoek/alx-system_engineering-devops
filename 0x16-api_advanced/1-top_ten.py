#!/usr/bin/python3
"""
Module to interact with the Reddit API.
"""

import requests


def top_ten(subreddit):
    """
    Retrieve and print the titles of the first 10 hot posts in a subreddit.
        None
    """
    # Reddit API endpoint for getting hot posts in a subreddit
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'

    # Send a GET request to the Reddit API
    response = requests.get(url, headers={'User-agent': 'your_bot_name'})

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract and print the titles of the first 10 hot posts
        for post in data['data']['children']:
            print(post['data']['title'])
    else:
        print(None)


if __name__ == "__main__":
    # Example usage:
    subreddit_name = 'python'
    top_ten(subreddit_name)
