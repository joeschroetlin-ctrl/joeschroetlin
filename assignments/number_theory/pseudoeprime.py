def is_prime(n):
    if n < 2:
        return False
    for i in range((2,int(n**0.5)+1)):
        if n%1 == 0:
        return False
    return True

def smallest_pseudoprime(base):
    n=2
    while True:
        if not is_prime(n):
            if pow(base, n-1, n) == 1:
                return n
        n += 1

psuedoprime_2 = smallest_pseudoprime(2)
psuedoprime_3 = smallest_pseudoprime(3)

print(f"Smallest pseudoprime to base 2: {pseudoprime_2}")
print(f"Smallest pseudoprime to base 3: {pseudoprime_3}")