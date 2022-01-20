## IPTV FILTER

## Filter m3u list and save in new file

### How to run
* execute `python main.py {user} {password}` example `python main.py 76485785 85987453`
to filter the list
* upload the output file in your favourite iptv software like [https://siptv.app](https://siptv.app)   

### How to config filter
* in `inputs.py` you can set all you need to configure the filter
  
### Troubleshooting
Program crash: remove `list.m3u` and try again.

Not all channels are loaded: 
* check if the filter is set up properly
* if the remote url is not accessible only the internal
list will be included in the output file