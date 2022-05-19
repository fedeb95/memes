from datetime import datetime as dt
from datetime import timedelta
import threading
import time

import requests

def appendRow(file, data, timestamp):
    name = str(data['name'])
    upvotes = str(data['ups'])
    downvotes = str(data['downs'])
    upvote_ratio = str(data['upvote_ratio'])
    score = str(data['score'])
    file.write(f'{timestamp};{name};{upvotes};{downvotes};{upvote_ratio};{score}\n')



def main():
    limit = 100
    reddit_time = 'hour' # hour, year, etc...
    feed = 'new' # feeds different from new are rounded

    headers = {'User-agent': 'Firefox'}

    # First get which posts to track
    res = requests.get(f'https://www.reddit.com/r/dankmemes/{feed}.json?limit={limit}&t={reddit_time}', headers=headers).json()

    tracked = [ p['data']['name']  for p in res['data']['children'] ]

    now = dt.now()
    end = now + timedelta(hours=10)
    timestamp = str(now).replace(' ', '_')
    with open(f'data_{feed}_{limit}_{reddit_time}_{timestamp}.csv', 'w') as file:
        file.write('time;name;upvotes;downvotes;upvote_ratio;score\n')
        while dt.now() < end:
            timestamp = str(dt.now())
            print(f"{timestamp} | Collecting {tracked}")
            for post in tracked:
                res = requests.get(f'https://www.reddit.com/by_id/{post}.json', headers=headers)
                child = res.json()['data']['children'][0]
                appendRow(file, child['data'], timestamp);
            time.sleep(1)

if __name__=='__main__':
    main()
