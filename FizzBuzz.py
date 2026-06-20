number = int(input("Enter a number: "))

rizz = int(input("Enter another number: "))

division = (number / rizz)
print("division", division)
moduloReminder = (number % 3)
print("moduloReminder",  moduloReminder)

if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")

elif number % 3 == 0:
    print("Fizz")

elif number % 5 == 0:
    print("Buzz")

else:
    print("Uh Oh Try Again")