import matplotlib.pyplot as plt
import pandas as pd

from plyer import notification

from data_processing import (get_average_close_price,
                             get_delta_close_price)


def create_and_save_plot(data,
                         ticker,
                         period,
                         filename=None,
                         style_name: str = "default"):
    """
    Создает и сохраняет график цены акции за указанный период.

    Parameters:
        data: Данные по акциям;
        ticker: Тикер акции;
        period: Период выборки данных по акциям;
        filename: Имя файла, в который сохранится график;
        style_name: Стиль графика.
    """
    fig, axes = plt.subplots(3,
                             figsize=(10, 6))

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            axes[0].plot(
                dates,
                data['Close'].values,
                label='Close Price')

            axes[0].plot(
                dates,
                data['Moving_Average'].values,
                label='Moving Average')
        else:
            print("Информация о дате отсутствует или не имеет "
                  + "распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])

        axes[0].plot(
            data['Date'],
            data['Close'].values,
            label='Close Price')

        axes[0].plot(
            data['Date'],
            data['Moving_Average'].values,
            label='Moving Average')

    axes[0].set_title(f"{ticker} Цена акций с течением времени")
    axes[0].set_xlabel("Дата")
    axes[0].set_ylabel("Цена")
    axes[0].legend()

    if data['RSI_14'] is not None:
        axes[1].plot(
            data.index,
            data['RSI_14'].values,
            label='RSI'
        )
        # Add overbought/oversold
        axes[1].axhline(y=30,
                        color='#ff0000',
                        linestyle='dashed')
        axes[1].axhline(y=70,
                        color='#078610',
                        linestyle='dashed')

        axes[1].set_xlabel("Дата")
        axes[1].set_ylabel("RSI")

        axes[1].legend()

    if data['MACD_1_3_2'] is not None:
        axes[2].plot(
            data.index,
            data['MACD_1_3_2'].values,
            label='MACD',
            color='#ff9900'
        )
        axes[2].plot(
            data.index,
            data['MACDs_1_3_2'].values,
            label='Сигнальная линия',
            color='#000000'
        )
        axes[2].legend()

    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart.png"

    plt.style.use(style_name)
    plt.savefig(filename)
    print(f"График сохранен как {filename}")


def print_style_variants():
    for i, style in enumerate(plt.style.available):
        print(str(i) + ". " + style)


def select_style():
    count_styles = len(plt.style.available)
    selected_style = -1
    while (not selected_style.is_integer()
           or selected_style < 0
           or selected_style > count_styles):
        print("Выберите стиль графика:\n")
        print_style_variants()
        selected_style = int(input("Введите номер стиля: "))

    return plt.style.available[selected_style]


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
