def dictAndSumTrees(trees):
    treesDict = dict()
    for tree in trees:
        if tree in treesDict:
            treesDict[tree] += 1
        else:
            treesDict[tree] = 1
    sumOfTrees = sum(treesDict.values())
    return treesDict, sumOfTrees

def printTrees(treesDict, sumOfTrees):
    treesDict = dict(sorted(treesDict.items()))
    for treeKey in treesDict.keys():
        percentage = (treesDict[treeKey]/sumOfTrees)*100
        print(treeKey, '{:.4f}'.format(percentage))

tests = int(input())
blank = input()
tuples = []
trees=[]
block = []

try:
    while True:
        entry = input()
        if entry == "":
            trees.append(block)
            block = []
        else:
            block.append(entry)
except EOFError:
    trees.append(block)
    block = []
    pass

for block in trees:
    treesDict, sumOfTrees = dictAndSumTrees(block)
    tuples.append((treesDict, sumOfTrees))

for i in range(0,tests):
    if i != 0:
        print("")
    printTrees(tuples[i][0], tuples[i][1])