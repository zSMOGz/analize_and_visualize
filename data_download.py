import yfinance as yf


def fetch_stock_data(ticker,
                     period='1mo'):
    """
    Получение данных о стоимости акции по тикеру.

    Parameters:
        ticker: Тикер акции;
        period: Период для получения данных о стоимости акции.

    Returns:
        DataFrame: Данные о стоимости акции по тикеру.
    """
    stock = yf.Ticker(ticker)
    if 2 <= len(period) <= 4:
        data = stock.history(period=period)
    elif len(period) == 21:
        periods = period.split('.')
        start_period = periods[2] + '-' + periods[1] + '-' + periods[0]
        end_period = periods[5] + '-' + periods[4] + '-' + periods[3]
        data = stock.history(start=start_period,
                             end=end_period)
    else:
        return None
    return data
