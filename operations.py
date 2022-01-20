import os
from os import path
from datetime import datetime, timedelta
from pathlib import Path

import requests
from ipytv import IPTVChannel, IPTVAttr

import inputs


# check if the file is hold and decide if is the case to download it again
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
    if r.status_code != 200:
        print("No content found in remote url, please check if is active, user and pass")
    open(file, 'wb').write(r.content)
    return file


# check if source text file is empty
def source_is_empty(file):
    return os.stat(file).st_size == 0


# build a new channel
def build_ch(tv_name, url):
    channel = IPTVChannel(
        url=url,
        name=tv_name,
        duration="-1",
        attributes={
            IPTVAttr.TVG_ID.value: tv_name,
            IPTVAttr.TVG_NAME.value: tv_name,
            IPTVAttr.GROUP_TITLE.value: inputs.favourite
        }
    )
    return channel


# get the value of group-title
def get_group_title(ch):
    return ch.attributes['group-title']


# get tv channel name
def get_ch_name(ch):
    return ch.attributes['tvg-name']


# set new group title
def set_group_title(ch, title):
    ch.attributes['group-title'] = title


# save all list to string and copy to file
def save_to_file(lis):
    str_list = lis.to_m3u_plus_playlist()
    out_file = open(inputs.output_file, 'w', encoding='utf-8')
    out_file.write(str_list)
    out_file.close()
