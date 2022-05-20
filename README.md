## Abstract

Study on meme diffusions on the internet. Reddit is taken as the source for memes, and the following assumptions are made:
- a meme diffusion can be approximated with a single post diffusion (strong assumption)
- a post diffusion can be approximated with Reddit `score` value (sum of bot upvotes and downvotes)

## Hypothesis:

Meme diffusion follows a power law. That is, given a number of competing posts, success of posts can be approximated with a power law distribution.

## Methodology:
Scrape Reddit for new posts and follow their evolution for an appropriate period of time (which is...?)
Try to fit data at the end of the tracking period to a Power Law distribution.

TODO find out:
- appropriate length of time to monitor posts (trying 10h)
- appropriate number of posts (trying 100)
- appropriate poll time for new stats about tracked posts (trying every second + requests time)

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

- first result doesn't quite fit a power law, but the most successful post got a stop in increase after 3 hours. 
