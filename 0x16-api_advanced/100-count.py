#!/usr/bin/python3
"""Script to count occurrences of specified words in the titles of hot posts on a Reddit subreddit."""
import requests

def count_keyword_occurrences(subreddit, keywords, after_token=None, word_count=None):
    """
    Recursively count and display occurrences of specified words in hot post titles on a subreddit.

    Args:
        subreddit (str): The name of the subreddit to search.
        keywords (list): List of words to count in the titles.
        after_token (str): Token for the next page of results (for pagination).
        word_count (dict): Dictionary to store word counts.
    """
    if word_count is None:
        word_count = {}

    api_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    request_headers = {'User-Agent': 'UniqueUserAgent/3.0 (Contact: user@example.com)'}
    query_params = {'limit': 100, 'after': after_token}

    try:
        response = requests.get(api_url, headers=request_headers, params=query_params, timeout=5)
        response.raise_for_status()
        hot_posts_data = response.json().get('data', {})
        after_token = hot_posts_data.get('after', None)
        posts = hot_posts_data.get('children', [])

        for post in posts:
            title = post['data'].get('title', '').lower().split()
            for keyword in keywords:
                keyword_lower = keyword.lower()
                if keyword_lower in title:
                    occurrences = title.count(keyword_lower)
                    word_count[keyword_lower] = word_count.get(keyword_lower, 0) + occurrences

        if after_token:
            return count_keyword_occurrences(subreddit, keywords, after_token, word_count)
        else:
            if word_count:
                sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_word_count:
                    print(f"{word}: {count}")

    except (requests.RequestException, ValueError) as error:
        print(f"Error occurred: {error}")
