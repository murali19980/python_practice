"""
Practice: Conditionals & Loops
"""
def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 15 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
    print()

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def find_primes(limit):
    # Implementing using nested loops directly
    primes = []
    for num in range(2, limit + 1):
        is_p = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_p = False
                break
        if is_p:
            primes.append(num)
    return primes

def enumerate_zip_demo():
    fruits = ["apple", "banana", "cherry"]
    prices = [100, 50, 75]
    for idx, fruit in enumerate(fruits):
        print(f"Index {idx}: {fruit}")
    for fruit, price in zip(fruits, prices):
        print(f"{fruit} costs {price}")

if __name__ == "__main__":
    print("FizzBuzz up to 15:")
    fizzbuzz(15)
    print(f"Is 17 prime? {is_prime(17)}")
    print(f"Primes up to 20: {find_primes(20)}")
    enumerate_zip_demo()
