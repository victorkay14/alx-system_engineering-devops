#!/usr/bin/python3
import praw

def count_words(subreddit, word_list, after=None, counts=None):
    # Initialize Reddit API connection using PRAW
    reddit = praw.Reddit(
        client_id='YOUR_CLIENT_ID',
        client_secret='YOUR_CLIENT_SECRET',
        user_agent='YOUR_USER_AGENT'
    )

    # Initialize counts dictionary if not provided
    if counts is None:
        counts = {}

    # Fetch hot articles in the subreddit
    try:
        subreddit_obj = reddit.subreddit(subreddit)
        hot_articles = subreddit_obj.hot(limit=100, params={'after': after})
    except praw.exceptions.Redirect as e:
        # Invalid subreddit or other error handling
        print(f"Invalid subreddit or error: {e}")
        return

    # Iterate through the hot articles
    for submission in hot_articles:
        # Call recursively with the next page's after parameter
        count_words(subreddit, word_list, after=submission.name, counts=counts)

        # Parse the title and count the occurrences of keywords
        title = submission.title.lower()
        for keyword in word_list:
            # Ensure the keyword is not a substring of a larger word
            if f" {keyword} " in f" {title} ":
                counts[keyword] = counts.get(keyword, 0) + 1

    # Print the results after processing all articles
    if after is None:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for keyword, count in sorted_counts:
            print(f"{keyword}: {count}")
