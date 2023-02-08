class ram:
    def __init__(self):
        self.intMem = {}

    def rT(self, tabName):
        try:
            return self.intMem.get(tabName)
        except:
            return -1

    def wT(self, tabName, data=None):
        try:
            self.intMem[tabName] = data
            return 0
        except:
            return -1

    def dumpAll(self):
        output = []
        for item, value in self.intMem.items():
            output.append({item, value})
        return len(self.intMem), output #First item here is length, second is list of items.

    def purge(self):
        self.intMem = {}
