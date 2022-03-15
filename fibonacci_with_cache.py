from functools import cache

@cache
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

@cache
def factorial(n):
    return n * factorial(n - 1)
def main():
    for i in range(400):
        print(i, fib(i))
    print("done")
    for i in range(20):
        print(i, factorial(i))
    print("done")

if __name__ == '__main__':
    main()
