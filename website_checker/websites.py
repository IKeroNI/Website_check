class Strony:
    def __init__(self, nazwa):
        self.filename = nazwa
        self.fileList = [] # lista słowników
        self.reportList = []
        self.index = 0
        self.loadFile(nazwa)

    def loadFile(self, nazwa):
        fh = open(nazwa, "r")
        dataList = fh.readlines()

        for x in dataList:
            x = "https://" + x.strip()
            data = {"website":x, "statusCode" : -1 } 
            self.fileList.append(data)
            data["index"] = len(self.fileList) - 1
            #print(data)    

    def getNextWebsiteToCheck(self):
        if self.index >= len(self.fileList):
            return None
        data = self.fileList[self.index]
        self.index += 1

        return data

    def putWebsiteData(self,data):
        if "index" in data and "website" in data and "statusCode" in data:
            self.reportList.append(data)
        else:
            print("bad keys in report: " + str(data))

    def saveReport(self):
        fh = open("report.txt", "w")

        for x in self.reportList:
            print(x)
            fh.write(str(x["website"])+" - " + str(x) + "\n")
        
        fh.close()
        print("report saved")