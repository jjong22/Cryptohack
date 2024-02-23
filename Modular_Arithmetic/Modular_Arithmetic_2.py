# https://ko.wikipedia.org/wiki/%ED%8E%98%EB%A5%B4%EB%A7%88%EC%9D%98_%EC%86%8C%EC%A0%95%EB%A6%AC

'''
print(pow(3, 17, 17)) # 3
print(pow(5, 17, 17)) # 5
print(pow(7, 16, 17)) # 1
'''

p = 65537
print(pow(273246787654,65536, p))

# python3 Modular_Arithmetic_2.py
# >> 1

# 페르마의 소정리에 의해 a^p ≡ a, a^(p-1) ≡ 1 이다.