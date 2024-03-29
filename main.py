#!/usr/bin/env python3
import sys

from ipytv import M3UPlaylist, playlist

import inputs
import operations


def main():
    hours = 24

    # check if file is too old and need to be downloaded
    if operations.is_file_old(hours) and len(sys.argv) == 2:
        print('Downloading m3u list from remote')
        source = operations.m3u_download(sys.argv[1], inputs.input_file)
    else:
        print('Source file newer than ' + str(hours) + ' hours')
        source = inputs.input_file

    # destination list
    destination = M3UPlaylist()

    print('Start to build list')
    if operations.source_is_not_empty(source):
        pl = playlist.M3UPlaylist.loadf(source)
        for ch in pl.list:
            # search for all ch not in the exclude list
            if not any(group_name in operations.get_group_title(ch) for group_name in inputs.exclude_gr_list):
                if not any(ch_name in operations.get_ch_name(ch) for ch_name in inputs.exclude_ch_list):
                    if operations.get_group_title(ch).__contains__(inputs.replace_list[0]):
                        operations.set_group_title(ch, inputs.replace_list[1])
                    if operations.get_ch_name(ch).find(inputs.separator) == -1:
                        destination.add_channel(ch)
                    if inputs.fav_list:
                        for tag in inputs.fav_list:
                            if operations.get_ch_name(ch).__contains__(tag):
                                operations.set_group_title(ch, inputs.favourite)
                                # ones is found is removed to make research faster
                                inputs.fav_list.remove(tag)

    for couple in inputs.ch_list_more:
        new_ch = operations.build_ch(couple[0], couple[1])
        destination.add_channel(new_ch)

    operations.save_to_file(destination)

    print('list built')
    print('total channels: ' + str(len(destination.list)))


if __name__ == '__main__':
    # freeze_support() here if program needs to be frozen
    main()  # execute this only when run directly, not when imported!
