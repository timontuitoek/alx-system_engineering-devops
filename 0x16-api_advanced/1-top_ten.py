#!/usr/bin/python3

"""
This script queries the Reddit API.
"""

import requests


def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'your_custom_user_agent'}

    try:
        response = requests.get(url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response and extract post titles
            data = response.json()
            posts = data['data']['children'][:10]  # Extract the first 10 posts

            if not posts:
                print("No hot posts found.")
            else:
                print(f"Top 10 hot posts in r/{subreddit}:\n")
                for post in posts:
                    title = post['data']['title']
                    print(f"• {title}")
        elif response.status_code == 404:
            # Subreddit not found, print None
            print(None)
        else:
            # Other error, print None
            print(None)

    except Exception as e:
        print(f"An error occurred: {e}")
        print(None)


if __name__ == "__main__":
    # Example usage:
    subreddit_name = 'python'
    top_ten(subreddit_name)
