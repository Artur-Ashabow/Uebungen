
def famous_quote():
    author = "Bruce Lee"
    quote = "The more we value things, the less we value ourselves."
    print(f'{author} once said, "{quote}"')


famous_quote()


def number_eight():
    print(5 + 3)
    print(10 - 2)
    print(4 * 2)
    print(16 // 2)
    print(2 ** 3)


number_eight()


def name_age():
    name = input("Name: ").capitalize()


    while True:
        age = input("Age: ")
        if age.isdigit():
            print(f"Hello, {name}. You are {age} years old.")  #f-strings
            print("Hello, {}. You are {} years old.".format(name, age))  #format function
            print("Hello, " + name + ". You are " + str(age) + " years old.")  #concatenation
            break
        else:
            print("Please enter a number for age!")



name_age()


def swap_integers():

    while True:
        x = input("x: Enter a number: ")
        y = input("y: Enter a number: ")
        if x.isdigit() and y.isdigit():
            print("x:", x)
            print("y:", y)

            new_x = y
            new_y = x
            print("After swap x:", new_x)
            print("After swap y:", new_y)
            break
        else:
            print("Please enter a number!")


swap_integers()


def check_number(number1, number2):

    print("Number 1:", number1)
    print("Number 2:", number2)
    if number1 % 6 == 0 and number2 % 6 == 0:
        print("Both numbers are divisible by 6.")
    elif number1 % 6 == 0 or number2 % 6 == 0:
        print("One number is divisible by 6.")
    else:
        print("Neither number is divisible by 6.")

    if number1 % 10 == 0 and number2 % 10 == 0:
        print("Both numbers are divisible by 10.")
    elif number1 % 10 == 0 or number2 % 10 == 0:
        print("Both numbers are not divisible by 10.")
    else:
        print("Neither numbers are divisible by 10.")


check_number(6, 10)


def sum_up(number1, number2):
    if number1 <= number2:
        sum = 0
        for i in range(number1, number2 + 1):
            sum += i
            print(i, end=" + ") if i < number2 else print(i, end=" = ")
        return sum
    else:
        print("Number 2 must be greater than number 1.")


print(sum_up(3, 9))


def sequence(number):
    if number.is_integer() and 0 < number <= 9:
        for i in range(10):
            if i != number:
                print(i, end=" ")
        print()
    else:
        print("The number must be between 0 and 9!")



sequence(5)


def check_string(text):
    text = text.lower()
    if text.startswith("a") or text.endswith("a"):
        return True
    else:
        return False

print(check_string("apple"))
print(check_string("WATER"))
print(check_string("Artur"))


def triangle(rows):
    for i in range(1, rows + 1):
        print("*")
        if i < rows:
            for j in range(1, i + 1):
                print("*", end=" ")

triangle(4)
