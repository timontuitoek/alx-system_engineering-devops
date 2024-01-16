#!/usr/bin/python3

"""
This script defines a recursive function that queries the Reddit API
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively fetch hot articles for a given subreddit.
    """
    if hot_list is None:
        hot_list = []  # Initialize the list if not provided

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'your_custom_user_agent'}
    params = {'after': after} if after else {}

    try:
        response = requests.get(url, headers=headers, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']

            if not posts:
                return hot_list  # Return the final list when no more posts are available

            for post in posts:
                title = post['data']['title']
                hot_list.append(title)

            # Use recursion to fetch the next page of results
            next_after = data['data']['after']
            return recurse(subreddit, hot_list, next_after)

        elif response.status_code == 404:
            # Subreddit not found, return None
            return None
        else:
            # Other error, return None
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    # Example usage:
    subreddit_name = 'python'
    hot_articles = recurse(subreddit_name)

    if hot_articles is not None:
        print(f"All hot articles in r/{subreddit_name}:\n")
        for i, title in enumerate(hot_articles, start=1):
            print(f"{i}. {title}")
    else:
        print(None)
