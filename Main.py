import functools
def function(num, item):
    print (num)
    return num + 1
password = input("Enter Your password (integers only): ")
lst = list(map(int, password))
print (lst)
magic = functools.reduce(function, lst)
print (magic)
result = (lambda x: x % 4 == 0)(magic)
if result:
    print("Correct password!")
else:
    print("Wrong password.")