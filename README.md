Hypothesis:

meme diffusion follows a power law.

Methodology:
Scrape Reddit for new memes and follow their evolution for an appropriate period of time (which is...?)
Try to fit it to a Power Law distribution for each memes.

TODO find out:
- appropriate length of time to monitor memes
- appropriate number of memes
- appropriate poll time for new stats about tracked memes

Data scraping:

1. query Reddit for new media posts in r/dankmemes
2. save n of them for tracking
3. every k minutes, retrieve those n posts again, query each of them for
    - likes
    - dislikes
    - comments
    - upvote ratio
    - score
    - awards 
4. append to csv along with timestamp of API call

Data analysis:
1. inspect data with plots and various statistics
2. try fitting with power law

TODO investigate if Reddit API has better stuff for my goals

Findings:

- with one hour data (data_2022-05-17_22:13:17.696999.csv), only 1 in 10 memes was successfull, following a straight line in upvotes increase (with 'new' feed)
