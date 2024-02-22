# GCD : 최대공약수

def GCD(a, b):
    while(a != b):
        if (a > b):
            a = a - b
        else : 
            b = b - a
    
    return a

'''
test = GCD(12, 8)
print(test) # 4
'''

a = 66528
b = 52920

result = GCD(a, b)
print(result)

# python3 Greatest_Common_Divisor.py
# >> 1512