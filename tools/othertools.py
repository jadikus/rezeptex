def euklid_gcd(a, b):
    if a > b:
        a, b = b, a
    if a == 0:
        return b
    else:
        return euklid_gcd(a, b-b/a*a)