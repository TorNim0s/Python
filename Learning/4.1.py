"""
def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    gen = (words[n] for n in sentence.split())
    return " ".join([item for item in gen])

print(translate("el gato esta en la casa"))
"""

def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def first_prime_over(n):
    gen = (num for num in range(n,n+100) if is_prime(num))
    return (next(gen))

print(first_prime_over(1000000))