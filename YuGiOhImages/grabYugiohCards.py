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

thread_count = 100
thread_list = []

for i in range(thread_count):
    if (i <= 10):
        start = math.floor(i * ((maxImgUrlIndex-minImgUrlIndex)/thread_count)) + 1 + minImgUrlIndex          
        end = math.floor((i + 1) * ((maxImgUrlIndex-minImgUrlIndex)/thread_count)) + 1 + minImgUrlIndex
        thread_list.append(threading.Thread(target=getCards, args=(start, end)))
    else:
        start = math.floor(i * ((maxImgUrlIndex-minImgUrlIndex)/thread_count)) + 1 + minImgUrlIndex          
        end = math.floor((i + 1) * ((maxImgUrlIndex-minImgUrlIndex)/thread_count)) + 1 + minImgUrlIndex
        thread_list.append(threading.Thread(target=getCards, args=(start, end)))


for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

getCards(minImgUrlIndex, maxImgUrlIndex)

"""
thread_count = 8
thread_list = []

for i in range(thread_count):
    # Conditions so that thread 0 does not start at 0 index
    if (i == 0):
        start = minImgUrlIndex          
        end   = int((maxImgUrlIndex - minImgUrlIndex) / 8)
        thread_list.append(threading.Thread(target=getCards, args=(start, end)))
    else:
        start = math.floor(i * ((maxImgUrlIndex-minImgUrlIndex)/thread_count)) + 1          
        end = math.floor((i + 1) * ((maxImgUrlIndex-minImgUrlIndex)/thread_count)) + 1 
        thread_list.append(threading.Thread(target=getCards, args=(start, end)))


for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

getCards(10011000, maxImgUrlIndex)
"""    