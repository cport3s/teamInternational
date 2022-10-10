class DataCapture():
    def __init__(self):
        self.number_list = []

    def add(self, number):
        self.number_list.append(number)

    def build_stats(self):
        # Pass sorted list to Stats class to optimize searching
        self.number_list.sort()
        return Stats(self.number_list)

class Stats():
    def __init__(self, sorted_number_list):
        self.sorted_number_list = sorted_number_list.copy()

    def less(self, number):
        counter = 0
        # Loop through the list as long as counter < list len and searched number is less than current number on list
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
                # Break to avoid looping through the list needlesly
                break
        return counter
