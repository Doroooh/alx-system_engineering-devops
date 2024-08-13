#!/usr/bin/python3

""" This function counts words in the hot posts for given Reddit subreddits."""

def count_words(subreddit, word_list, word_count={}, after=None):
    """
    Function to query the Reddit API and count occurrences of words 
    in the provided word_list within the titles of all hot posts in a subreddit.

    :param subreddit: The name of the subreddit to search within
    :param word_list: A list of words to count in the titles of hot posts
    :param word_count: A dictionary to store the count of each word, initialized as an empty dictionary
    :param after: The 'after' parameter for pagination through Reddit's API, defaults to None
    :return: Prints word counts sorted by frequency and alphabetically; 
             or recursively calls itself to process the next page if needed
    """
    
    # Import requests library to handle HTTP requests
    import requests

    # Construct the Reddit API URL to fetch hot posts from the specified subreddit
    sub_info = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            params={"after": after},  # Handle pagination with 'after'
                            headers={"User-Agent": "My-User-Agent"},  # Custom User-Agent to avoid 429 errors
                            allow_redirects=False)  # Prevent redirects, ensuring we stay on the target subreddit
    
    # Checking if API request was successful (status code 200)
    if sub_info.status_code != 200:
        return None  # Return None if the request fails

    # Parsing JSON response from Reddit API
    info = sub_info.json()

    # Extracting titles of hot posts from JSON data
    hot_l = [child.get("data").get("title")
             for child in info
             .get("data")
             .get("children")]
    
    # If no titles found, return None
    if not hot_l:
        return None

    # Removing duplicate words from the word_list using dict.fromkeys
    word_list = list(dict.fromkeys(word_list))

    # Initializing word_count dictionary if empty
    if word_count == {}:
        word_count = {word: 0 for word in word_list}

    # Iterating through every title in the list of hot post titles
    for title in hot_l:
        split_words = title.split(' ')  # Split the title into individual words
        for word in word_list:
            for s_word in split_words:
                # Compare each word in the title with words in word_list (case-insensitive)
                if s_word.lower() == word.lower():
                    word_count[word] += 1  # Increment the count for each match

    # Check if there's a 'next page' (pagination) available in the data
    if not info.get("data").get("after"):
        # Sort and print the word counts first alphabetically, then by frequency
        sorted_counts = sorted(word_count.items(), key=lambda kv: kv[0])  # Sort alphabetically by word
        sorted_counts = sorted(word_count.items(),
                               key=lambda kv: kv[1], reverse=True)  # Sort by frequency (highest first)
        # Print out the results where the word count is not zero
        [print('{}: {}'.format(k, v)) for k, v in sorted_counts if v != 0]
    else:
        # If more pages are available, recursively call count_words with the 'after' parameter
        return count_words(subreddit, word_list, word_count,
                           info.get("data").get("after"))
