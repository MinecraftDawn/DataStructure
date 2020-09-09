def fib(n: int) -> int:
    if n < 0:
        raise Exception("n could not small than 0")
    elif n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def _fib_dp_list(n: int, dp: list):
    if n >= len(dp):
        value = _fib_dp_list(n - 1, dp) + _fib_dp_list(n - 2, dp)
        dp.append(value)

    return dp[n]


def fib_dp_list(n: int) -> int:
    if n < 0:
        raise Exception("n could not small than 0")
    dp = [0, 1]
    return _fib_dp_list(n, dp)


def _fib_dp_dict(n: int, dp: dict) -> int:
    if n not in dp:
        value = _fib_dp_dict(n - 1, dp) + _fib_dp_dict(n - 2, dp)
        dp[n] = value
    return dp[n]


def fib_dp_dict(n: int) -> int:
    if n < 0:
        raise Exception("n could not small than 0")
    dp = {0: 0, 1: 1}
    return _fib_dp_dict(n, dp)


def fib_iter(n: int) -> int:
    if n < 0:
        raise Exception("n could not small than 0")
    elif n <= 1:
        return n
    else:
        pre, cur = 0, 1
        for _ in range(n - 1):
            pre, cur = cur, pre + cur
        return cur
