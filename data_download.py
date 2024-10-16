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
    data = stock.history(period=period)
    return data

