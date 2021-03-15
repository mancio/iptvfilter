#!/usr/bin/env python3.7

# insert the filename
fileName = 'list.m3u'

# region list
keyRegion = ['|EU|', 'VOD']
# country of a specific region
keyCountry = ['ITALIA', 'POLONIA']

# combine list
keyMatch = []
match = []
for region in keyRegion:
    for country in keyCountry:
        match = [region, country]
        keyMatch.append(match)

print('check combinations: ', keyMatch)
print('Please wait until you see done!')

# read file and store in a array of lines
with open(fileName, errors='replace', encoding='utf_8') as f:
    lines = f.readlines()
f.close()

# cont line position to be able to add the next line with the url link
lineNumber = 0

with open('output.m3u', 'w', encoding='utf_8') as o:
    # write '#EXTM3U'
    o.write(lines[0])
    for line in lines[1:]:
        lineNumber += 1
        for combination in keyMatch:
            if all(element in line for element in combination):
                o.write(line)
                o.write(lines[lineNumber + 1])
                print('printed line number: ', lineNumber + 1)
o.close()

print('done!')
