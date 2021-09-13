#!/usr/bin/env python3
from ipytv import M3UPlaylist, playlist

import inputs
import operations


def main():
    hours = 24

    # check if file is too old and need to be downloaded
    if operations.is_file_old(hours):
        print('Downloading m3u list from remote')
        source = operations.m3u_download(inputs.url, inputs.input_file)
    else:
        print('Source file newer than ' + str(hours) + ' hours')
        source = inputs.input_file

    # destination list
    destination = M3UPlaylist()

    print('Start to build list')
    pl = playlist.M3UPlaylist.loadf(source)
    for ch in pl.list:
        if not any(group_name in operations.get_group_title(ch) for group_name in inputs.exclude_list):
            if operations.get_group_title(ch).__contains__(inputs.replace_list[0]):
                operations.set_group_title(ch, inputs.replace_list[1])
            if operations.get_tvg_name(ch).find(inputs.separator) == -1:
                destination.add_channel(ch)

    operations.save_to_file(destination)

    print('list built')
    print('total channels: ' + str(len(destination.list)))


if __name__ == '__main__':
    # freeze_support() here if program needs to be frozen
    main()  # execute this only when run directly, not when imported!
