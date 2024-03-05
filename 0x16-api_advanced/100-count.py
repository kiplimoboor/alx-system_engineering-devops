#!/usr/bin/python3
"""Recursively finds all hot posts in a subreddit"""


import re

import requests


def count_words(subreddit, word_list, after='', titles=''):
    """Recursion to get all host posts in subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'
    res = requests.get(url, headers={'User-Agent': 'I'}, allow_redirects=False)
    if res.status_code != 200:
        return
    after = res.json().get('data').get('after')
    if after:
        children = res.json().get('data').get('children')
        for child in children:
            titles += child.get('data').get('title')
        count_words(subreddit, word_list, after=after, titles=titles)
    else:
        for word in word_list:
            appearances = re.findall(rf'\b{word}\b', titles, re.IGNORECASE)
            if appearances:
                print(f'{word}: {len(appearances)}')
