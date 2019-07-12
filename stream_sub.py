import praw

reddit = praw.Reddit('RepostBot')

for submission in reddit.subreddit('AABotTesting').stream.submissions():
    print(submission)
