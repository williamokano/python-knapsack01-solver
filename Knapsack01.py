class Knapsack01(object):
    
    capacity = 0
    numberOfItems = 0
    dataSet = []
    valuesSet = []
    takeSet = []

    def __init__(self, capacity, numberOfItems, dataset):
        self.update(capacity, numberOfItems, dataset)

    def createMatrixes(self):
        self.valuesSet = []
        self.takeSet = []
        
        tmp = []
        
        for _ in range(self.numberOfItems + 1):
            rowVSet = []
            rowTSet = []
            for _ in range(self.capacity + 1):
                rowVSet.append(0)
                rowTSet.append(0)
            
            self.valuesSet.append(rowVSet)
            tmp.append(rowTSet)
        
        self.takeSet.append(tmp)

    def update(self, capacity, numberOfItems, dataset):
        self.capacity = capacity
        self.numberOfItems = numberOfItems
        self.dataSet = dataset
        
        self.createMatrixes()
    
    def solve(self):
        #
        # fill the matrixes
        #
        for i in range(self.numberOfItems + 1):
            
            item = self.dataSet[i - 1]
            
            for w in range(self.capacity + 1):
                
                if i == 0 or w == 0:
                    self.valuesSet[i][w] = 0
                    
                    for x in range(len(self.takeSet)):
                        self.takeSet[x][i][w] = 0
                
                if i != 0 and w != 0:
                    value = item[0]
                    weight = item[1]
                    
                    if weight > w:
                        self.valuesSet[i][w] = self.valuesSet[i - 1][w]
                        
                        for x in range(len(self.takeSet)):
                            self.takeSet[x][i][w] = 0
                    else:
                        cellValue = value + self.valuesSet[i - 1][w - weight]
                        aboveCellValue = self.valuesSet[i - 1][w]
                        
                        maxBetween = max(cellValue, aboveCellValue)
                        
                        self.valuesSet[i][w] = maxBetween
                        
                        if cellValue > aboveCellValue:
                            for x in range(len(self.takeSet)):
                                self.takeSet[x][i][w] = 1
                        
                        elif aboveCellValue > cellValue:
                            for x in range(len(self.takeSet)):
                                self.takeSet[x][i][w] = 0
                        else: #That case. Really, don't be that case dude
                            tmp = list(self.takeSet)
                            
                            #Duplicate to mantain states
                            for mtx in tmp:
                                t = []
                                
                                for row in mtx:
                                    t.append(list(row))
                                
                                self.takeSet.append(t)
        
                            
                            #set 0's for the fist half of the list
                            #set 1's for the rest of the list
                            y = len(self.takeSet)
                            hy = int(y / 2)
                            
                            for x in range(hy):
                                self.takeSet[x][i][w] = 1
                                
                            for x in range(hy):
                                self.takeSet[x + hy][i][w] = 0

        #
        # find the items
        #
        solutionList = []
        
        for takeSet in self.takeSet:
            i = self.numberOfItems
            w = self.capacity
                        
            tmpSolution = []
            
            while i > 0:
                if takeSet[i][w] == 1: #I want this object
                    tmpSolution.append(self.dataSet[i - 1])
                    w -= self.dataSet[i - 1][1]
                
                i -= 1
            
            solutionList.append(tmpSolution)
        
        maxWeight = 0
        maxValue = 0
        
        solutionList = self.unique(solutionList)
        
        for item in solutionList[0]:
            maxWeight += item[1]
            maxValue += item[0]
        
        #print all the take matrixes
        
        return [maxValue, maxWeight, solutionList]
    
    def unique(self, myInput):
        output = []
        
        for x in myInput:
            if x not in output:
                output.append(x)
        
        return output