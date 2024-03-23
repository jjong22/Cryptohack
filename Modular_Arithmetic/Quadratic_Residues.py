p = 29
ints = [14, 6, 11]
all_qr = set([])
qr = []

for a in range(p):
  a2 = pow(a,2,p)
  if a2 in ints:
      qr.append(a)
      
for a in range(p):
    a2 = pow(a,2,p)
    all_qr.add(a2)
    
print(all_qr)
      
print(min(qr))