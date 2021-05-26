## IPTV FILTER

## Filter m3u list and save in new file

### How to run
* install progressbar2 lib by using `pip install progressbar2`
be careful to not get confused with `progressbar`
* execute `python main.py {user} {password}` example `python main.py 76485785 85987453`
to filter the list
* upload the output file in your favourite iptv software like [https://siptv.app](https://siptv.app)   

### How to config filter
* enter the name of the file `fileName = 'list.m3u'`
* choose what to keep in the list `keyMatch = [['|EU|', 'ITALIA'],
  ['|EU|', 'POLONIA'],
  ['VOD', 'ITALIA'],
  ['XXX']]`
  NOTE that is a list of list. Is done in this way to choose all the combinations
* set exclusion list `exclude = ['XXX ITALIANO', 'XXX MARIO SALIERI XXX']`
* if you want to replace group names `replace = ['|XXX|', 'PRIV']`
* if you don't want to filter, just substitute with `???`
  or every symbol not present in the list 
  
### Extra notes
Progress bar works only in a for loop and this can 
give some thoughts to who has already loops in the code.
Not a problem just wrap your function 
`for item in loop(1...n)` to `for item in progressbar(loop(1...n))` 