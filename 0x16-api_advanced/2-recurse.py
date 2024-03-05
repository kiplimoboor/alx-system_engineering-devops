#!/usr/bin/python3
"""Recursively finds all hot posts in a subreddit"""


import requests


def recurse(subreddit, hot_list=[], after=''):
    """Recursion to get all host posts in subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'
    res = requests.get(url, headers={'User-Agent': 'I'}, allow_redirects=False)
    if res.status_code != 200:
        return None
    after = res.json().get('data').get('after')
    if after:
        children = res.json().get('data').get('children')
        for child in children:
            hot_list.append(child.get('data').get('title'))
        recurse(subreddit, hot_list, after=after)
        return hot_list
