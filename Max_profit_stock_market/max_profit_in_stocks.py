def stock_price_calculator(min_price: float, max_price: float):
    max_profit =  max_price - min_price
    print(f"min stock price is: {min_price}")
    print(f"max stock price is: {max_price}")
    print(f"max profit gained by the user is: {max_profit}")
    return max_profit


def main() -> None:
    dummy_stock_prices: list[float] = [10,12,54,78,90,333,700,1201,2]
    sorted_stocks_pricers: list[float] = sorted(dummy_stock_prices)
    min_price = sorted_stocks_pricers[0]
    max_price = sorted_stocks_pricers[-1]
    stock_price_calculator(min_price,max_price)
    

if __name__ == '__main__':
    main()