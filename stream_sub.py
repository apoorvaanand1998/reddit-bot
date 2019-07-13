import praw
from db import *

create_table()

reddit = praw.Reddit('RepostBot')

for submission in reddit.subreddit('AABotTesting').stream.submissions():
    insert_sub(submission.id, submission.is_self, submission.url, submission.permalink)

    
