# Fizz Buzz 
# Given a random number as an input to a function, return "FIZZ" if the number is even and "BUZZ" if the number is odd

def randnum(a):
    if a % 2 == 0:
        return "FIZZ"
    else:
        return "BUZZ"

print(randnum(4))