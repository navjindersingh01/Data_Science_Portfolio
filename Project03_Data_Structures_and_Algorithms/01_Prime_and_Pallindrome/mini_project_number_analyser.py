import prime_palindrome as p


def number_analyser(n):
    prime = False
    palindrome = False

    if p.prime(n):
        prime = True

    if p.pallindrome(n):
        palindrome = True

    return f"Prime Status: {prime}\nPalindrome Status: {palindrome}"

print("--------------------")
num = int(input("Enter the number: "))
print("--------------------")
print(number_analyser(num))
print("--------------------")