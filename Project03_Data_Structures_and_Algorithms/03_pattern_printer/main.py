import logic

message = """Choose the Option:
1. Pyramid
2. Inverse Pyramid
3. Right Triangle
4. Inverse Right Triangle
5. Diamond"""

note = """Choose the number of pattern required and write it below:"""
note2 = """Enter the size of the pattern. (Minimum 3)"""

print("")
print("-" * 30)
print("Pattern Printer")
print("-" * 30)
print("")
print(message)
print("")
print("-" * 30)
print("")

print(note)
try:
    choice = int(input("Enter the Choice: "))
    if not (1 <= choice <= 5):
        raise ValueError("Input must be in between 1 to 5.")
    
except ValueError as e:
    print("Error:",e)

print("")
print(note2)
try:
    size = int(input("Enter the Size: "))
    if not (3 <= size):
        raise ValueError("Size must be greater than 2.")

    pattern = logic.Patterns(size)

except ValueError as e:
    print("Error:",e)

match choice:
    case 1:
        print(pattern.pyramid())
    
    case 2:
        print(pattern.inverse_pyramid())
    
    case 3:
        print(pattern.right_triangle())

    case 4:
        print(pattern.inverse_right_triangle())
    
    case 5:
        print(pattern.diamond())
