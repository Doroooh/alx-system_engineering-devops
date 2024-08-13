#!/usr/bin/python3
"""
Script to retrieve the number of subscribers for a specific subreddit using the Reddit API.
"""
import requests  # Import the requests module for handling HTTP requests

def get_subscriber_count(subreddit):
    """
    Fetch and return the number of subscribers for a given subreddit.

    :param subreddit: The name of the subreddit to query
    :return: The number of subscribers, or 0 if the subreddit is not found
    """
    # Formulate the API URL to fetch subreddit details
    api_endpoint = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Define custom headers to avoid potential issues with the Reddit API
    user_agent = {'User-Agent': 'CustomClient/2.0 (Contact: developer@example.com)'}

    # Make a GET request to the Reddit API
    response = requests.get(api_endpoint, headers=user_agent, allow_redirects=False)

    # Check if the request was successful by examining the status code
    if response.status_code == 200:
        # Convert the response to a JSON object
        subreddit_info = response.json()

        # Extract the number of subscribers from the JSON data
        subscriber_count = subreddit_info.get('data', {}).get('subscribers', 0)

        return subscriber_count  # Return the number of subscribers
    else:
        return 0  # Return 0 if the subreddit is not found or the request fails

# Example usage:
# print(get_subscriber_count('learnpython'))  # Uncomment to test with 'learnpython' subreddit
