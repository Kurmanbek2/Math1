import math


def reduce_angle(x):
    two_pi = 2 * math.pi
    y = math.fmod(x, two_pi)
    if y > math.pi:
        y -= two_pi
    elif y < -math.pi:
        y += two_pi
    if y > math.pi / 2:
        y = math.pi - y
    elif y < -math.pi / 2:
        y = -math.pi - y
    return y


def sin_series(y, eps=1e-6):
    term = y
    s = term
    k = 0
    while True:
        next_term = -term * y * y / ((2 * k + 2) * (2 * k + 3))
        if abs(next_term) < eps:
            break
        term = next_term
        s += term
        k += 1
    return s, k + 1, abs(next_term)


if __name__ == "__main__":
    x = 6.98
    y = reduce_angle(x)
    s, n, nxt = sin_series(y)
    print(f"x = {x}")
    print(f"x - 2*pi = {x - 2 * math.pi:.10f}")
    print(f"приведённый угол y = {y:.10f}  (в [-pi/2, pi/2]: {abs(y) <= math.pi / 2})")
    print(f"sin(x) = {s:.6f}")
    print(f"число членов = {n}")
    print(f"|следующий член| = {nxt:.3e}")
    print(f"проверка math.sin(x) = {math.sin(x):.6f}")
    print(f"фактическая погрешность = {abs(s - math.sin(x)):.3e}")