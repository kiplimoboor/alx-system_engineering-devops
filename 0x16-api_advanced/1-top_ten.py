#!/usr/bin/python3
"""Module to fetch top 10 posts from subreddit"""

import requests


def top_ten(subreddit):
    """Fetch top 10 popular posts on a subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    res = requests.get(
        url, headers={'User-Agent': 'I am the Agent'}, allow_redirects=False)
    if res.status_code == 200:
        children = res.json().get('data').get('children')
        for i in range(10):
            print(children[i].get('data').get('title'))
    else:
        print('None')
