'''a=[1,[2,3,4,5],7,8,9,7,8,9,11,45,6,8,5,5,6,665546,65,65,65,62,5,6]
j=0
for i in a:
    j+=1
    print(j,'-element qiymati=',i)
for i in 'O`zbekiston Milliy universiteti':
    print(i)
n=int(input('n='))
nfakt=1
for i in range(1,n+1,1):
    nfakt*=i
print(nfakt)
# n sonigacha bo'lgan 7 ga bo'linuvchi sonlar nechta
n=int(input('n='))
s=0
for i in range(7,n+1,7):
    s+=1
print('Jami ',s,' ta son 7 ga bo`linadi')
# Berilgan natural n va m uchun hisoblansin:   .
n=int(input('n='))
m=int(input('m='))
s=0
p=1
for i in range(1,n+1):
    for j in range(5,m+1):
        p=p*(i+j)
    s=s+p
    p=1
print('s=',s)
# Ixtiyoriy natural son  n va n ta float  sonlar ketma-ketligi berilgan to’q o’rinda
# turgan sonlar maximumini, juft o’rinda turgan sonlar minimumini topish programmasi tuzilsin.
n=int(input('n='))
a=float(input('1-sonni kiriting'))
max_a=a
for i in range(2,n+1):
    a=float(input(str(i)+'-sonni kiriting='))
    if i%2==1:
        if a>max_a:
            max_a=a
    else:
        if i==2:
            min_a=a
        if a<min_a:
            min_a=a
print('max_a=',max_a)
print('min_a',min_a)'''

# n soni berilgan En birlik matritsani ekranga chop eting.
n = int(input('n ni kiriting: '))
for i in range(n):
    print('|',end='')
    for j in range(n):
        if i==j:
            print(1,end=", ")
        else:
            print(0,end=", ")
    print('|', end='')
    print()





