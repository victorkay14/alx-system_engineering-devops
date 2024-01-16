#!/usr/bin/python3

"""
Reddit API Subscribers Counter

This script queries the Reddit API and returns the number of subscribers for a given subreddit.

Usage:
    ./subreddit_subscribers.py <subreddit_name>
"""

import requests

def number_of_subscribers(subreddit):
    """
    Retrieve the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers. Returns 0 for invalid subreddits.
    """
    # Reddit API endpoint for getting subreddit information
    api_url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # Set a custom User-Agent to avoid errors related to Too Many Requests
    headers = {'User-Agent': 'CustomUserAgent'}

    try:
        # Send a GET request to the Reddit API
        response = requests.get(api_url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Extract and return the number of subscribers
            return data['data']['subscribers']
        elif response.status_code == 404:
            # If the subreddit is not found, return 0
            return 0
        else:
            # Print an error message for other status codes
            print(f"Error: {response.status_code}")
            return 0
    except Exception as e:
        # Print an error message for exceptions
        print(f"Error: {e}")
        return 0

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: ./subreddit_subscribers.py <subreddit_name>")
        sys.exit(1)

    subreddit_name = sys.argv[1]
    subscribers_count = number_of_subscribers(subreddit_name)

    if subscribers_count > 0:
        print(f"The subreddit r/{subreddit_name} has {subscribers_count} subscribers.")
    else:
        print(f"The subreddit r/{subreddit_name} is not valid or does not exist.")
