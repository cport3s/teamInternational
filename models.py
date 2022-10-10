class DataCapture():
    def __init__(self):
        self.number_list = []

    def add(self, number):
        self.number_list.append(number)

    def build_stats(self):
        # n*Log(n)
        self.number_list.sort()
        return Stats(self.number_list)

class Stats():
    def __init__(self, sorted_number_list):
        self.sorted_number_list = sorted_number_list.copy()

    def less(self, number):
        counter = 0
        while number > self.sorted_number_list[counter]:
            counter += 1
        return counter

    def greater(self, number):
        counter = 0
        while number > self.sorted_number_list[counter]:
            counter += 1
        counter -= len(self.sorted_number_list)
        return counter

    def between(self, start_number, end_number):
        counter = 0
        for i in self.sorted_number_list:
            if i >= start_number and i <= end_number:
                counter += 1
            if i > end_number:
                break
        #return len([i for i in self.numberList if i >= startNumber and i <= endNumber])
        return counter
