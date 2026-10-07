def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Please enter a valid number.")


def arithmetic():
    print("\n--- Arithmetic Calculator ---")

    num1 = get_number("Enter first number: ")
    operator = input("Enter operator (+, -, *, /): ")

    while operator not in ["+", "-", "*", "/"]:
        print("Invalid operator!")
        operator = input("Enter operator (+, -, *, /): ")

    num2 = get_number("Enter second number: ")

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        while num2 == 0:
            print("Cannot divide by zero.")
            num2 = get_number("Enter a non-zero number: ")
        result = num1 / num2

    print("Result:", result)


def unit_conversion():
    print("\n--- Unit Converter ---")
    print("1. Kilometers to Miles")
    print("2. Celsius to Fahrenheit")

    choice = input("Enter your choice: ")

    while choice not in ["1", "2"]:
        print("Invalid choice!")
        choice = input("Enter 1 or 2: ")

    value = get_number("Enter value: ")

    if choice == "1":
        miles = value * 0.621371
        print(f"{value} km = {miles:.2f} miles")

    elif choice == "2":
        fahrenheit = (value * 9 / 5) + 32
        print(f"{value}°C = {fahrenheit:.2f}°F")


def currency_conversion():
    print("\n--- Currency Converter ---")
    print("1. USD to INR")
    print("2. INR to USD")

    choice = input("Enter your choice: ")

    while choice not in ["1", "2"]:
        print("Invalid choice!")
        choice = input("Enter 1 or 2: ")

    amount = get_number("Enter amount: ")

    usd_to_inr = 83.0

    if choice == "1":
        result = amount * usd_to_inr
        print(f"${amount:.2f} = ₹{result:.2f}")

    elif choice == "2":
        result = amount / usd_to_inr
        print(f"₹{amount:.2f} = ${result:.2f}")


def main():
    while True:
        print("\n===== CALCULATOR & UNIT CONVERTER =====")
        print("1. Arithmetic")
        print("2. Unit Conversion")
        print("3. Currency Conversion")
        print("4. Exit")

        choice = input("Enter your choice: ")

        while choice not in ["1", "2", "3", "4"]:
            print("Invalid choice! Please enter 1-4.")
            choice = input("Enter your choice: ")

        if choice == "1":
            arithmetic()

        elif choice == "2":
            unit_conversion()

        elif choice == "3":
            currency_conversion()

        elif choice == "4":
            print("Thank you for using the calculator!")
            break


main()