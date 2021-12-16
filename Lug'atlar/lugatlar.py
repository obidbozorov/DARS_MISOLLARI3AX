'''users = {1: "Tom", 2: "Bob", 3: "Bill"}
elements = {"Au": "Oltin", "Fe": "Temir", "H": "Vodorod",
"O": "Kislorod"}
print(type(users))
objects = {1: "Tom", "2": True, 3: 100.6}
users_list = [["909837022",["Tolib","AX1901"]],["909939343", "Bobur"],
["903943493", "Alibek"]]
users_dict = dict(users_list)
print(users_dict)'''
# uzbek_ingliz={"kitob":"book","qalam":"pencil","daftar":"notebook","ruchka":"pencil"}
# print(uzbek_ingliz["daftar"])
# print(uzbek_ingliz["ruchka"])
# print(uzbek_ingliz)
# uzbek_ingliz["ruchka"]="pen"
# print(uzbek_ingliz)
# uzbek_ingliz={"kitob":"book","qalam":"pencil","daftar":"notebook","ruchka":"pencil"}
# uzbek_ingliz["telefon"]="mobile phone"
# suz=input("So`zni kriting: ")
# if suz in uzbek_ingliz:
#     print(uzbek_ingliz[suz])
# else:
#     print("Bu so`zning tarjimasi topilmadi")
# uzbek_ingliz={"kitob":"book","qalam":"pencil","daftar":"notebook","ruchka":"pencil"}
# print(uzbek_ingliz.get("telefon","Bu zo`zning tarjimasi lug`atimizda yo`q"))
# print(uzbek_ingliz.get("qalam","Bu zo`zning tarjimasi lug`atimizda yo`q"))
# bahoDict = {"A": 5, "B": 4, "C": 3, "D": 2}
# print(bahoDict)
# del bahoDict["C"]
# print(bahoDict)
# bahoDict = {"A": 5, "B": 4, "C": 3, "D": 2}
# print(bahoDict)
# uchirilgan_element=bahoDict.pop("K","Bunday element topilmadi")
# print(uchirilgan_element)
# bahoDict = {"A": 5, "B": 4, "C": 3, "D": 2}
# bahoDict.clear()
# print(bahoDict)
# l = {"ismi": "Sardor", "yoshi": 34}
# l2 = l.copy()
# l2["guruhi"]="AX19"
# l["guruhi"]="ATT19"
# print(l)
# print(l2)
# l1 = {"ismi": "Sardor", "yoshi": 34}
# l2 = {"ismi": "Yusufjon","kursi": 1, "yo`nalishi": "IAT","ismi": "Bekzod"}
# l2.update(l1)
# print(l1)
# print(l2)
# talabalar = {
# "+99890123": "Tolmas",
# "+99890124": "Bobur",
# "+99890125": "Alisher" }
# for tal in talabalar:
#     print(tal, " - ", talabalar[tal])
# talabalar = {
# "+99890123": "Tolmas",
# "+99890124": "Bobur",
# "+99890125": "Alisher" }
# for key, value in talabalar.items():
#     print(value, " - ", key)
# talabalar = {
# "+99890123": "Tolmas",
# "+99890124": "Bobur",
# "+99890125": "Alisher" }
# telraqamlar=talabalar.keys()
# ismlar=talabalar.values()
# listtellraqam=list(telraqamlar)
# print(listtellraqam[1])
# print(ismlar)
# for i in telraqamlar:
#     print(i)
loginData = {
"Zafar":
{
"email": "zafar@nuu.uz",
"tel": "+99890933",
"manzil": "Univer ko`chasi 4"
},
"Rustam":
{
"email": "rustam@nuu.uz",
"tel": "+998902222",
"manzil": "Dekanat ko`chasi 105"
} }
print((loginData["Zafar"]["tel"]))