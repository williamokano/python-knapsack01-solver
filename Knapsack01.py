class Knapsack01(object):
    
    capacity = 0
    numberOfItems = 0
    dataSet = []
    valuesSet = []
    takeSet = []

    def __init__(self, capacity, numberOfItems, dataset):
        self.update(capacity, numberOfItems, dataset)

    def createMatrixes(self):
        for _ in range(self.numberOfItems + 1):
            rowVSet = []
            for _ in range(self.capacity + 1):
                rowVSet.append(0)
            
            self.valuesSet.append(rowVSet)
            self.takeSet.append(rowVSet.copy())

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
                    self.takeSet[i][w] = 0
                
                if i != 0 and w != 0:
                    value = item[0]
                    weight = item[1]
                    
                    if weight > w:
                        self.valuesSet[i][w] = self.valuesSet[i - 1][w]
                        self.takeSet[i][w] = 0
                    else:
                        maxBetween = max(value + self.valuesSet[i - 1][w - weight], self.valuesSet[i - 1][w])
                        self.valuesSet[i][w] = maxBetween
                        self.takeSet[i][w] = 1 if maxBetween != self.valuesSet[i - 1][w] else 0
        
        #
        # find the items
        #
        i = self.numberOfItems
        w = self.capacity
        
        solutionList = []
        
        while i > 0:
            if self.takeSet[i][w] == 1: #I want this object
                solutionList.append(self.dataSet[i - 1])
                w -= self.dataSet[i - 1][1]
            
            i -= 1
        
        idealWeight = 0
        idealValue = 0
        
        for item in solutionList:
            idealValue += item[0]
            idealWeight += item[1]
        
        return [idealValue, idealWeight, solutionList]