"""Le système du cours, (XᵀX + I) w = Xᵀy sur les quatre observations : A, b, x*, les
lignes de niveau de q, et les itérés du gradient conjugué et de la descente de gradient.
Module partagé par les figures du gradient conjugué ; il n'imprime rien."""
import math

A = ((4.0, 1.0), (1.0, 3.0))
B = (1.0, 2.0)
XS = (1 / 11, 7 / 11)
L1, L2 = (7 + math.sqrt(5)) / 2, (7 - math.sqrt(5)) / 2          # valeurs propres


def mv(v):
    return (A[0][0] * v[0] + A[0][1] * v[1], A[1][0] * v[0] + A[1][1] * v[1])


def dot(u, v):
    return u[0] * v[0] + u[1] * v[1]


def vp(l):
    v = (1.0, l - A[0][0])
    n = math.hypot(*v)
    return (v[0] / n, v[1] / n)


V1, V2 = vp(L1), vp(L2)


def niveau(t, n=160):
    """La ligne de niveau ½ (x − x*)ᵀ A (x − x*) = t."""
    pts = []
    for k in range(n + 1):
        s = 2 * math.pi * k / n
        a, b = math.sqrt(2 * t / L1) * math.cos(s), math.sqrt(2 * t / L2) * math.sin(s)
        pts.append((XS[0] + a * V1[0] + b * V2[0], XS[1] + a * V1[1] + b * V2[1]))
    return pts


def ecart(x):
    e = (x[0] - XS[0], x[1] - XS[1])
    return 0.5 * dot(e, mv(e))


def gradient_conjugue(x0=(0.0, 0.0)):
    """Les itérés de l'algorithme des slides (slide 17)."""
    x = x0
    g = tuple(a - b for a, b in zip(mv(x), B))
    xs, ds, d, q = [x], [], None, None
    for k in range(2):
        if k == 0:
            d = g
        else:
            al = -dot(g, q) / dot(d, q)
            d = (g[0] + al * d[0], g[1] + al * d[1])
        q = mv(d)
        be = dot(g, d) / dot(d, q)
        x = (x[0] - be * d[0], x[1] - be * d[1])
        g = (g[0] - be * q[0], g[1] - be * q[1])
        xs.append(x)
        ds.append(d)
    return xs, ds


def descente(pas, n, x0=(0.0, 0.0)):
    x, xs = x0, [x0]
    for _ in range(n):
        g = tuple(a - b for a, b in zip(mv(x), B))
        x = (x[0] - pas * g[0], x[1] - pas * g[1])
        xs.append(x)
    return xs
