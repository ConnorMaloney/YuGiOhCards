import requests
import time
import threading
import math

startIndex = 10000000
# stopped at 10011000
endIndex   = 100000000
for x in range(startIndex, endIndex):
    try:
        r = requests.get('https://ygoprodeck.com/pics/' + str(x) + '.jpg')
        if ('Content-length' in r.headers):
            with open(str(x) + '.jpg', 'wb') as f:
                if ('Content-length' not in r.headers):
                    print('no content')
                else:
                    f.write(r.content)
                    print(str(x) + ': ' + str(r.headers['Content-type']) + ' size: ' + str(r.headers['Content-length']) + "   " + str(time.time()))
        else:
            print(str(x) + ' ' + str(r.headers['Content-type']) + "   " + str(time.time()))
    except:
        print('error, quitting')
        quit()

       