def factorial_recursion(n: int) -> int:
    if n < 0:
        raise Exception("Integer can't less than zero")
    if n == 0 or n == 1:
        return 1
    return factorial_recursion(n - 1) * n


def factorial_iteration(n: int) -> int:
    ans = 1
    for i in range(1, n + 1):
        ans *= i
    return ans
