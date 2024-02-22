from pwn import *

flag = "crypto{"

encry = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
encry_bytes = bytes.fromhex(encry)

encry_front = [0x0e, 0x0b, 0x21, 0x3f, 0x26, 0x04, 0x1e]
to_flag = [] # 99 114 121 112 116 111 123

for char in flag:
    to_flag.append( ord(char) )
    
key = ""

for i in range(7):
    key += chr( to_flag[i] ^ encry_front[i])
    
key = "myXORkey" # myXORke 까지만 알아내고, y는 그냥 추측함.

result = xor(encry_bytes, key)
result = result.decode('utf-8')

print(result)

# >> python3 You_either_know_XOR_you_dont.py
# crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}