'''a=13
b=82
natija=a>18 and b==72 #and-->&&
natija2=a>18 or b==72 #and-->||
print(natija2)
kontrakt_turi=input('Kontrak turini kiriting')
tulagan_summasi=int(input('To`lagan summasini kiriting'))
natija=(kontrakt_turi=='oddiy' and tulagan_summasi>=10000000) or (kontrakt_turi=='super' and tulagan_summasi>=50000000)
print(natija)
yoshi = 10
t = False
print(not yoshi > 17)
print(not t) # True
yoshi = 22
xolati = False
vazni = 58
natija = vazni == 58 or xolati and not yoshi > 21 # True
print(natija)
import math

a,b,c=1,1,2
D=pow(b,2)-4*a*c
if D>0:
    x1=(-b+math.sqrt(D))/(2*a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print('x1=',x1, 'x2=',x2)
elif D==0:
    x=(-b)/(2*a)
    print('x=',x)
else:print('Tenglama yechimga ega emas')
x,y,z=float(input('x=')),float(input('y=')),float(input('z='))
if x!=y and y!=z and x!=z:
    if x+y+z<1:
        if x<y and x<z:
            x=(y+z)/2
        elif y<x and y<z:
            y=(x+z)/2
        else:z=(x+y)/2
    elif x>y:
        y=(x+z)/2
    else:x=(y+z)/2
else:print('Sonlar har-xil bo`lishi kerak!') #x=5.0 y=2.0 z=3.0
print('x=',x,'y=',y,'z=',z)'''
a=85
b=9
c= a if a>b else b
print(c)










