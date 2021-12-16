# class xodimlar:
#     def __init__(self,FISH, oyligi):
#         self.Fish=FISH
#         self.Oyligi=oyligi
#     def xisoblangan_soliq(self):
#         pass
#     def __str__(self):
#         return self.Fish
# class yapon_xodim(xodimlar):
#     def xisoblangan_soliq(self):
#         return self.Oyligi*0.15
#     def __str__(self):
#         return "Yaponiyalik "+self.Fish
# class uzbek_xodim(xodimlar):
#     def xisoblangan_soliq(self):
#         return self.Oyligi*0.12
# Suzuki=yapon_xodim('Suzuki',9000)
# Abdujalil=uzbek_xodim('Karimov Abdujalil',9000)
# # print("Suzukiga hisoblangan soliq ",Suzuki.xisoblangan_soliq())
# # print("Abdujalilga hisoblangan soliq ",Abdujalil.xisoblangan_soliq())
# print(Suzuki)
from builtins import property
class talaba:
    def __init__(self,FISh,kursi,guruhi):
        self.FISH=FISh
        self.guruh=guruhi
        self.__kursi=kursi
    @property
    def kursi(self):
        return self.__kursi
    @kursi.setter
    def kursi(self,kursi):
        if kursi>=1 and kursi<=6:
            self.__kursi=kursi
        else:print("Siz noto`g`ri kurs kiritdingiz. Kurs [1,6] oraliqqa tegishli bo'lishi kerak")
Tulqunov=talaba(FISh="Tulqunov B.",kursi=3,guruhi="AX1901")
print(Tulqunov.kursi)
Tulqunov.kursi=6
Tulqunov.kursi=Tulqunov.kursi+1
print(Tulqunov.kursi)





