import sys

# remote url (in case you cannot download please check your firewall and Antivirus)
username = sys.argv[1]
password = sys.argv[2]
url = 'http://line.uhd-ott.me/get.php?username={}&password={}&type=m3u_plus&output=mpegts'.format(username, password)

# input filename
input_file = 'list.m3u'

# output file
output_file = 'output.m3u'

# exclude list
exclude_list = ['ITALY', 'POLAND', 'NETFLIX', 'DISNEY+', 'HBO']

# replace names
replace_list = ['FOR ADULTS', 'PRIV']

# category separator
separator = '----'
