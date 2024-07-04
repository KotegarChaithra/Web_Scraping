#To get https request from any website 'request' library is important

import requests

##url = "https://www.kodnest.com/"
##r = requests.get(url)
##print(r.status_code) #get the number whether it is good request, bd or ok type, 200 is 

##For more info on status code check this website : https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

#if you want to get only text:

url1 = "https://www.kodnest.com/"
r = requests.get(url1)
##print(r.status_code)
print(r.text)#get html code for the website as a output
