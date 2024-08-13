#!/usr/bin/python3
""" This is a module to consume Reddit API, will return list that contains titles of all hot articles for given subreddit."""
import requests

def recurse(subreddit, hot_list=[], n=0, after=None):
    """ This will query Reddit API, to return list with titles for
    all hot articles for given subreddit. 
    Reddit API utilizes pagination to separate the page responses.
    If the subreddit isn't valid, return None. 

    Args:
        subreddit (str): subreddit.
        hot_list (list, optional): the list of the article titles. Defaults to [].

    Returns:
        list: to return list of titles.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'user-agent': 'custom'}
    hawih = requests.get(url, headers=headers, allow_redirects=False)
    if hawih.status_code == 200:
        hawih = hawih.json()
        for post in hawih.get('data').get('children'):
            hot_list.append(post.get('data').get('title'))
        if hawih.get('data').get('after'):
            recurse(subreddit, hot_list)
        return hot_list
    else:
        return None
