def fib(n, memo = {}):
    if n in memo: return memo[n]
    if n < 2:return 1
    memo[n] = fib(n- 2) + fib(n - 1)
    return memo[n]


def productFib(prod):
    i = 2
    product = fib(i) * fib(i - 1)
    while product < prod:
        if product == prod:
            return True
        i += 1
        product = fib(i) * fib(i - 1)
    return False
print(productFib(4895))