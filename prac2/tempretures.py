def main():

    menu = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(menu)
    choice = get_conversion_choice()
    while choice != "Q":
        if choice == "C":
            fahrenheit = converting_celsius_to_fahrenheit()
            display_fahrenheit_result(fahrenheit)
        elif choice == "F":
            celsius = convert_fahrenheit_to_celsius()
            display_celsius_result(celsius)
        else:
            print("Invalid option")
        print(menu)
        choice = get_conversion_choice()
    print("Thank you.")


def display_celsius_result(celsius):
    print("Result: {:.2f} C".format(celsius))


def display_fahrenheit_result(fahrenheit):
    print("Result: {:.2f} F".format(fahrenheit))


def convert_fahrenheit_to_celsius():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def converting_celsius_to_fahrenheit():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def get_conversion_choice():
    choice = input(">>> ").upper()
    return choice


main()
