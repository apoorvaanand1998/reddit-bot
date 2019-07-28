import praw
from db import youtu_results, upd_proc, img_results
from utils import get_yt_id
from yt_process import *
from kd_process import *

reddit = praw.Reddit("RepostBot")

for result in youtu_results():
    sub_id = result[0]
    yt_id = get_yt_id(result[2])
    res = get_yt_result(yt_id)
    if res:
        post_result(sub_id, res)
    upd_proc(sub_id)

for result in img_results():
    sub_id = result[0]
    permalink = result[3]
    res = get_kd_result(permalink)
    if res:
        post_result(sub_id, str(res))
    upd_proc(sub_id)

