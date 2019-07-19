import praw
import time

def get_yt_result(yt_id):
    reddit = praw.Reddit('RepostBot')
    comment = ['Anyone seeking more info might also check here:\n',
               'title | points | age | /r/ | comnts',
               ':--|:--|:--|:--|:--']
    for submission in reddit.subreddit('all').search('url:'+yt_id, limit=5):
        comment.append('[' + submission.title + '](http://www.reddit.com' +
                       submission.permalink+') | ' + str(submission.score)
                       + ' | ' + str(time.time() - submission.created_utc) +
                       ' | ' + submission.subreddit.display_name + ' | ' +
                       str(submission.num_comments))
    comment.append('I am a bot bleep bloop. These results have been ' + 
                        'brought to you by the Reddit API.\n')
    comment = '\n'.join(comment)
    # print(comment)
    return comment
            
def post_yt_result(sub_id, res):
    reddit = praw.Reddit('RepostBot')
    submission = reddit.submission(id=sub_id)
    try:
        submission.reply(res)
        return True
    except:
        return False
