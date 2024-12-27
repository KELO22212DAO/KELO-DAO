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
        results[name] = (amount, cost_value)
    
    return results

def print_results(results):
    print("\n------------- Cost per Position ----------")
    print("{:<10} | {:<15} | {:<10}".format("Position", "Amount", "Cost"))
    print("-" * 40)
    for position, (amount, cost) in results.items():
        print("{:<10} | {:<15.8f} | ${:<10.2f}".format(position, amount, cost))
    print("-" * 40)

def main():
    print("--- This program calculates dollar value cost of crypto positions ---")
    print()

    # Variables
    name = input("Enter your ticker name: ")
    supply = float(input("Enter current supply: "))
    cost = float(input("Enter current market price: "))

    # Calculate positions and costs
    results = calculate_positions(supply, cost)

    # Print results
    print_results(results)

if __name__ == "__main__":
    main()
