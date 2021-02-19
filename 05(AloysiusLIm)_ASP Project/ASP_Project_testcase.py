import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import unittest
import grp5_ASP_project as asp

class testMyProgram(unittest.TestCase):
    def test_sum(self):
         self.assertEqual(asp.Asia5.sum_of_top3, 60923003)

    def test_mean(self):
        self.assertEqual((round(asp.Asia5.mean_of_top3), 2), 20307668.98)


if __name__ == '__main__':
    unittest.main()