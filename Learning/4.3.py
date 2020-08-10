def get_fibo():
    before = [1,0,0]
    while(range(10)):
        yield before[1]
        before[2] = before[0]+before[1]
        before[1] , before[0] = before[0], before[2]

fibo_gen = get_fibo()
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))