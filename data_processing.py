from pandas import DataFrame


def add_moving_average(data,
                       window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data

def get_average_price(data: DataFrame):
    return data['Close'].sum() / data['Close'].count()

