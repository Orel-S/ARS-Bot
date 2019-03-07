import praw
r = praw.Reddit('bot1', user_agent="AskReddit Scraper .1 by Orel", )
for submission in r.subreddit('askreddit').top('day', limit=10):
    print(submission.title)
    top_level_comments = list(submission.comments)[:10]
    for comment in top_level_comments:
        print(comment.body)
