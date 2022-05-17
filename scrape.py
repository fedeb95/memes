from datetime import datetime as dt
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
    limit = 10
    reddit_time = 'hour' # hour, year, etc...
    view = 'hot' #rising, new, ...

    headers = {'User-agent': 'Firefox'}

    # First get which posts to track
    res = requests.get(f'https://www.reddit.com/r/dankmemes/{view}.json?limit={limit}&t={reddit_time}', headers=headers).json()

    tracked = [ p['data']['name']  for p in res['data']['children'] ]

    timestamp = str(dt.now()).replace(' ', '_')
    with open(f'data_{timestamp}.csv', 'w') as file:
        file.write('time;name;upvotes;downvotes;upvote_ratio;score\n')
        while True:
            timestamp = str(dt.now())
            print(f"{timestamp} | Collecting {tracked}")
            for post in tracked:
                res = requests.get(f'https://www.reddit.com/by_id/{post}.json', headers=headers)
                child = res.json()['data']['children'][0]
                appendRow(file, child['data'], timestamp);
            time.sleep(1)

if __name__=='__main__':
    main()
