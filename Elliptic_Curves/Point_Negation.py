# E: Y ** 2 = X ** 3 + 497 X + 1768, p: 9739
# P(8045,6936)

# The rule is: if P = (x_p, y_p), then P + (x_p, x_p + y_p) = 0.
# In other word, -P = (x_p, x_p + y_p)

print(8045, -6936 % 9739)

# P + Q = 0 , P + (-P) = 0

# -P_y mod p = p - P_y
# -6936 mod 9739 = 9739 - 6936
# == 2803

# https://www.ctfnote.com/crypto/ecc
# https://trustica.cz/2018/03/08/elliptic-curves-point-negation/

# python3 Point_Negation.py
# >> 8045, 2803