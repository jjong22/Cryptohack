# y = pow(x, -1, p) -> x * y ≡ 1 (mod p)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
    
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
    
print(pow(3, -1, 13))
print(modinv(3, 13))
    
# reference : https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
# python3 Modular_Inverting.py
# >> 9