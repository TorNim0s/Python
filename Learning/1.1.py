"""
## double letters
def setdouble(item):
    return item * 2

def double_letter(my_str):
    return "".join(list(map(setdouble,my_str)))

print (double_letter("hello mother fucker"))

## devide 4
def dividefour(number):
    return number % 4 == 0

def four_dividers(number):
    return list(filter(dividefour ,range(1,number)))

print (four_dividers(15))

## add number together
import functools

def add(a,b):
    return a+b


def sum_of_digits(number):
    return functools.reduce(add, map(int,str(number)))

print (sum_of_digits(157))

def combine_coins(sem, nums):
    return ", ".join(list(map(lambda s,n: s+str(n), [sem for num in nums], nums)))

print(combine_coins("$", [1,2,3,4]))


def intersection(list_1, list_2):
    return list(set([x for x in list_1 if x in list_2]))

print(intersection([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6]))

def is_prime(number):
    return False if "False" in "".join(set(["False" if number % x == 0 else "True" for x in range(2, number)])) else True
print(is_prime(23))
"""


password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"

print ("".join(list(map(lambda x: chr(ord(x) + 2) if x != " " and x != ":" else x, password))))