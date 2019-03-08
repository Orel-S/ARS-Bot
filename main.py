import praw
from gtts import gTTS
import re


def comment_array(sub):
    comment_arr = []
    top_level_comments = list(sub.comments)[:25]
    for comment in top_level_comments:
        comment_arr.append(comment.body)
    return comment_arr


language = 'en'
r = praw.Reddit('bot1', user_agent="AskReddit Scraper .2 by Orel")
sub_array = []
for submission in r.subreddit('askreddit').top('day', limit=10):
    print(submission.title)
    title_string = re.sub('\'|\?|\.|\!|\/|\;|\:|\*', '', submission.title)
    print(title_string)
    g = gTTS(text=title_string, lang='en', slow=False)
    g.save('Recordings//' + title_string + '.mp3')
    sub_array.append([submission.title, comment_array(submission)])


    

