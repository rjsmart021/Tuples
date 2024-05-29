stocks_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    ("MSFT", "2021-01-02", 225.0),
    ("GOOGL", "2021-01-01", 1850.0),
    ("GOOGL", "2021-01-02", 1870.0),
    ("AAPL", "2021-01-03", 135.0),
    ("MSFT", "2021-01-03", 230.0),
    ("GOOGL", "2021-01-03", 1900.0),
]


def get_average_closing_price(company_symbol_name: str):
    total_closing_price: float = 0.0

    count = 0

    for stock_data in stocks_data:

        if company_symbol_name == stock_data[0]:
            total_closing_price += stock_data[2]
            count += 1

    return total_closing_price / count


print(get_average_closing_price('AAPL'))
print(get_average_closing_price('MSFT'))
print(get_average_closing_price('GOOGL'))
