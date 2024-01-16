#!/usr/bin/python3
'''
recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit, the function
should return None
'''
import requests

after = None


def recurse(subreddit, hot_list=[]):
    '''
    returns top 10 post titles recursively
    '''
    global after
    user_agent = {'User-Agent': 'api_advanced-project'}
    url = 'http://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    params = {'after': after}
    results = requests.get(url, params=params, headers=user_agent,
                            allow_redirects=False)

    if results.status_code == 200:
        after_data = results.json().get('data').get('after')
        if after_data is not None:
            after = after_data
            recursive(subreddit, hot_list)

        all_titles = results.json().get('data').get('children')
        for i in all_titles:
            hot_list.append(i.get("data").get("title"))

        return hot_list
    else:
        return (None)
