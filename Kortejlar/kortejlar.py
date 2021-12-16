'''user = ("Akmal", 21,"Shuhrat")
user[2]="Dilshod"
print(user)
viloyatlar='Toshkent','Sirdaryo','Jizzax'
#print(type(viloyatlar))
print(viloyatlar[2])
boshliq='Anvarov',
print(type(boshliq))
user_list = ["Yusuf", 'Tolib', 'Rustam']
user_tuple = tuple(user_list)
print(user_list)
users = ("Yusuf", 'Qodir', 'Erkin', 'Oybek')
print(users[1:]) # ('Qodir', 'Erkin')
viloyatlar='Toshkent','Sirdaryo','Jizzax'
birvil,ikkivil,uchvil=viloyatlar
print(ikkivil)
def get_user():
    name = "Dilshod"
    age = 21
    is_married = False
    return name, age,is_married
ismi,yoshi,oilalimi = get_user()
print(ismi)
print(yoshi)
print(oilalimi)
talabalar=('Dilshod','Sherzod','Jahongir','Asliddin', 'Xursanali')
for i in range(1):
    print(talabalar[i], end=' ')
talabalar=('Dilshod','Sherzod','Jahongir','Asliddin', 'Xursanali')
if 'Yusufjon' in talabalar:
    print('Talabalar orasida Sherzod ismli talaba bor')
else:
    print('Talabalar orasida Sherzod ismli talaba yo`q')
davlatlar = (
    ("O`zbekiston", 33.8,
     (("Toshkent", 2.65),
      ("Samarqand", 1.1),
      ("Urganch", 0.223),
      ("Farg`ona", 1.223))
     ),
    ("Qozog`iston", 17.5,
     (("Nur Sultan", 1.1),
      ("Olmaota", 2.3))
     ))
#print(davlatlar[1][2][1][1])
for davlat in davlatlar:
    nomi, aholi_soni, shaharlar = davlat
    print(nomi, '-', aholi_soni)
    print("Katta shaharlari:")
    for i, shahar in enumerate(shaharlar) :
        print(i+1,'-',shahar[0], '-', shahar[1])'''
from collections import namedtuple




