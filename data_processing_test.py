import pandas as pd

from data_processing import get_average_close_price


def test_get_average_close_price():
    test_data = pd.DataFrame({'Close': [400, 500, 600, 700, 800]})

    assert get_average_close_price(test_data) == 600
