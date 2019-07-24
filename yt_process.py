import praw
import time
from utils import ch_epoch


def get_yt_result(yt_id):
    reddit = praw.Reddit("RepostBot")
    search_list = list(reddit.subreddit("all").search("url:" + yt_id, limit=5))
    if not search_list:
        return False  ## checks if list is empty

    comment = [
        "Anyone seeking more info might also check here:\n",
        "title | points | age | /r/ | comments",
        ":--|:--|:--|:--|:--",
    ]
    for submission in search_list:
        comment.append(
            "["
            + submission.title
            + "](http://www.reddit.com"
            + submission.permalink
            + ") | "
            + str(submission.score)
            + " | "
            + str(ch_epoch(time.time() - submission.created_utc))
            + " | "
            + submission.subreddit.display_name
            + " | "
            + str(submission.num_comments)
        )
    comment.append(
        "I am a bot bleep bloop. These results have been "
        + "brought to you by the Reddit API.\n"
    )
    comment = "\n".join(comment)
    return comment


def post_yt_result(sub_id, res):
    reddit = praw.Reddit("RepostBot")
    submission = reddit.submission(id=sub_id)
    submission.reply(res)
