#!/usr/bin/python3
""" Queries the Reddit API and returns a list containing the titles
of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """ Returns a list containing the titles of
    all hot articles for a given subreddit.
    """
    red_api = "https://www.reddit.com/r/{}/hot.json?after={}".format(
            subreddit, after)
    user_agent = {"User-Agent": "papaskripto"}
    if subreddit is None or type(subreddit) is not str:
        return None
    req = requests.get(
            red_api,
            headers=user_agent,
            allow_redirects=False
            ).json()
    data = req.get("data")
    if data:
        child = data.get("children")
        post = req.get("post")
        for post in child:
            post_data = post.get("data")
            title = post_data.get("title")
            hot_list.append(title)
        after = data.get("after")
        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
