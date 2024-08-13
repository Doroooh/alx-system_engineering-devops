#!/usr/bin/python3
#!/usr/bin/python3
"""A script to fetch the subscriber count of a specified subreddit using Reddit's API."""
import requests

def get_subreddit_subscribers(subreddit_name):
    """
    Fetch and return the number of subscribers for a given subreddit.

    Args:
        subreddit_name (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is not found.
    """
    reddit_url = f"https://www.reddit.com/r/{subreddit_name}/about.json"
    custom_headers = {
        'User-Agent': 'CustomAgent/1.1 (Contact: example@example.com)'
    }

    try:
        response = requests.get(reddit_url, headers=custom_headers, timeout=5)
        response.raise_for_status()
        subreddit_data = response.json().get('data', {})
        return subreddit_data.get('subscribers', 0)
    except (requests.RequestException, ValueError):
        return 0
