## IPTV FILTER

## Filter m3u list and save in new file

### How to run
* execute `python main.py {url}` example `python main.py http://url:2082/get.php?username=gigi&password=jhvckjv&type=m3u_plus`
to filter the list
* upload the output file in your favourite iptv software like [https://siptv.app](https://siptv.app)   

### How to config filter
* in `inputs.py` you can set all you need to configure the filter
* you can find some channels here [https://iptvcat.com](https://iptvcat.com)
  
### Troubleshooting
Program crash: remove `list.m3u` and try again.

Not all channels are loaded: 
* check if the filter is set up properly
* if the remote url is not accessible only the internal
list will be included in the output file