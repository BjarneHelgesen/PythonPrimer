import time

def is_prime(candidates, num):
    for i in candidates:
        if num % i == 0:
            return False
    return True

def get_primes(n):
    primes = []

    for i in range(1, n):
        if is_prime(primes, i):
            primes.append(i)
    return primes

start_time = time.time()
primes = get_primes(1000000) 
end_time = time.time()
print(primes)
print("Time taken: ", end_time - start_time) 
