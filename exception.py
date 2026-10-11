try:
    numerator = int(input("Enter a value: "))
    denominator = int(input("Enter a value: "))
    result = numerator / denominator

except ValueError:
    print("Enter a valid integer input")

except ZeroDivisionError:
    print("The denominator cannot be 0")

except TypeError:
    print("Invalid data type")

except Exception as e:
    print(f"An unexpected error has occurred")
else:
    print(f"The result: {result}")

finally:
    print("Execution is completed")