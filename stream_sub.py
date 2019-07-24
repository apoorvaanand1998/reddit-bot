import praw
from db import *

create_table()

reddit = praw.Reddit("AA")

for submission in reddit.subreddit("AABotTesting").stream.submissions():
    insert_sub(submission.id, submission.is_self, submission.url, submission.permalink)

    if submission.is_self:
        upd_proc(submission.id)
