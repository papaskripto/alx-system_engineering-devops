#!/usr/bin/python3
""" Queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """ Prints the titles of the first 10 hot posts listed
    for a given subreddit.
    """
    red_api = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    user_agent = {"User_agent": "papascripto"}
    if subreddit is None or type(subreddit) != str:
        print(None)
    req = requests.get(
            red_api,
            headers=user_agent,
            allow_redirects=False,
            params={"limit": 10}
            ).json()
    data = req.get("data")
    if data:
        children = data.get("children")
    if data is not None and children is not None:
        post = req.get("post")
        for post in children:
            post_data = post.get("data")
            title = post_data.get("title")
            print(title)
    else:
        print("None")
