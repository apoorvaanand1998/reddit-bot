import praw
from db import youtu_results, upd_proc
from utils import get_yt_id
from yt_process import *

reddit = praw.Reddit('RepostBot')


for result in youtu_results():
    sub_id = result[0]
    yt_id = get_yt_id(result[2])
    if post_yt_result(sub_id, get_yt_result(yt_id)):
        upd_proc(sub_id)

