def prime(n):
    if n < 2:
        return False
    
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
        
    return True

def pallindrome(n):
    return str(n) == str(n)[::-1]


def combine(n):
    if prime(n) and pallindrome(n):
        return "Both"
    else:
        if prime(n):
            return "Prime only"
        if pallindrome(n):
            return "Pallindrome only"

if __name__ == "__main__":
    print(prime(4))
    print(pallindrome(121))
    print(combine(13))