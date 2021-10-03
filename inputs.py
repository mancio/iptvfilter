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
    ['R101', 'https://live3-radio-mediaset-it.akamaized.net/content/hls_h0_clr_vos/live/channel(er)/index.m3u8'],
    ['Radio 105', 'https://live3-radio-mediaset-it.akamaized.net/content/hls_h0_clr_vos/live/channel(ec)/index.m3u8'],
    ['Trentino TV', 'https://5e73cf528f404.streamlock.net/TrentinoTV/livestream/playlist.m3u8'],
    ['Virgin Radio TV', 'https://live2-radio-mediaset-it.akamaized.net/Content/hls_h0_clr_vos/live/channel('
                        'ew)/index.m3u8'],
    ['ETV Rete 7', 'https://live.ipstream.it/etv/etv.stream/playlist.m3u8'],
    ['DeeJay TV', 'https://deejay_tv-lh.akamaihd.net/i/DeejayTv_1@129866/master.m3u8'],
    ['Radio 51', 'https://59d7d6f47d7fc.streamlock.net/canale51/canale51/playlist.m3u8'],
    ['Radio Company TV', 'https://5929b138b139d.streamlock.net/CompanyTV/livestream_720p/playlist.m3u8'],
    ['Radio Italia TV', 'https://radioitaliatv-lh.akamaihd.net/i/radioitaliatv_1@329645/master.m3u8'],
    ['Radio Kiss Kiss TV', 'https://59253971be783.streamlock.net/KissKissTV/KissKissTV.stream/playlist.m3u8'],
    ['Radio Monte Carlo TV', 'https://live3-radio-mediaset-it.akamaized.net/Content/hls_h0_clr_vos/live/channel('
                             'bb)/index.m3u8']
]

# exclude group list
exclude_gr_list = ['ITALY', 'POLAND', 'NETFLIX', 'DISNEY+', 'HBO']

# exclude ch name list
exclude_ch_list = ['CALCIO', 'Calcio', 'LPC', 'DAZN']

# replace names
replace_list = ['FOR ADULTS', 'PRIV']

# category separator
separator = '----'
