import matplotlib.pyplot as plt
import pandas as pd

from plyer import notification

from data_processing import (get_average_close_price,
                             get_delta_close_price)


def create_and_save_plot(data,
                         ticker,
                         period,
                         filename=None):
    """
    Создает и сохраняет график цены акции за указанный период.

    Parameters:
        data: Данные по акциям;
        ticker: Тикер акции;
        period: Период выборки данных по акциям;
        filename: Имя файла, в который сохранится график.
    """
    plt.figure(figsize=(10, 6))

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates,
                     data['Close'].values,
                     label='Close Price')
            plt.plot(dates,
                     data['Moving_Average'].values,
                     label='Moving Average')
        else:
            print("Информация о дате отсутствует или не имеет "
                  + "распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'],
                 data['Close'],
                 label='Close Price')
        plt.plot(data['Date'],
                 data['Moving_Average'],
                 label='Moving Average')

    plt.title(f"{ticker} Цена акций с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()

    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")


def display_average_close_price(stock_data,
                                period):
    """
    Отображает среднее значение цены акции за указанный период.

    Parameters:
        stock_data: Исходные данные по акциям;
        period: Период, за который необходимо отобразить среднее.
    """
    average_price = round(get_average_close_price(stock_data), 2)
    print(f"Среднее значение цены акции {average_price} "
          + f"за {period} \n")


def notify_if_strong_fluctuation(data,
                                 threshold: float):
    """
    Уведомляет пользователя о колебаниях цены акций более чем на
        указанный процент.

    Parameters:
        data: Данные по акциям;
        threshold(float): Пороговое значение, при преодолении которого,
            отправляется уведомление.
    """
    delta_close_price = round(get_delta_close_price(data), 2)

    if delta_close_price > threshold:
        message = f"Колебания цены акции более чем на {delta_close_price}"
        notification.notify(message=message,
                            title='Зафиксировано колебание цены акций')
        print(message)
