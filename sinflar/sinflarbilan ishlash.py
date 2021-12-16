'''class Talaba:
    ID = 1
    yoshi = 23
    FISH = "Talaba" + str(ID)
    kursi = 3

    def tanishtirish(self):
        return "Mening ismim " + self.FISH

    def bal_baho(self, baho):
        if baho == 5:
            self.baho_suz = "A`lo"
        if baho == 4:
            self.baho_suz = "Yaxshi"
        if baho == 3:
            self.baho_suz = "Qoniqarli"
        if baho == 2:
            self.baho_suz = "Qoniqarsiz"


talaba1 = Talaba()
talaba1.bal_baho(2)
print(talaba1.FISH + "ning o`qishi " + talaba1.baho_suz)
class avto:
    def __init__(self,nomi,yili,yurgan_masofasi, rangi,narxi,xolati):
        self.nomi=nomi
        self.chiqqan_yili=yili
        self.rangi=rangi
        self.yurgani=yurgan_masofasi
        self.narxi=narxi
        self.xolati=xolati
        self.laqabi="Malibu"
    def xolatinianiqlash(self):
        if 2021-self.chiqqan_yili<=3:
            return "Yangi"
        else:
            return "Eski"
    def bojnianiqlash(self,xolati):
        if xolati=="Eski":
            return self.narxi*0.5
        else: return self.narxi*0.3
damas=avto("Damas",2021,1000,"Oq",7500,"Eski")
print(damas.narxi)
nexia=avto(rangi="Qora",yurgan_masofasi=25000,yili=2020,narxi=6000,nomi="Nexia",xolati="Eski")

del nexia
print(nexia.laqabi)'''
class fanlar:
    def __init__(self,nomi,soati,yunalish,kursi=1):
        self.nomi=nomi
        self.soat=soati
        self.kursi=kursi
        self.yunalishi=yunalish
ATUX=fanlar(nomi="ATUX",soati=40, yunalish="AX")
print(ATUX.kursi)



