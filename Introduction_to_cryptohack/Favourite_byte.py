from pwn import * # pwntools가 아니라 pwn이다...

flag = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
cnt = 0

flag_bytes = bytes.fromhex(flag) # hex string -> bytes

while(1):
    result = xor(flag_bytes, cnt) # -> bytes
    result = result.decode('utf-8') # bytes -> string
    
    if (result[:1] == "c"): # when result == "crypto{ ~ }"
        print(result)
        print("cnt = ", cnt)
        break
    
    cnt += 1
    
'''
>>  python3 Favourite_byte.py

crypto{0x10_15_my_f4v0ur173_by7e}
cnt =  16
'''