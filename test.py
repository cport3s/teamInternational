import models

capture = models.DataCapture()

capture.add(3)
capture.add(7)
capture.add(10)
capture.add(5)
capture.add(12)

stats = capture.build_stats()

print(capture.number_list)
print(stats.less(4))
print(stats.greater(9))
print(stats.between(3,8))
