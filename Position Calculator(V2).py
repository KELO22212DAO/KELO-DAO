# Position Calculator

def calculate_positions(supply, cost):
    positions = {
        "Poseidon": 0.1,
        "Whale": 0.01,
        "Shark": 0.001,
        "Dolphin": 0.0001,
        "Squid": 0.00001,
        "Turtle": 0.000001,
        "Crab": 0.0000001,
        "Shrimp": 0.00000001,
    }

    results = {}
    for name, fraction in positions.items():
        amount = fraction * supply
        cost_value = amount * cost
        results[name] = (fraction, amount, cost_value)
    
    return results

def print_results(results):
    print("\n------------- Cost per Position ----------")
    print("{:<10} | {:<25} | {:<20} | {:<10}".format("Position", "Percent", "Amount", "Cost"))
    print("-" * 80)
    for position, (fraction, amount, cost_value) in results.items():
        # Format percent to 12 decimal places then strip trailing zeros and an unnecessary dot.
        raw_percent = fraction * 100
        formatted_percent = f"{raw_percent:.12f}"
        percent_str = formatted_percent.rstrip('0').rstrip('.') + '%'
        # Format amount with commas and 8 decimal places, then strip trailing zeros and dot if needed.
        formatted_amount = f"{amount:,.8f}"
        if '.' in formatted_amount:
            amount_str = formatted_amount.rstrip('0').rstrip('.')
        else:
            amount_str = formatted_amount
        # If cost_value is less than $0.01, display "<$0.01"
        if cost_value < 0.01:
            cost_str = "<$0.01"
        else:
            cost_str = f"${cost_value:,.2f}"
        print("{:<10} | {:<25} | {:<20} | {:<10}".format(position, percent_str, amount_str, cost_str))
    print("-" * 80)

def main():
    print("--- This program calculates dollar value cost of crypto positions ---")
    print()

    # Input variables
    name = input("Enter your ticker name: ")
    supply = float(input("Enter current supply: "))
    cost = float(input("Enter current market price: "))

    # Calculate positions and costs
    results = calculate_positions(supply, cost)

    # Print results table
    print_results(results)

if __name__ == "__main__":
    main()
