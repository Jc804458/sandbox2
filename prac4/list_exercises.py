numbers = []
for i in range(5):
    valid = False
    while not valid:
        try:
            number = int(input("Number: "))
            numbers.append(number)
            valid = True
        except ValueError as e:
            print("Not a number. Please enter a number")

print(numbers)
print(f"the first number is {numbers[0]}\nThe last number is {numbers[-1]}\nThe smallest number is "
      f"{min(numbers)}\nThe largest number is {max(numbers)}\nThe average of the number is "
      f"{sum(numbers)/len(numbers):.1f}")
