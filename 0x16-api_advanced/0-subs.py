#!/usr/bin/python3
"""
query an API and return the number of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    u = ("https://www.reddit.com/r/{}.json".format(subreddit))
    r = requests.get(u, headers={'User-agent': 'angie'}, allow_redirects=False)
    status = r.status_code
    if (status != 200):
        return 0
    else:
        parent = r.json()
        parent_data = parent['data']
        children = parent_data['children']
        child = children[0]['data']
        sub_count = child['subreddit_subscribers']
        return sub_count
