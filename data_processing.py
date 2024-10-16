from pandas import DataFrame


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
