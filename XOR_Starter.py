string = "label"
result = ""

for char in string:
    result += chr(ord(char) ^ 13)
    
print(result)

# python3 XOR_Starter.py
# > aloha / crypto{aloha}