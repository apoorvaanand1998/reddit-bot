from bs4 import BeautifulSoup
import requests
import time


def get_kd_result(permalink):
    header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'}
    r = requests.get("http://karmadecay.com"+permalink, headers=header)
    soup = BeautifulSoup(r.text, "html.parser")  ## default python html parser
    if not soup.textarea:
        return False
    return soup.textarea.string



