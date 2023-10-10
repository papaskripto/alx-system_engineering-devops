#!/usr/bin/python3
""" Queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """ returns number of subreddit subscribers."""
    red_api = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    user_agent = {"User-Agent": "papaskripto"}
    req = requests.get(red_api, headers=user_agent, allow_redirects=False)
    if req.status_code == 200:
        req = req.json()
        data = req.get("data")
        sub_red = data.get("subscribers")
        return sub_red
    return 0
