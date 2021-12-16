# class Talaba:
#     def __init__(self,name,kursi):
#         self.ismi=name
#         self.__kursi=kursi
# Dilshod=Talaba("Bekmurodov Dilshod",3)
# Dilshod.
# print(Dilshod.kursi)
class Person:
    def __init__(self, name):
        self.__name = name
        self.__age = 1  # yoshni o'rnatish
    def yoshga_qiymat_yuklash(self, age):
        if age in range(1, 120):
            self.__age = age
        else:
            print("Mumkin bo'lmagan yosh")
    def yoshni_uqish(self):
        return self.__age
    def get_name(self):
        return self.__name
    def display_info(self):
        print("Ism:", self.__name, "\tYosh:", self.__age)
Dilshod=Person("Dilshod")
Dilshod.yoshga_qiymat_yuklash(250)
Dilshod.__age=20
print(Dilshod.yoshni_uqish())
def salomlashgich():
    return "Assalomu Alaykum!"