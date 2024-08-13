!/usr/bin/python3
"""Defining a recurse function"""
import requests


def get_title(children):
    """Returning children's title"""
    return children.get("data").get("title")


def recurse(subreddit, hot_list=[], after=None):
    """
    Query Reddit API, return list that contains titles of
    all hot articles for a given subreddit.
    - If no results are found for given subreddit,
    the function should return None
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x016.project:v1.0.0 (by /u/ecalvoc)"
        }
    params = {"limit": 100}
    if after:
        params["after"] = after

    hot_data = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False).json().get("data")
    if not hot_data:
        return

    child = hot_data.get("children")
    hot_list.extend(list(map(get_title, child)))

    after = hot_data.get("after")
    if not after:
        return hot_list
    return recurse(subreddit, hot_list, after)
