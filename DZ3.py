
#Task 1

def is_prime(n):
    if n in (0, 1):
        return False
    i = 2
    while i <= int(n**(0.5))+1:
        if n % i == 0:
            return False
        i += 1
    return True

def find_primes(start, end):
    primes = []
    i = start
    while i <= end:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes

print(find_primes(50, 80))

#Task 2

i = 1
while i <= 10:
    j = 1
    while j <= 10:
        print(f"{i} x {j} = {i*j}")
        j += 1
    print("\n")
    i += 1

#Task 3

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

i = start
while i <= end:
    j = start
    while j <= end:
        print(f"{i} x {j} = {i*j}")
        j += 1
    print("\n")
    i += 1

