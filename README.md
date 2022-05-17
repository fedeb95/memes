## Abstract

Study on meme diffusions on the internet. Reddit is taken as the source for memes, and the following assumptions are made:
- a meme diffusion can be approximated with a single post diffusion (strong assumption)
- a post diffusion can be approximated with Reddit `score` value (sum of bot upvotes and downvotes)

## Hypothesis:

Meme diffusion follows a power law.

## Methodology:
Scrape Reddit for new posts and follow their evolution for an appropriate period of time (which is...?)
Try to fit it to a Power Law distribution for the most successful posts.

TODO find out:
- appropriate length of time to monitor posts
- appropriate number of posts 
- appropriate poll time for new stats about tracked posts 

### Data scraping:

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

### Data analysis:
1. inspect data with plots and various statistics
2. try fitting with power law

TODO investigate if Reddit API has better stuff for my goals

## Findings:

- with one hour data (data_2022-05-17_22:13:17.696999.csv), only 1 in 10 posts was successfull, following a straight line in upvotes increase (with 'new' feed)
- with 100 elements (data_new_100_hour_2022-05-17_23:26:35.380098.csv) but for just ten minutes, a power law seems a better fit then an exponential for the best post at the end of the tracking period 
