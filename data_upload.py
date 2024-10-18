from pandas import DataFrame
from logging import warning


def export_data_to_csv(data: DataFrame,
                       filename: str):
    """
    Экспорт данных в csv

    Parameters:
        data: Тикер акции;
        filename: Период для получения данных о стоимости акции.

    Returns:
        DataFrame: Данные о стоимости акции по тикеру.
    """
    result_save = data.to_csv(filename,
                              index=False)
    if result_save is None:
        warning(f"Ошибка при экспорте данных в csv: {filename}")
