a = 0xa6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313 # KEY1
b = 0x37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e # KEY2 ^ KEY1
c = 0xc1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1 # KEY2 ^ KEY3
d = 0x04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf # FLAG ^ KEY1 ^ KEY3 ^ KEY2

key1 = a
key2 = key1 ^ b
key3 = key2 ^ c
flag = key1 ^ key2 ^ key3 ^ d

flag = hex(flag)

bytes_flag = bytes.fromhex(flag[2:])
result = bytes_flag.decode('utf-8')

print(result)

# >> crypto{x0r_i5_ass0c1at1v3}