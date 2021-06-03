import sys
import time
import datetime

def SieveOfAtkin(limit):
    sieve = [False] * (limit + 1)

    for i in range(0, limit + 1):
        sieve[i] = False

    x = 1
    while x * x < limit:
        y = 1
        while y * y < limit:

            n = (4 * x * x) + (y * y)
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                sieve[n] ^= True

            n = (3 * x * x) + (y * y)
            if n <= limit and (n % 12 == 7):
                sieve[n] ^= True

            n = (3 * x * x) - (y * y)
            if x > y and n <= limit and (n % 12 == 11):
                sieve[n] ^= True
            y += 1
        x += 1

    x = 5
    while x * x < limit:
        if sieve[x]:
            y = x * x
            while y <= limit:
                sieve[y] = False
                y = y + x * x
        x = x + 1

    # Print primes
    # using sieve[]
    # for a in range(5, limit):
    #     if (sieve[a]):
    #         print(a, end=" ")


if __name__ == "__main__":
    start = time.time()
    limit = 100_000_000
    if sys.argv.__len__() > 1:
        limit = sys.argv[1]
    print("limit: " + str(limit))
    SieveOfAtkin(limit)
    end = time.time()
    duration = end - start
    print("Duration: " + str(datetime.timedelta(seconds=duration)))
