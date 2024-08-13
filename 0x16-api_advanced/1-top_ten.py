#!/usr/bin/python3
"""
Script that interacts with the Reddit API to retrieve and display the titles of 
the top 10 hottest posts in a specified subreddit.
"""
import requests  # Import the requests library for handling HTTP requests

def display_top_ten(subreddit):
    """
    Fetch and print the titles of the top 10 hot posts from a specified subreddit.

    :param subreddit: The name of the subreddit to query
    """
    # Construct the URL for the Reddit API endpoint to get hot posts from the subreddit
    api_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    # Set up custom headers to avoid being blocked by Reddit's API for using a default User-Agent
    custom_headers = {'User-Agent': 'CustomRedditClient/1.0 (Contact: admin@example.com)'}

    # Define the query parameters to limit the number of posts returned to 10
    query_params = {'limit': 10}

    # Send a GET request to the Reddit API
    api_response = requests.get(api_url, headers=custom_headers, params=query_params,
                                allow_redirects=False)

    # Check if the request was successful by examining the status code
    if api_response.status_code == 200:
        # Parse the JSON response into a Python dictionary
        response_data = api_response.json()

        # Loop through the list of hot posts and extract their titles
        for post in response_data.get('data').get('children'):
            post_title = post.get('data').get('title')  # Retrieve the title of the post
            print(post_title)  # Output the title to the console
    else:
        # If the request was not successful, print 'None' to indicate failure
        print("None")

# Example usage:
# display_top_ten('python')  # Uncomment to test with the 'python' subreddit
