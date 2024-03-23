'''
string = "label"
result = ""

for char in string:
    result += chr(ord(char) ^ 13)
    
print(result)

# python3 XOR_Starter.py
# > aloha / crypto{aloha}

'''

from pwn import *

string = b"label"
result_bytes = xor(string, 13) # -> bytes
result = result_bytes.decode('utf-8')

print(result)