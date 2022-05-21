import sys
import copy

prob = {
    "B": 0.001,
    "E": 0.002,
    "A|B,E": 0.95,
    "A|B,nE": 0.94,
    "A|nB,E": 0.29,
    "A|nB,nE": 0.001,
    "J|A": 0.90,
    "J|nA": 0.05,
    "M|A": 0.70,
    "M|nA": 0.01
}

def getProb(item):
    if item[0] == "n":
        return (1 - getProb(item[1:]))
    if item in prob:
        return prob[item]

par = {
    'A': ['B','E'], 
    'B': None, 
    'E': None, 
    'J': ['A'], 
    'M': ['A']
}
def findPar(array):
    newArr = []
    for node in array:
        newItem = node + "|"
        if node[0] == "n":
            nodePar = par[node[1:]]
        else:
            nodePar = par[node]

        if nodePar != None:
            for p in nodePar:
                if p in array:
                    newItem = newItem + p + ","
                else:
                    newItem = newItem + "n" + p + ","
        
        newItem = newItem[0:len(newItem)-1]
        newArr.append(newItem)
    return newArr  

requiredItems = ['A', 'B', 'E', 'J', 'M']
def computeProb(array):
    if len(array) == 5:
        newArr = findPar(array)
        prod = 1
        for node in newArr:
            prod = prod * getProb(node)
        return prod
    else:
        for missingNode in requiredItems:
            if missingNode in array:
                continue
            else:
                flag = False
                for nodeArr in array:
                    if missingNode == nodeArr[1:]:
                        flag = True
                        break

                if flag == True:
                    continue
                else:
                    missedNode = missingNode
                    break

        normalArr = copy.deepcopy(array)
        negateArr = copy.deepcopy(array)
        normalArr.append(missedNode)
        negateArr.append("n"+missedNode)
        return computeProb(normalArr) + computeProb(negateArr)

def convertToProgNotations(array):
    newArr = []
    for node in array:
        if node[1] == "t":
            newArr.append(node[0])
        else:
            newArr.append("n"+node[0])
    return newArr

def __main__(argv):
    if "given" in argv:
        givenIndex = argv.index("given")
        den = argv[givenIndex+1:]
        num = argv[1:givenIndex] + den
        n = computeProb(convertToProgNotations(num))
        d = computeProb(convertToProgNotations(den))
        print "probability = " + str(n/d)
    else:
        print "probability = " + str(computeProb(convertToProgNotations(argv[1:])))

__main__(sys.argv)
