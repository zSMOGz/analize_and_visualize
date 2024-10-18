import logging

import data_download as dd
import data_upload as du
import data_processing as dps
import data_showing as ds

CSV_FILE_NAME = 'data.csv'


def main():
    logging.basicConfig(filename='analyze_and_visualize_info.log',
                        level=logging.INFO)
    logging.basicConfig(filename='analyze_and_visualize_warning.log',
                        level=logging.WARNING)

    print("Добро пожаловать в инструмент получения и построения графиков"
          + " биржевых данных.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете "
          + "рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT "
          + "(Microsoft Corporation), AMZN (Amazon.com Inc), TSLA "
          + "(Tesla Inc).")
    print("Общие периоды времени для данных о запасах включают: 1д, 5д, "
          + "1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")
    period = input("Введите период для данных (например, '1mo' для одного "
                   + "месяца): ")

    stock_data = dd.fetch_stock_data(ticker,
                                     period)
    if (stock_data is not None
            and not stock_data.empty):
        stock_data = dps.add_moving_average(stock_data)

        ds.create_and_save_plot(stock_data,
                                ticker,
                                period)

        ds.display_average_close_price(stock_data,
                                       period)

        ds.notify_if_strong_fluctuation(stock_data,
                                        1.0)

        du.export_data_to_csv(stock_data,
                              CSV_FILE_NAME)
    else:
        logging.info(f"Не удалось получить данные по тикеру {ticker}"
                     + f" за период {period}")


if __name__ == "__main__":
    main()
