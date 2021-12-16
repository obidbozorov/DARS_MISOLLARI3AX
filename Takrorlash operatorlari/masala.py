import math

n=int(input('n='))
s=0
for i in range(n):
    s=s+math.pow(-1,i)*(1+(i+1)*0.1)
print(s)

