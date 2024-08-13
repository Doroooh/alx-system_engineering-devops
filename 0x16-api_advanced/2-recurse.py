#!/usr/bin/python3
"""A script to recursively fetch and return hot post titles from a subreddit using Reddit's API."""
import requests

def fetch_hot_posts(subreddit, titles_list=None, after_marker=None):
    """
    Recursively retrieve hot post titles from a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        titles_list (list): A list to accumulate hot post titles.
        after_marker (str): The marker for the next page of results.

    Returns:
        list: A list containing the titles of hot posts, or None if the request fails.
    """
    if titles_list is None:
        titles_list = []

    reddit_api_url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    user_agent_header = {'User-Agent': 'RedditScraper/2.0 (by /u/unique_user)'}
    request_params = {"limit": "100", "after": after_marker}

    try:
        response = requests.get(reddit_api_url, headers=user_agent_header, params=request_params, timeout=5)
        response.raise_for_status()

        data = response.json().get('data', {})
        posts = data.get('children', [])
        after_marker = data.get('after', None)

        for post in posts:
            titles_list.append(post['data'].get('title', 'Untitled'))

        if after_marker:
            return fetch_hot_posts(subreddit, titles_list, after_marker)
        else:
            return titles_list

    except (requests.RequestException, ValueError) as error:
        print(f"An error occurred: {error}")
        return None
