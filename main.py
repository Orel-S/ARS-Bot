import praw
from gtts import gTTS
import re
import os
import time

init_time = time.time()
LANGUAGE = 'en'
POST_LIMIT = 10
COMMENT_LIMIT = 20
DIRECTORY = "C:\\Users\\Orel\\PycharmProjects\\askredditbot\\Recordings\\"
FILE_EXTENSION = '.mp3'
TIME = 'day'


def comment_array(sub):
    comment_arr = []
    top_level_comments = list(sub.comments)[:COMMENT_LIMIT]
    for comment in top_level_comments:
        comment_arr.append(comment.body)
    return comment_arr



r = praw.Reddit('bot1', user_agent="AskReddit Scraper .2 by Orel")
sub_array = []
# Initial loop to establish titles and comments in array
for submission in r.subreddit('askreddit').top(TIME, limit=POST_LIMIT):
    print("Inserting the following submission into sub_array: ")
    print(submission.title)
    title_string = re.sub('\'|\?|\.|\!|\/|\;|\:|\*', '', submission.title)
    sub_array.append([title_string, comment_array(submission)])
# Second loop iterates through sub_array and creates sorted mp3 files
j = 1
audio_conversion_init_time = time.time()
for item in sub_array:
    item_start_time = time.time()
    shortened_title = re.sub('\'|\?|\.|\!|\/|\;|\:|\*', '', item[0])[ 0 : 0 + 15].rstrip()
    print("Submission " + str(j) + "/" + str(POST_LIMIT) + " in progress...")
    if not os.path.exists(DIRECTORY + shortened_title):
        os.makedirs(DIRECTORY + shortened_title)
    g = gTTS(text=item[0], lang=LANGUAGE, slow=False)
    g.save('Recordings\\' + shortened_title + '\\' + shortened_title + FILE_EXTENSION)
    k = 1
    for comment in item[1]:
        print("Comment " + str(k) + "/" + str(COMMENT_LIMIT) + " in progress...")
        shortened_comment = re.sub('\'|\?|\.|\!|\/|\;|\:|\*|\|\\n|\"', '', comment)[ 0 : 0 + 15]
        shortened_comment = (shortened_comment.replace("\n", ' ')).rstrip()
        g = gTTS(text=comment, lang=LANGUAGE, slow=False)
        if shortened_comment != '':
            g.save('Recordings\\' + shortened_title + '\\' + shortened_comment + FILE_EXTENSION)
        k += 1
    print("Elapsed time for submission " + str(j) + ": " + str((time.time() - item_start_time)) + " seconds.")
    j += 1
print("Total audio conversion time: " + str((time.time() - audio_conversion_init_time)) + " seconds.")
print("Total function time: " + str((time.time() - init_time)) + " seconds.")

