from art import logo


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

print(logo)
num1 = int(input("What is the 1st number: "))
for keys in operations:
    print(keys)

should_continue = True

while should_continue:
    symbol = input("Pick an operation: ")
    num2 = int(input("What is the next number: "))
    calculation_function = operations[symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {symbol} {num2}: {answer}")
    if input(f"Type 'y' to continue calculating with {answer}, otherwise type 'n': ") == "y":
        num1 = answer
    else:
        should_continue = False
        print("GoodBye")