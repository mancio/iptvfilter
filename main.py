#!/usr/bin/env python3
import sys

import requests as requests

import replacer
from progressbar import progressbar

# insert the filename
fileName = 'list.m3u'

#remote url
username = sys.argv[1]
password = sys.argv[2]
url = 'http://first4k.live:8000/get.php?username={}&password={}&type=m3u_plus&output=ts'.format(username,password)


keyMatch = [['|EU|', 'ITALIA'],
            ['|EU|', 'POLONIA'],
            ['VOD', 'ITALIA'],
            ['|XXX|']]

exclude = ['XXX ITALIANO', 'XXX MARIO SALIERI XXX', '---', '==']

replace = ['|XXX|', 'PRIV']

print('check combinations: ', keyMatch)
print('exclude: ', exclude)

# download and rename file
print('Start file download PLEASE WAIT')
r = requests.get(url, allow_redirects=True)
open(fileName, 'wb').write(r.content)
print('Download complete')

print('Start filtering m3u file')

# read file and store in a array of lines
with open(fileName, errors='replace', encoding='utf_8') as f:
    lines = f.readlines()
f.close()

# cont line position to be able to add the next line with the url link
lineNumber = 0

with open('output.m3u', 'w', encoding='utf_8') as o:
    # write '#EXTM3U'
    o.write(lines[0])
    for line in progressbar(lines[1:]):
        lineNumber += 1
        for combination in keyMatch:
            if all(element in line for element in combination) and not any(element in line for element in exclude):
                if line.__contains__(replace[0]):
                    line = replacer.replacegroup(line, replace[1])
                o.write(line)
                o.write(lines[lineNumber + 1])
                # print('printed line number: ', lineNumber + 1)

o.close()

print('done!')
