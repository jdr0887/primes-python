import sys
import time
import datetime


def SieveOfEratosthenes(n):

    prime = [True for i in range(n + 1)]
    x = 2
    while x * x <= n:
        if prime[x]:
            for i in range(x * x, n + 1, x):
                prime[i] = False
        x += 1

    # for p in range(2, n + 1):
    #     if prime[p]:
    #         print(p),


if __name__ == "__main__":
    start = time.time()
    limit = 100_000_000
    if sys.argv.__len__() > 1:
        limit = int(sys.argv[1])
    print("limit: " + str(limit))
    SieveOfEratosthenes(limit)
    end = time.time()
    duration = end - start
    print("Duration: " + str(datetime.timedelta(seconds=duration)))
