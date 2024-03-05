#!/usr/bin/python3
"""Gets subscriber count of a subreddit"""

import requests


def number_of_subscribers(subreddit):
    """
        This functions takes in a subreddit name and returns the
        subscriber count.
        If the subreddit is nonexistent, return a 0
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(
        url, headers={'User-Agent': 'kiplimoboor'}, allow_redirects=False)
    if response.status_code != 200:
        return 0
    return response.json().get('data').get('subscribers')
