def add(a, b):
  return a + b


def subtract(a, b):
  return a - b


def multiply(a, b):
  return a * b


def divide(a, b):
  return a / b


while True:
  print("What operation would you like to perform?")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")

  operation = input("Enter your choice (1/2/3/4): ")

  if operation in ('1', '2', '3', '4'):
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if operation == '1':
      print(num1, "+", num2, "=", add(num1, num2))

    elif operation == '2':
      print(num1, "-", num2, "=", subtract(num1, num2))

    elif operation == '3':
      print(num1, "*", num2, "=", multiply(num1, num2))

    else:
      print(num1, "/", num2, "=", divide(num1, num2))

  else:
    print("Invalid input!")

  choice = input("Continue? (Y/N): ")
  if choice == "N":
    break

