# Python script to calculate the dollar value of your share in a pool and the amount of reflection tokens

def calculate_pool_value(ticker, volume_dollars, tax_rate, share_of_pool):
    """
    Calculate the dollar value of your share in the pool.

    :param ticker: Stock ticker symbol (string)
    :param volume_dollars: Total volume in dollars (float)
    :param tax_rate: Tax rate as a percentage (float)
    :param share_of_pool: Share of the pool as a percentage (float)
    :return: Dollar value of your share in the pool (float)
    """
    # Convert percentages to decimals
    tax_rate_decimal = tax_rate / 100
    share_of_pool_decimal = share_of_pool / 100

    # Calculate the dollar value of the pool after tax
    pool_after_tax = volume_dollars * tax_rate_decimal

    # Calculate the dollar value of your share
    your_share_value = pool_after_tax * share_of_pool_decimal

    return your_share_value

def calculate_reflection_tokens(reflection_token_price, dollar_value):
    """
    Calculate the number of reflection tokens earned based on dollar value.

    :param reflection_token_price: Current price of the reflection token (float)
    :param dollar_value: Dollar value of your share in the pool (float)
    :return: Number of reflection tokens earned (float)
    """
    return dollar_value / reflection_token_price

# Input from the user
ticker = input("Enter the ticker: ")
volume_dollars = float(input("Enter the total volume in dollars: "))
tax_rate = float(input("Enter the tax rate (in %): "))
share_of_pool = float(input("Enter your share of the pool (in %): "))
reflection_token_ticker = input("Enter the reflection token ticker: ")
reflection_token_price = float(input(f"Enter the current price of {reflection_token_ticker}: "))

# Calculate the dollar value of the pool
pool_value = calculate_pool_value(ticker, volume_dollars, tax_rate, share_of_pool)

# Calculate the number of reflection tokens earned
reflection_tokens = calculate_reflection_tokens(reflection_token_price, pool_value)

# Output the results
print(f"The dollar value of your share in the {ticker} pool is: ${pool_value:,.2f}")
print(f"With a reflection token price of ${reflection_token_price:.2f}, you will earn {reflection_tokens:,.2f} {reflection_token_ticker} tokens.")
