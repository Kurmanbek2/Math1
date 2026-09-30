import math


def exp_series(t, eps):
    term = 1.0
    s = 1.0
    k = 0
    while True:
        next_term = term * t / (k + 1)
        if abs(next_term) < eps:
            break
        term = next_term
        s += term
        k += 1
    return s, k + 1


def cos_series(t, eps):
    term = 1.0
    s = 1.0
    k = 0
    t2 = t * t
    while True:
        next_term = -term * t2 / ((2 * k + 1) * (2 * k + 2))
        if abs(next_term) < eps:
            break
        term = next_term
        s += term
        k += 1
    return s, k + 1


if __name__ == "__main__":
    t, eps = 0.27, 1e-8
    e_val, n_exp = exp_series(t, eps)
    c_val, n_cos = cos_series(t, eps)
    F = e_val * c_val
    F_lib = math.exp(t) * math.cos(t)
    print(f"t = {t}, eps = {eps}")
    print(f"e^t   (ряд) = {e_val:.10f}, членов: {n_exp}")
    print(f"cos t (ряд) = {c_val:.10f}, членов: {n_cos}")
    print(f"F = {F:.8f}")
    print(f"F (библиотека) = {F_lib:.8f}")
    print(f"абсолютная ошибка  = {abs(F - F_lib):.3e}")
    print(f"относительная ошибка = {abs(F - F_lib) / abs(F_lib):.3e}")