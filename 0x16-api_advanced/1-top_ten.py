#!/usr/bin/python3
"""Script to retrieve and display the titles of the top 10 hot posts from a subreddit using Reddit's API."""
import requests

def fetch_top_ten_posts(subreddit_name):
    """
    Retrieve and print the titles of the top 10 hot posts for a given subreddit.

    Args:
        subreddit_name (str): The name of the subreddit to query.
    """
    reddit_url = f"https://www.reddit.com/r/{subreddit_name}/hot.json"
    custom_headers = {
        'User-Agent': 'UniqueUserAgent/2.0 (Contact: example@domain.com)'
    }
    query_params = {'limit': 10}  # Retrieve only the top 10 posts

    try:
        response = requests.get(reddit_url, headers=custom_headers, params=query_params, timeout=5)
        response.raise_for_status()
        hot_posts = response.json().get('data', {}).get('children', [])

        if not hot_posts:
            print("No hot posts found.")
        else:
            for post in hot_posts:
                post_title = post.get('data', {}).get('title', 'Untitled')
                print(post_title)
    except (requests.RequestException, ValueError) as error:
        print(f"Failed to fetch data: {error}")

