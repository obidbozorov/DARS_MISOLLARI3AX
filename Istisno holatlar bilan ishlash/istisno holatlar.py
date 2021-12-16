'''
try:
    a,b=4,0 #c=a/b

    c=a/b*d
    print(c)
except:
    print("Nolga bo'lish xatoligi. Siz b songa 0 qiymat berdingiz!")'''
#a,b,c qiymatlar berilgan. Ulardan uchburchak yasab bo'ladimi?
'''import math

try:
    a=float(input('a='))
    b=float(input('b='))
    c=float(input('c='))
    D=math.sqrt(b*b-4*a*c)
    print(D)
    x1=(-b+D)/(2*a)
    x2 = (-b - D) / (2 * a)
    print('x1=',x1,'  x2=',x2)
except ValueError:
    print("Siz haqiqiy son kiritmadingiz")
except ZeroDivisionError:
    print(" a ning qiymati 0 bo'lmasligi kerak!")
except:
    print("Boshqa turdagi xatolik")
finally:
    print('Dastur ishlashi yakunlandi.')'''

import math
try:
    a=float(input('a='))
    b=float(input('b='))
    c=float(input('c='))
    D=math.sqrt(b*b-4*a*c)
    print(D)
    x1=(-b+D)/(2*a)
    x2 = (-b - D) / (2 * a)
    print('x1=',x1,'  x2=',x2)
except Exception as xato:
    print("Quyidagi xatolik yuz berdi:", xato)
finally:
    print('Dastur ishlashi yakunlandi.')

