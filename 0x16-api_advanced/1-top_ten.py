#!/usr/bin/python3
'''
function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
'''
from requests import get


def top_ten(subreddit):
    '''
    queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit
    '''

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    user_agent = {"USer-agent": "Google Chrome Version 80.0.4044.129"}
    params = {'limit': 10}
    url = 'http://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    response = get(url, headers=user_agent, params=params)
    results = response.json()

    try:
        new_data = results.get('data').get('children')

        for data in new_data:
            print(data.get('data').get('title'))

    except Exception:
        print("None")
