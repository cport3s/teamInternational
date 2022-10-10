class DataCapture():
    def __init__(self):
        self.number_dict = {}

    def add(self, number):
        if self.number_dict.get(number) is None:
            self.number_dict[number] = 1
        else:
            self.number_dict[number] += 1

    def build_stats(self):
        return Stats(dict(sorted(self.number_dict.items())))

class Stats():
    def __init__(self, sorted_number_dict):
        self.sorted_number_dict = sorted_number_dict.copy()

    def less(self, number):
        counter = 0
        while counter < len(self.sorted_number_list) and number > self.sorted_number_list[counter]:
            counter += 1
        return counter

    def greater(self, number):
        counter = 0
        for i in self.sorted_number_list:
            if number < i:
                counter += 1
        return counter

    def between(self, start_number, end_number):
        counter = 0
        for i in self.sorted_number_list:
            if i >= start_number and i <= end_number:
                counter += 1
            if i > end_number:
                break
        return counter
