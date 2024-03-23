from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda acc, b: acc*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * pow(p, -1, n_i) * p
    return sum % prod

n = [5,11,17]
a = [2,3,5]
print(chinese_remainder(n, a))

# >> 872
# 참고 : https://medium.com/analytics-vidhya/chinese-remainder-theorem-using-python-25f051e391fc