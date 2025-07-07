import math


def calculate(expression):

    allowed = {
        "sqrt": math.sqrt,
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "log": math.log,
        "abs": abs,
        "round": round,
        "pi": math.pi,
        "e": math.e
    }

    try:
        # Evaluate the expression safely using allowed functions
        result = eval(expression, {"__builtins__": None}, allowed)
        return result
    except Exception as error:
        return f"Error: {error}"


print("Simple Calculator with BODMAS and math functions")
print("Type 'quit' to exit.\n")

while True:
    user_input = input("Enter expression: ")

    if user_input.lower() == "quit":
        print("Thanks for using calculator")
        break

    answer = calculate(user_input)
    print("Result:", answer)
