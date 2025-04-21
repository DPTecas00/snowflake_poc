def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return 1 if n == 0 else n * factorial(n - 1)

if __name__ == "__main__":
    try:
        number = int(input("Enter a non-negative integer: "))
        print(f"The factorial of {number} is {factorial(number)}")
    except ValueError as e:
        print(f"Error: {e}")
