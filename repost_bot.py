import praw
from db import *
from utils import get_yt_id

reddit = praw.Reddit('RepostBot')

for result in youtu_results():
    yt_id = get_yt_id(result[2])
    
