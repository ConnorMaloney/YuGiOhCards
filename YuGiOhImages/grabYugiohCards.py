import requests
import time
import threading
import math

# stopped at 10011000
minImgUrlIndex = 10000000
maxImgUrlIndex = 100000000

def getCards(start, end):
    print("Scanning cards for ranges: ", start, " to ", end)
    for x in range(start, end):
        try:
            r = requests.get('https://ygoprodeck.com/pics/' + str(x) + '.jpg')
            if ('Content-length' in r.headers):
                with open(str(x) + '.jpg', 'wb') as f:
                    if ('Content-length' not in r.headers):
                        print('no content')
                    else:
                        f.write(r.content)
                        print(x, ': ' + r.headers['Content-type'], ' size: ', r.headers['Content-length'])
            else:
                print(x, ' ', r.headers['Content-type'], "   ")
        except:
            print('exception, quitting')
            quit()


getCards(10011000, maxImgUrlIndex)
       