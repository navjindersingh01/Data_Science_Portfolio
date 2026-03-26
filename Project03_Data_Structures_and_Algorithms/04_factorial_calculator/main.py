import factorial_logic as logic
factorial = logic.Factorial()

note = """Choose Method For Factorial:
1. Recursive
2. Iterative"""

print("-" * 30)
print(note)
print("-" * 30)
print("")
try:
    choice = int(input("Enter the Choice: "))
    if not(1 <= choice <= 2):
        raise ValueError("Choose From 1 or 2.")
    
    num = int(input("Enter the Number of which Factorial is required: "))
    if not (num >= 0):
        raise ValueError("Invalid Input (must be positive integer)")
    
except Exception as e:
    print("Error:",e)


match choice:
    case 1:
        print("You Have Choosen Recursive Method of Factorial.")
        print("")
        print("Your answer is: ", end = " ")
        result = factorial.factorial_recursion(num)
        print(result)

    case 2:
        print("You Have Choosen Iterative Method of Factorial.")
        print("")
        print("Your answer is: ", end = " ")
        result = factorial.factorial_iterative(num)
        print(result)
        

