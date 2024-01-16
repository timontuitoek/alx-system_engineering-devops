#!/usr/bin/python3

"""
This script queries the Reddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Get the number of subscribers for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'your_custom_user_agent'}

    try:
        response = requests.get(url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response and extract the number of subscribers
            data = response.json()
            subscribers_count = data['data']['subscribers']
            return subscribers_count
        elif response.status_code == 404:
            # Subreddit not found, return 0
            return 0
        else:
            # Other error, return 0
            return 0

    except Exception as e:
        print(f"An error occurred: {e}")
        return 0


if __name__ == "__main__":
    # Example usage:
    subreddit_name = 'python'
    subscribers_count = number_of_subscribers(subreddit_name)
    print(f"The number of subscribers in r/{subreddit_name}:
          {subscribers_count}")
