from os import path
from datetime import datetime, timedelta
from pathlib import Path

import requests

import inputs


def is_file_old(h):
    if Path(inputs.input_file).is_file():
        file_date = datetime.fromtimestamp(path.getmtime(inputs.input_file))
        hours_ago = datetime.now() - timedelta(hours=h)
        print(file_date)
        print(hours_ago)
        return file_date <= hours_ago
    else:
        return bool(True)


# download m3u original file
def m3u_download(url, file):
    r = requests.get(url, allow_redirects=True)
    open(file, 'wb').write(r.content)
    return file


# get the value of group-title
def get_group_title(ch):
    return ch.attributes['group-title']


# set new group title
def set_group_title(ch, title):
    ch.attributes['group-title'] = title


# get tvg value
def get_tvg_name(ch):
    return ch.attributes['tvg-name']


# save all list to string and copy to file
def save_to_file(lis):
    str_list = lis.to_m3u_plus_playlist()
    out_file = open(inputs.output_file, 'w', encoding='utf-8')
    out_file.write(str_list)
    out_file.close()
