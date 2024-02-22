from pwn import * # pip install pwntools
from Crypto.Util.number import *
import json
import codecs

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


for i in range(100):
    received = json_recv()
    
    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])

    result = ""

    if ( (received["type"]) == "base64"):
        result = base64.b64decode( received["encoded"] )
        result = result.decode('utf-8')
    if ( (received["type"]) == "hex"):
        result = bytes.fromhex( received["encoded"] )
        result = result.decode('utf-8')
    if ( (received["type"]) == "rot13"):
        result = codecs.decode(received["encoded"], 'rot_13')
    if ( (received["type"]) == "bigint"):
        result = bytes.fromhex(received["encoded"][2:])
        result = result.decode("utf-8")
    if ( (received["type"]) == "utf-8"):
        for num in received["encoded"]:
            result += chr(num)

    to_send = {
        "decoded": result
    }
    json_send(to_send)

json_recv()

# python3 Encoding_Challenge.py
# >> {"flag": "crypto{3nc0d3_d3c0d3_3nc0d3}"}