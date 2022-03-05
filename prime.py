import numpy as np
from bisect import bisect_right


def smallest_multiple_of_n_geq_m(n: int, m: int) -> int:
    return m + ((n - (m % n)) % n)


class PrimeArraySieve:
    def __init__(self, dtype = np.uint64):
        self.primes: np.ndarray = np.array([2, 3, 5, 7], dtype=dtype)
        self.end_segment: int = 1
        self.dtype = dtype = dtype
    
    def extend(self) -> None:
        k = self.end_segment
        p, q = int(self.primes[k]), int(self.primes[k + 1])
        segment_min, segment_max = p* p, q * q - 1
        segment_len = segment_max - segment_min + 1 

        is_prime = np.full(shape = segment_len, fill_value = True, dtype=bool)

        for pk in self.primes[:k + 1]:
            pk = int(pk)
            start = smallest_multiple_of_n_geq_m(pk, segment_min)
            is_prime[start - segment_min::pk] = False

        segment = np.arange(p * p, q * q, dtype=self.dtype)
        new_primes = segment[is_prime]
        try:
            old_len = len(self.primes)
            self.primes.resize(old_len + len(new_primes))
            self.primes[old_len:] = new_primes
        except ValueError:
            self.primes = np.concatenate((self.primes, new_primes))

        self.end_segment += 1

    def count_prime_less_or_equal(self, n: int) -> int:
        while self.primes[-1] < n:
            self.extend()
        return bisect_right(self.primes, n)
def main():
    import time
    target = 10 ** 9
    start = time.perf_counter()
    sieve = PrimeArraySieve()
    print(sieve.count_prime_less_or_equal(target))
    elapsed = time.perf_counter() - start
    print(f'done in {elapsed:.2f}s')
    
if __name__ == '__main__':
    main()