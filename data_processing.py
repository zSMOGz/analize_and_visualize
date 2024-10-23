import pandas_ta as ta

from pandas import DataFrame, Series


def add_moving_average(data: DataFrame,
                       window_size: int = 5):
    """
    Добавления и вычисление значения поля среднего арифметического к
    данным.

    Parameters:
        data(DataFrame): Данные, по которым будет производиться
            вычисление и добавление поля;
        window_size: Размер окна.

    Returns:
        DataFrame: Данные с добавленным полем.
    """
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def get_macd(data: DataFrame):
    """
    Вычисление технического индикатора MACD по полю цены закрытия.
    MACD - технический индикатор, позволяющий оценивать силу тренда и
    построенный с учетом усредненного изменения цены.
    График MACD включает в себя две линии:
    1. Среднее значение между экскпоненциальными скользящими средними
    fast и slow;
    2. Экспоненциальное скользящее среднее signal.
    На пересечении двух линий определяется смена тренда.

    Parameters:
        data(DataFrame): Данные, по которым будет производиться
            вычисление.

    Returns:
        tuple[Series, DataFrame]: Индикаторы MACD.
    """

    data.ta.macd(close=data['Close'],
                 fast=1,
                 slow=3,
                 signal=2,
                 append=True)


def get_rsi(data: DataFrame):
    """
    Индекс относительной силы (RSI) — это индикатор импульса, который
    показывает текущую цену относительно средних максимальных и
    минимальных цен за предыдущий торговый период.
    Этот индикатор оценивает состояние перекупленности или
    перепроданности и помогает выявлять развороты тренда, откаты цен и
    появление бычьих или медвежьих рынков.
    Где length - длина скользящего окна.

    Parameters:
        data(DataFrame): Данные, по которым будет производиться
            вычисление.
    """
    data.ta.rsi(close=data['Close'],
                length=14,
                append=True)


def get_average_close_price(data: DataFrame) -> float:
    """
    Вычисление среднего значения по полю цены закрытия.

    Parameters:
        data(DataFrame): Данные, по которым будет производиться
            вычисление.

    Returns:
        float: Среднее значение цены закрытия.
    """
    return data['Close'].mean()


def get_delta_close_price(data: DataFrame) -> float:
    """
    Вычисление разницы между максимальным и минимальным значениями по
        полю цены закрытия.

    Parameters:
        data(DataFrame): Данные, по которым будет производиться
            вычисление.

    Returns:
        float: Разница между максимальным и минимальным значениями цены
            закрытия.
    """
    return data['Close'].max() - data['Close'].min()
