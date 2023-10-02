"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []

    if number_of_primes<=0:
        raise ValueError("Number must be positive and greater than 0!")
    
    target = 0
    start = 2
    while target<number_of_primes:
        count = 0
        for i in range(2,start):
            if start% i == 0:
                print(f"{start} % {i}")
                count += 1
        if count <1:
            target +=1
            list.append(start)
        start += 1
    return list

print(primes(100))