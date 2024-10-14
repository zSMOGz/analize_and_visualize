from data_processing import get_average_close_price

def display_average_close_price(stock_data,
                                period):
    average_price = round(get_average_close_price(stock_data), 2)
    print(f"Среднее значение цены акции {average_price} "
          + f"за {period} \n")