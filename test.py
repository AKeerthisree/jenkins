import unittest
from prog1 import summation

class TestSum(unittest.TestCase):
  def test_list_int(self):
    #TEST CASE to add 2 numbers
    data=[23,32]
    res=summation(data)
    self.assertEqual(result,55)
    
if __name__ == "__main__":
  unittest.main()
