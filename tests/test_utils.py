import pytest
from utils import *


def test_ch_epoch():
    assert ch_epoch(1) == "1 second"
    assert ch_epoch(2) == "2 seconds"
    assert ch_epoch(60) == "1 minute"
    assert ch_epoch(119) == "1 minute"
    assert ch_epoch(120) == "2 minutes"
    assert ch_epoch(60 * 60) == "1 hour"
    assert ch_epoch(60 * 60 * 2) == "2 hours"
    assert ch_epoch(60 * 60 * 24) == "1 day"
    assert ch_epoch(60 * 60 * 24 * 2) == "2 days"
    assert ch_epoch(60 * 60 * 24 * 30) == "1 month"
    assert ch_epoch(60 * 60 * 24 * 30 * 2) == "2 months"
    assert ch_epoch(60 * 60 * 24 * 30 * 12) == "1 year"
    assert ch_epoch(60 * 60 * 24 * 30 * 12 * 2) == "2 years"


def test_get_yt_id():
    assert get_yt_id("http://youtu.be/_lOT2p_FCvA") == "_lOT2p_FCvA"
    assert get_yt_id("http://www.youtube.com/embed/_lOT2p_FCvA") == "_lOT2p_FCvA"
    assert (
        get_yt_id("http://www.youtube.com/v/_lOT2p_FCvA?version=3&amp;hl=en_US")
        == "_lOT2p_FCvA"
    )
    assert (
        get_yt_id(
            "https://www.youtube.com/watch?v=rTHlyTphWP0&index=6&list=PLjeDyYvG6-40qawYNR4juzvSOg-ezZ2a6"
        )
        == "rTHlyTphWP0"
    )
