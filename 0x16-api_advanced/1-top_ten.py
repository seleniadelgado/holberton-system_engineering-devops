#!/usr/bin/python3
"""
Top 10 hot posts
"""
import requests


def top_ten(subreddit):
    u = ("https://www.reddit.com/r/{}/hot.json".format(subreddit))
    r = requests.get(u, headers={'User-agent': 'angie'}, allow_redirects=False)
    status = r.status_code
    if (status != 200):
        print("None")
    else:
        parent = r.json()
        parent_data = parent['data']
        children = parent_data['children']
        for index in range(10):
            if index < len(children):
                print(children[index]['data']['title'])
            else:
                return None
