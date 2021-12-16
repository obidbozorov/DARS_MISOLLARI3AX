'''def greet(**names):
    print(names['familiyasi'])

greet(ismi='Bekzod', familiyasi='Begzodovich')
def maksimum(nomi,*tuplam):
    print('Ushbu funksiya '+nomi+' to`plamdagi maksimum elementni topadi')
    max=tuplam[0]
    for i in tuplam:
        if max<i:
            max=i
    return max
print(maksimum('Asosiy to`plam',5,98,-98,100,-9,78,))
def talabani_tanishtir(**kwargs):
    if kwargs['yutugi']:
        print('Ushbu talaba iqtidorli talaba')
    for key, value in kwargs.items():
        print(key,value)
talabani_tanishtir(ismi='Ibratjon',
Familiyasi='Olimov',
stipendiyasi=600000,
yutugi='Prezident stipendiyanti',tillarni_bilishi='C++, Python, Java')'''
#Rekursiv funksiyalar n gacha bo'lgan barcha fibonachi sonini chop eting.
n=int(input('n='))
f0=1
f1=1
A=1
print(f0, f1,end=', ')
def fibonachi(n):
    global f0,f1,A
    f2=f0+f1
    f0 = f1
    f1 = f2
    if f2 < n:
        print(f2,end=', ')
        fibonachi(n)
    A+=1
    print(A)
    return
fibonachi(n)
