import classes

capture = classes.DataCapture()

capture.add(3)
capture.add(7)
capture.add(10)
capture.add(5)
capture.add(12)

print(capture.numberList)
print(capture.less(4))
print(capture.greater(9))
print(capture.between(3,8))