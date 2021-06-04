import sys
import time
import datetime


def SieveOfSundaram(n):
    nNew = int((n - 1) / 2)

    sieve = [0] * (nNew + 1)

    for i in range(1, nNew + 1):
        j = i
        while (i + j + 2 * i * j) <= nNew:
            sieve[i + j + 2 * i * j] = 1
            j += 1

    # for i in range(1, nNew + 1):
    #     if sieve[i] == 0:
    #         print((2 * i + 1), end=" ")


if __name__ == "__main__":
    start = time.time()
    limit = 100_000_000
    if sys.argv.__len__() > 1:
        limit = int(sys.argv[1])
    print("limit: " + str(limit))
    SieveOfSundaram(limit)
    end = time.time()
    duration = end - start
    print("Duration: " + str(datetime.timedelta(seconds=duration)))
