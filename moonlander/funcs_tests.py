# Project 1 - Moonlander
#
# Author: Kelly Mok
# Instructor: Mork

import unittest
from landerFuncs import *

class TestCases(unittest.TestCase):
   def test_update_acc1(self):
      self.assertAlmostEqual(updateAcceleration(1.62, 0), -1.62)
   def test_update_acc2(self):
      self.assertAlmostEqual(updateAcceleration(1.62, 5), 0)
   def test_update_acc3(self):
      self.assertAlmostEqual(updateAcceleration(1, 10), 1)
   def test_update_acc4(self):
      self.assertAlmostEqual(updateAltitude(38.5, 60, 45.7), 121.35)
   def test_update_acc5(self):
      self.assertAlmostEqual(updateAltitude(-10, -60.8, 4), -68.8)
   def test_update_acc6(self):
      self.assertAlmostEqual(updateVelocity(1, 10), 11)
   def test_update_acc7(self):
      self.assertAlmostEqual(updateVelocity(-68.8, 89),20.2)
   def test_update_acc8(self):
      self.assertAlmostEqual(updateFuel(33, -80), 113)
   def test_update_acc9(self):
      self.assertAlmostEqual(updateFuel(45, 96), -51)
   def test_update_acc10(self):
      self.assertAlmostEqual(updateVelocity(-1, -10),-11)
   def test_update_acc11(self):
      self.assertAlmostEqual(updateFuel(961, 480), 481)
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

