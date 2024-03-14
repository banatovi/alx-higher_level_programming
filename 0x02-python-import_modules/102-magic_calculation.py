#!/usr/bin/python3
def magic_calculation(m, n, t):
    if m < n:
        return t
    if t > n:
        return m + n
    return m*n - t
