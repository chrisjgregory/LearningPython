age = 19
has_id = True

if age < 18:
    print("You cannot enter, you are too young")

elif age >= 18 and not has_id:
    print("You cannot enter, you have no ID")

else:
    print("Welcome!")

 sigma = -99
while sigma < 1:
    print("IMBORED")
    sigma += 1


    def meow(times):
        for i in range(times):
            print("meow")




name = input("What is your name? ")
print("Hello, " + name)


fruits = ["apple", "banana", "cherry"]

print(fruits[0])
print(fruits[1])
print(fruits[-1])

fruits.append("orange")

print(fruits)

score1 = int(input("Enter score 1: "))
score2 = int(input("Enter score 2: "))
score3 = int(input("Enter score 3: "))

scores = [score1, score2, score3]

average = sum(scores) / len(scores)

print(f"Average: {average:.2f}")

word = input("Enter a word: ")
print(word.upper())

words: list[str] = ["basketball", "baseball", "cricket", "tennis"]

search = input("Search for: ")

if search in words:
    print("Found your word!!")
else:
    print("Your word was not found...")

a = "Hi!"
b = 100
print(id(b))

