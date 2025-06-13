from tabulate import tabulate

def sanitize_input(value):
    return float(value.replace(',', '').strip())

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

    results = []
    for name, fraction in positions.items():
        amount = fraction * supply
        cost_value = amount * cost
        results.append({
            "Position": name,
            "Percent": f"{fraction * 100:.12f}".rstrip('0').rstrip('.') + '%',
            "Amount": f"{amount:,.8f}".rstrip('0').rstrip('.'),
            "Cost": "<$0.01" if cost_value < 0.01 else f"${cost_value:,.2f}"
        })

    return results

def print_results_table(results):
    headers = ["Position", "Percent", "Amount", "Cost"]
    table = [[r["Position"], r["Percent"], r["Amount"], r["Cost"]] for r in results]
    print("\n" + tabulate(table, headers=headers, tablefmt="fancy_grid"))

def main():
    print("--- Crypto Position Calculator ---\n")

    while True:
        token = input("Enter the token name (e.g., PLS): ").strip().upper()
        try:
            total_supply = sanitize_input(input("Enter the total token supply: "))
            percent_burned = sanitize_input(input("Enter the percent burned (0–100): "))
            if not (0 <= percent_burned <= 100):
                raise ValueError("Burn percent must be between 0 and 100.")
            price = sanitize_input(input("Enter the current market price: $"))
        except ValueError as ve:
            print(f"❌ {ve}\n")
            continue

        circulating = total_supply * (1 - percent_burned / 100)
        print(f"\nCirculating Supply: {circulating:,.0f} tokens")

        results = calculate_positions(circulating, price)
        print_results_table(results)

        again = input("\nWould you like to calculate another token? (y/n): ").strip().lower()
        if again != 'y':
            print("\nGoodbye!")
            break

# Call main() directly for online emulators
main()
