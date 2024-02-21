import base64

flag = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

flag_bytes = bytes.fromhex(flag)
flag_b64 = base64.b64encode(flag_bytes) # encode -> bytes
result = flag_b64.decode('utf-8')

print(result)

# python3 Base64.py
# >> crypto/Base+64+Encoding+is+Web+Safe/