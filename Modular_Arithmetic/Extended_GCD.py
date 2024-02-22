# 베주 항등식 : a * u + b * v = gcd(a,b) 로 GCD를 a와 b로 표현 가능.

def EEA(r1, r2, u1, u2, v1, v2) :
    if r2 == 0:
        print(f'gcd: {r1}\nu: {u1}\nv: {v1}')
        return
    q = r1//r2
    r = r1%r2
    u = u1 - q*u2
    v = v1 - q*v2

    return EEA(r2, r, u2, u, v2, v)

result = EEA(26513, 32321, 1, 0, 0, 1)
print(result)

# python3 Extended_GCD.py
# gcd = 1 / u = 10245, v = -8404

# gcd = 1 일 때, modular inverse를 구하는데 