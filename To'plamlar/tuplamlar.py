'''ismlar={'Sherzod','Islombek','Yusufjon',4}
print(ismlar[2])
son = {1,2,45,25,54,3}
print(son)
tubSonlar = [2,3,5,7,11]
tubSonlarTuplami = set(tubSonlar)
print(tubSonlarTuplami)
tuplam={1,2}#set()
print(tuplam)
son = {3,4,(5,8),6,4}
print(len(son))
son = set()
son.add(2)
son.add(4)
son.add('Yusufjon')
print(son)
ismlar = {"Anvar", "Abbos", "Abror"}
ismlar.remove("Yusufjon")
print(ismlar)
ismlar = {"Anvar", "Abbos", "Abror"}
ismlar.discard("Yusufjon")
print(ismlar)
ismlar = {"Anvar", "Abbos", "Abror"}
ismlar.clear()
print(ismlar)
ismlar = {"Anvar", "Abbos", "Abror"}
for ism in ismlar:
    print(ism)
ismlar = {"Anvar", "Abbos", "Abror"}
ismlar2 = ismlar.copy()
ismlar2.add("Yusufjon")
print(ismlar)
print(ismlar2)
famil = {"Axmedov", "Niyazov"}
ism = {"Sardor", "Tohir", "Niyazov"}
FIO = famil.union(ism)
print(FIO)
ism1 = {"Axmad", "Sardor", "Ikrom"}
ism2 = {"Sardor", "Tohir","Ikrom"}
ism = ism1.intersection(ism2)
print(ism)
famil = {"Axmad", "Sardor", "Ikrom"}
ism = {"Sardor", "Tohir","Ikrom"}
ism2 = famil & ism
print(ism2)
ism1 = {"Axmad", "Sardor", "Ikrom"}
ism2 = {"Sardor", "Tohir","Ikrom"}
ism = ism2.difference(ism1)
print(ism)
ism1 = {"Axmad", "Sardor", "Ikrom"}
ism2 = {"Sardor", "Ikrom"}
print(ism1.issuperset(ism2))#ism1.issuperset(ism2)==ism2.issubset(ism1)
famil = {"Axmad", "Sardor", "Ikrom"}
fam = frozenset(famil)
fam.add("Qodir")
print(fam)
famil = {"Axmad", "Sardor", "Ikrom"}
if "Akrom" in famil:
    print("Bor")
else:
    print("Yo`q")

ism1 = {"Axmad", "Sardor", "Ikrom"}
ism2 = {"Sardor", "Ikrom"}
if ism2.issubset(ism1):
    print("true")
else:print("false")'''

ism1 = {"Axmad", "Sardor", "Ikrom"}
ism2 = {"Sardor", "IIkrom"}
print(ism1.isdisjoint(ism2))