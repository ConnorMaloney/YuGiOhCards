import requests
import time
import threading
import math

# Define boundaries
minImgUrlIndex = 10000000
maxImgUrlIndex = 100000000
checks = 0
# Scraping function
def getCards(start, end):
    print("Scanning cards for ranges: ", start, " to ", end)
    # Trying reversed for now because script lost connection crashed 1/3rd way in 
    for x in reversed(range(start, end)):
        global checks
        try:
            r = requests.get('https://ygoprodeck.com/pics/' + str(x) + '.jpg')
            if ('Content-length' in r.headers):
                with open(str(x) + '.jpg', 'wb') as f:
                    f.write(r.content)
                    checks += 1
                    print("[CARD OK] ", x, ': ' + r.headers['Content-type'], ' size: ', r.headers['Content-length'], checks, " CHECKS")
            else:
                checks += 1
                print("[NO CARD] ", x, ' ', r.headers['Content-type'], checks, " CHECKS")
        except:
            print('exception, quitting')
            quit()

# Define threads
thread_count = 100
thread_list = []

# Assign thread ranges
for i in range(thread_count):
    start = math.floor(i * ((maxImgUrlIndex-minImgUrlIndex)/thread_count)) + 1 + minImgUrlIndex          
    end = math.floor((i + 1) * ((maxImgUrlIndex-minImgUrlIndex)/thread_count)) + 1 + minImgUrlIndex
    thread_list.append(threading.Thread(target=getCards, args=(start, end)))

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

getCards(minImgUrlIndex, maxImgUrlIndex)