import requests
import time
import threading
import math

# Define boundaries
minImgUrlIndex = 10000000
maxImgUrlIndex = 100000000

# Scraping function
def getCards(start, end):
    print("Scanning cards for ranges: ", start, " to ", end)
    for x in range(start, end):
        try:
            r = requests.get('https://ygoprodeck.com/pics/' + str(x) + '.jpg')
            if ('Content-length' in r.headers):
                with open(str(x) + '.jpg', 'wb') as f:
                    f.write(r.content)
                    print("[CARD OK] ", x, ': ' + r.headers['Content-type'], ' size: ', r.headers['Content-length'])
            else:
                print("[NO CARD] ", x, ' ', r.headers['Content-type'])
        except:
            print('exception, quitting')
            quit()

# Define threads
thread_count = 100
thread_list = []

# Assign thread ranges
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