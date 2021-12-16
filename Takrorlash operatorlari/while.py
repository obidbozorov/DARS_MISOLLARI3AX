'''# 1 dan n gacha bo'lgan sonlar yig'indisini hisoblang
n=int(input('n sonini kiriting n='))
i,s=0,0
while i<=n:
    s+=i #s=s+i
    i=i+1
print('s=',s)'''
#Berilgan n ta haqiqiy sonlar orasida o'zidan  oldingi va keyingi sonlardan katta bo'lgan sonlar miqdori topilsin.# 1,5,7,2,6,8,12,45,78,25,41,26
'''n=int(input('n='))
a,b,c=0,0,0
i,s=0,0 #n=12  1,5,7,2,6,8,12,45,78,25,41,26
while i<n:
    a,b,c=b,c,int(input('Keyingi sonni kiriting: '))
    if i>1:
        if b>a and b>c:
            s=s+1
    i+=1
print('s=',s)'''
n=int(input('n='))
i,s=0,0
while i<n:
    a=int(input('Keyingi sonni kiriting: '))
    if i%2==0:
        i=i+1
        continue
    else:
        s=s+a
    i+=1
print('S=',s)


