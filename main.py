import praw
from gtts import gTTS
import re
import os


def comment_array(sub):
    comment_arr = []
    top_level_comments = list(sub.comments)[:25]
    for comment in top_level_comments:
        comment_arr.append(comment.body)
    return comment_arr


language = 'en'
r = praw.Reddit('bot1', user_agent="AskReddit Scraper .2 by Orel")
sub_array = []
for submission in r.subreddit('askreddit').top('month', limit=10):
    print(submission.title)
    title_string = re.sub('\'|\?|\.|\!|\/|\;|\:|\*', '', submission.title)
    sub_array.append([title_string, comment_array(submission)])
    for item in sub_array:
        shortened_title = re.sub('\'|\?|\.|\!|\/|\;|\:|\*', '', item[0])[ 0 : 0 + 15].rstrip()
        if not os.path.exists("C:\\Users\\Orel\\PycharmProjects\\askredditbot\\Recordings\\" + shortened_title):
            os.makedirs("C:\\Users\\Orel\\PycharmProjects\\askredditbot\\Recordings\\" + shortened_title)
        g = gTTS(text=item[0], lang='en', slow=False)
        g.save('Recordings\\' + shortened_title + '\\' + shortened_title + '.mp3')
        for comment in item[1]:
            shortened_comment = re.sub('\'|\?|\.|\!|\/|\;|\:|\*|\|\\n|\"', '', comment)[ 0 : 0 + 15]
            shortened_comment = (shortened_comment.replace("\n", ' ')).rstrip()
            g = gTTS(text=comment, lang='en', slow=False)
            if shortened_comment != '':
                g.save('Recordings\\' + shortened_title + '\\' + shortened_comment + '.mp3')

    

