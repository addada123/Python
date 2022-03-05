def fib(n, memo = {}):
    if n < 0:
        n *= -1
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        if n in memo:
            return memo[n]
        memo[n] = fib(n - 1) + fib(n - 2)
        return memo[n] * -1
    else:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        if n in memo:
            return memo[n]
        memo[n] = fib(n - 1) + fib(n - 2)
        return memo[n]
print(fib(26524))