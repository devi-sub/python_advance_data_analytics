try:
    n = int(input("Enter a number: "))
    result = n + "10"   
except ValueError:
    print("ValueError")
except TypeError:
    print("TypeError")
else:
    print("No error! Result is:", result)
finally:
    print("Program ended.")
