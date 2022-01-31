from websites import *
import os, sys
import threading, time
import requests
import validators

scriptDir = os.path.dirname(__file__)
os.chdir(scriptDir)

websites = Strony("websites.txt")

#websites.putWebsiteData({"index":0, "website": "duckduckgo.com","statusCode":200})
#websites.saveReport

dataLock = threading.Lock()

class Client(threading.Thread):
    def __init__(self, threadName, websites, sleepTime):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.websites = websites
        self.sleepTime = sleepTime

    def run(self):
        while True:
            dataLock.acquire()
            websiteToCheck = self.websites.getNextWebsiteToCheck()
            dataLock.release()
            if not websiteToCheck:
                break
            print(websiteToCheck)
            self.checkUrl(websiteToCheck)
            time.sleep(self.sleepTime)

        print(self.threadName, "ended")
    
    def checkUrl(self, data):
        try:
            validUrlFlag = validators.url(data["website"])
            if validUrlFlag:
                data["validUrlFlag"] = True
                response = requests.get(data["website"], allow_redirects= True)
                data["statusCode"] = response.status_code
            else:
                data["validUrlFlag"] = False
        except:
            data["exception"] = sys.exc_info()[0]
        
        dataLock.acquire()
        self.websites.putWebsiteData(data)
        dataLock.release()

client1 = Client("client1", websites, 0.1)
client1.start()

client1.join()

numThreads = 10
threadsList = []
num = 0

while num < numThreads:
    t = Client("T" +str(num), websites, 0.1)
    threadsList.append(t)
    t.start()
    num += 1

for t in threadsList:
    t.join()


websites.saveReport()
print("Skonczone")