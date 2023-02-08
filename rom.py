class rom:
    def __init__(self, content):
        self.intMem = content

    def rT(self, tabName):
        try:
            return self.intMem.get(tabName)
        except:
            return -1

    def dumpAll(self):
        output = '\ntotal addresses: ' + str(len(self.intMem))
        for item, value in self.intMem.items():
            output.append({item, value})
        return len(self.intMem), output #copied from ram.py
