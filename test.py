import unittest
import models

class TestDataCapture(unittest.TestCase):
    def setUp(self):
        self.capture = models.DataCapture()
        self.capture.add(3)
        self.capture.add(7)
        self.capture.add(10)
        self.capture.add(5)
        self.capture.add(12)
        self.stats = self.capture.build_stats()
    
    def test_less(self):
        self.assertEqual(self.stats.less(2), 0)
        self.assertEqual(self.stats.less(5), 1)
        self.assertEqual(self.stats.less(13), 5)

    def test_greater(self):
        self.assertEqual(self.stats.greater(1), 5)
        self.assertEqual(self.stats.greater(7), 2)
        self.assertEqual(self.stats.greater(13), 0)

    def test_between(self):
        self.assertEqual(self.stats.between(3, 5), 2)
        self.assertEqual(self.stats.between(7, 12), 3)
        self.assertEqual(self.stats.between(15, 20), 0)
        self.assertEqual(self.stats.between(1, 2), 0)

if __name__ == '__main__':
    unittest.main()