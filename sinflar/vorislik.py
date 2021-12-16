# class avto:
#     nomi="Avto"
#     chiqqan_yili=2021
#     rangi="oq"
#     davlat_raqami="00.A123AA"
# class yuk_mashinalari(avto):
#     yuk_kutarish_massasi=4000
#     samosvalmi=True
# kamaz=yuk_mashinalari()
# kamaz.nomi="Kamaz"
# kamaz.rangi="Sariq"
# kamaz.chiqqan_yili=1996
# kamaz.yuk_kutarish_massasi=25000
# kamaz.samosvalmi=True
# qandaydiravto=avto()
# print(qandaydiravto.samosvalmi)
class Talabalar:
    def __init__(self,FISH,KURSI,YUNALISHI):
        self.__fish=FISH
        self.kursi=KURSI
        self.yunalishi=YUNALISHI
class iqtidorli_talabalar(Talabalar):
    def __init__(self, FISH, KURSI, YUNALISHI,Yutugi,olgan_vaqti):
        super().__init__(FISH, KURSI, YUNALISHI)
        self.yutugi=Yutugi
        self.olgan_vaqti=olgan_vaqti
class super_iqtidorli_talabalar(iqtidorli_talabalar):
    def __init__(self, FISH, KURSI, YUNALISHI, Yutugi, olgan_vaqti,super_yutugi):
        super().__init__(FISH, KURSI, YUNALISHI, Yutugi, olgan_vaqti,)
        self.super_yutugi=super_yutugi

Omadbek=Talabalar(FISH="Omadbek",KURSI=3,YUNALISHI="AX")
Omadbek._Talabalar__fish="Azizbek"
aaaaa=super_iqtidorli_talabalar(FISH="Omadbek",KURSI=3,YUNALISHI="AX",super_yutugi='AAAA', Yutugi=458, olgan_vaqti=124)
print(aaaaa.super_yutugi)
