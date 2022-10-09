class DataCapture():
    def __init__(self):
        self.numberList = []

    def add(self, number):
        self.numberList.append(number)
        return self

    def less(self, number):
        tmpList = self.numberList.copy()
        tmpList.sort()
        counter = 0
        while number > tmpList[counter]:
            counter += 1
        return counter

    def greater(self, number):
        tmpList = self.numberList.copy()
        tmpList.sort(reverse=True)
        counter = 0
        while number < tmpList[counter]:
            counter += 1
        return counter

    def between(self, startNumber, endNumber):
        counter = 0
        for i in self.numberList:
            if i >= startNumber and i <= endNumber:
                counter += 1
        #return len([i for i in self.numberList if i >= startNumber and i <= endNumber])
        return counter

    def build_stats():
        pass