"""
Python program to calculate GCD of two numbers,using the euclidean algorithm.

Euclidean algorithm - https://en.wikipedia.org/wiki/Euclidean_algorithm

eg. If we want to find the GCD of 50 and 20, then we divide 50 by 20.
The remainder is 10 and now we divide 20 by 10, remainder is 0, and hence
10 is the GCD of 50 and 20.
"""


def gcd(n, m):
    """Function computing GCD using the euclidean approach"""
    while (n):
        m, n = n, m % n
    return m

if __name__ == "__main__":
    n, m = map(
        int,
        raw_input(
            'Enter the two numbers seperated with a space: '
        ).strip().split()
    )
    print gcd(n, m)
