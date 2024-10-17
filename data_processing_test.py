import unittest as ut
import pandas as pd

from data_processing import get_average_close_price


class DataProcessingTest(ut.TestCase):
    def test_get_average_close_price(self):
        test_data = pd.DataFrame({'Close': [400, 500, 600, 700, 800]})
        average_close_price = get_average_close_price(test_data)

        self.assertAlmostEqual(average_close_price, 600)
