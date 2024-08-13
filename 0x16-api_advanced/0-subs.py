#!/usr/bin/python3
"""Defining the number_of_subscribers function"""
import requests


def number_of_subscribers(subreddit):
    """Querying Reddit API and returning total number of subscribers, they are total subscribers,
    not the active subscribers, subreddit. 
    If an invalid subreddit is given, function needs to return 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {'User-Agent': 'RedditDataAnalyzer/1.0 (ALX Africa)'} 
    subreddit_data = requests.get(url,
                                  headers=headers,
                                  allow_redirects=False).json().get("data")
    if subreddit_data:
        return subreddit_data.get("subscribers")
    return 0
