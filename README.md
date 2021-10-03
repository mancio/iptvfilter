## IPTV FILTER

## Filter m3u list and save in new file

### How to run
* install progressbar2 lib by using `pip install progressbar2`
be careful to not get confused with `progressbar`
* execute `python main.py {user} {password}` example `python main.py 76485785 85987453`
to filter the list
* upload the output file in your favourite iptv software like [https://siptv.app](https://siptv.app)   

### How to config filter
* in `inputs.py` you can set all you need to configure the filter
  
### Extra notes
Progress bar works only in a for loop and this can 
give some thoughts to who has already loops in the code.
Not a problem just wrap your function 
`for item in loop(1...n)` to `for item in progressbar(loop(1...n))` 