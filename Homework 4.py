myUniqueList = []
LeftOvers = []

def addToLeftOvers(extra):
    LeftOvers.append(extra)
    return

def addItem(item):
    if item in myUniqueList:
        addToLeftOvers(item)
        return
    else:
        myUniqueList.append(item)
        return

addItem(6)
addItem(12)
addItem("var1")
addItem(35)
addItem(200)
addItem(200)
addItem("var1")

print(myUniqueList)
print(LeftOvers)

