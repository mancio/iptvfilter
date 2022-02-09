import sys

# remote url (in case you cannot download please check your firewall and Antivirus)
username = sys.argv[1]
password = sys.argv[2]
url = 'http://line.uhd-ott.me/get.php?username={}&password={}&type=m3u_plus&output=mpegts'.format(username, password)

# input filename
input_file = 'list.m3u'

# output file
output_file = 'output.m3u'

# favourite group name
favourite = 'FAV'

# favourites
fav_list = [
    '[PL] [HD] HBO',
    '[PL] [HD] HBO 2',
    '[PL] [HD] HBO 3',
    '[PL] [HD] VH1',
    '[PL] [HD] 4FUN GOLD HITS',
    '[PL] [HD] 4FUN.TV',
    '[PL] [HD] 4FUN DANCE',
    '[PL] [HD] ESKA TV',
    '[PL] [HD] ESKA ROCK TV',
    'GAMBERO ROSSO',
    '[IT] [HD] FOOD NETWORK HD',
    'ALICE HD',
    'DMAX HD',
    'SKY TG 24',
    'RAI NEWS 24 HD'
]

# name, url list of additional channels
ch_list_more = [
    ['M2O TV', 'http://m2otv-lh.akamaihd.net/i/m2oTv_1@186074/index_600_av-b.m3u8'],
    ['ETV Rete 7', 'https://live.ipstream.it/etv/etv.stream/playlist.m3u8'],
    ['DeeJay TV', 'https://deejay_tv-lh.akamaihd.net/i/DeejayTv_1@129866/master.m3u8'],
    ['Radio 51', 'https://59d7d6f47d7fc.streamlock.net/canale51/canale51/playlist.m3u8'],
    ['Radio Company TV', 'https://5929b138b139d.streamlock.net/CompanyTV/livestream_720p/playlist.m3u8'],
    ['Radio Italia TV', 'https://radioitaliatv-lh.akamaihd.net/i/radioitaliatv_1@329645/master.m3u8'],
    ['Radio Kiss Kiss TV', 'https://59253971be783.streamlock.net/KissKissTV/KissKissTV.stream/playlist.m3u8'],
    ['Radio Ibiza TV', 'https://5929b138b139d.streamlock.net/RadioIbizaTV/livestream/playlist.m3u8'],
    ['Radio Number One', 'https://list.iptvcat.com/my_list/s/0a3514d3ff625c9ccff0c29674d2b317.m3u8'],
    ['Radio Birikina TV', 'https://list.iptvcat.com/my_list/s/ddbe4de96e6aa6890c6b28cdac4d27ad.m3u8'],
    ['RaiNews24', 'https://list.iptvcat.com/my_list/s/6091d973177060119c8612ed1e822b56.m3u8'],
    ['SkyTg24', 'https://skyanywhere3-i.akamaihd.net/hls/live/510696/tg24/playlist.m3u8'],
    ['Gambero Rosso', 'http://epix.hopto.org:7713/tony-durr-origin/68985258TNY/889?checkedby:iptvcat.com'],
    ['Food Network', 'https://sbshdlu5-lh.akamaihd.net/i/sbshdl_6@1000854/master.m3u8?checkedby:iptvcat.com'],
    ['Alice', 'https://list.iptvcat.com/my_list/s/d6ab6fbfe6d0edae63978c7773222804.m3u8'],
    ['Comedy Central FHD', 'https://list.iptvcat.com/my_list/s/35234df83d59def8b5ae416c13f93fb3.m3u8']
]

# exclude group list
exclude_gr_list = ['ITALY', 'POLAND', 'NETFLIX', 'DISNEY+', 'HBO']

# exclude ch name list
exclude_ch_list = ['CALCIO', 'Calcio', 'LPC', 'DAZN']

# replace names
replace_list = ['FOR ADULTS', 'PRIV']

# category separator
separator = '----'
