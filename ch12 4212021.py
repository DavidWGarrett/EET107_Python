## recursion is cool?

#looks wrong

#recursive function calls itself

#virtualization?

# recursive shows repetition of a function

# lab FIND MIMIMUM (TUPLE LIST, NOT DICT) - DON'T USE MIN FUNCTION

def main():
    values = [2,2,2,2,2]

    print(str(factorial_r(4)))  #4! = 24
    print(str(factorial_1(4)))  #4! = 24
    print(str(sum_r(values)))  # adds all numbs
    print(str(fibonacci(25)))

def factorial_r(n):
    if n < 1:
        return 1
    else:
        return n * factorial_r(n-1)


def factorial_1(n):
    prod = 1
    for i in range(1, n+1):
        prod = prod * i
    return prod

#find sum of a list of numbers recursively

def sum_r(nums):
    print(nums)
    if len(nums) is 1:
        return nums[0]
    else:
        return nums[0] + sum_r(nums[1:])

def fibonacci(n): #1,1,2,3,5,8 f(n) = f(n-1) + f(n-2)
    print(n)
    if n is 0:
        return 0
    elif n is 1:
       return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)



def factorial_1(n, chara):
    prod = 1
    repeated_chara = ''

    for i in range(1, n+1):
        prod = prod * i
        print(prod)
        repeated_chara += chara

    return repeated_chara


main()