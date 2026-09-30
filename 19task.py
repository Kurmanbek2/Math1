import math


def cos_series(x, eps):
    x2 = x * x
    t = 1.0
    s = 1.0
    k = 0
    table = [(0, t, s)]
    while True:
        t_next = -t * x2 / ((2 * k + 1) * (2 * k + 2))
        if abs(t_next) < eps:
            break
        t = t_next
        s += t
        k += 1
        table.append((k, t, s))
    return s, k + 1, abs(t_next), table


if __name__ == "__main__":
    x, eps = 0.44, 1e-8
    s, n, nxt, table = cos_series(x, eps)
    print(f"{'k':>2} {'t_k':>18} {'S_k':>16}")
    for k, t, sk in table:
        print(f"{k:>2} {t:>18.10e} {sk:>16.10f}")
    print(f"\nx = {x}, eps = {eps}")
    print(f"cos(x) = {s:.8f}")
    print(f"число членов = {n}")
    print(f"|следующий член| = {nxt:.3e}")
    print(f"проверка math.cos(x) = {math.cos(x):.8f}")
    print(f"фактическая погрешность = {abs(s - math.cos(x)):.3e}")