enc = "HFWQY HIAPZS OZGC GSGGWCB"


for i in range(26):
    result = ""
    for char in enc:
        if (char == " "):
            result += " "
            continue
        
        if (ord(char) + i > ord("Z")):
            result += chr( ord(char) + i  - 26 )
        else : result += chr( ord(char) + i )
        
    print(result)
    
# python3 Register.py

# ...
# TRICK TUMBLE ALSO SESSION
# ...

