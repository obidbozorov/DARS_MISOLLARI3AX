'''a=[]
b=[5,7,'sakkiz', True, False]
d=9
sonlar = [1, 'ikki', [3,33,44,[55,11,22,b]], 4,b, True,6,7,8.25,9e9,0]

print(sonlar[4][2])
a=[1,[2,3]]*6
print(a)
a=list(range(2,101,2))
print(a)
poytaxtlar = ['London', 'Parij', [1,'Moskva','Kiev'], 'Tashkent']
print(len(poytaxtlar))
for poytaxt in poytaxtlar:
    print(poytaxt)
nums1 = [1, 0, 2, 3, 4, 5, 6, 7, 8, 9]
nums2 = list(range(10))
if nums1 == nums2:
    print("Bu ro`yxatlar aynan teng.")
else:
    print("Bu ro`yxatlar teng emas.")
n=int(input('n='))
a=[]
for i in range(n):
    a.append(input('Keyingi elementni kiriting: '))
print(a)
a.append('Oxirgi element')
print(a)
a=[100,2,3,4,2,44,87,115,69]
b=[8,9,10]
#a.insert(2,b)
#a.remove(2)
#a.clear()
#a.pop()
#a.sort(reverse=True)
print(min(a))
companies = ["Microsoft", "Google", "Oracle", "Apple"]
item = "Oracle" # o’chirish kerak bo’lgan element
if item in companies:
    companies.remove(item)
else:print('Royhatda '+item+' elementi yo`q')
print(companies)
a=[100,2,3,4,2,44,87,115,69]
print(a.count(44))
nomlar = ["anvar","Sobir","sobir","Alisher","Qosim","tolib"]
sorted_nomlar = sorted(nomlar, key = str.lower)
print(sorted_nomlar)
vil1 = ["Toshkent", "Xorazm", ]
vil2 = vil1
vil2.append('Buxoro')
print(vil1) # ['Toshkent', 'Xorazm', 'Buxoro']
print(vil2) # ['Toshkent', 'Xorazm', 'Buxoro']'''
a=[100,2,3,4,2,44,87,115,69]
print(a[:7:3])
