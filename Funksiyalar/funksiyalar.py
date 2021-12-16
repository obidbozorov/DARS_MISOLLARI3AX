def  salomlashgich(ism, familiyasi):
    print('Assalomu Alaykum, '+ism+' '+familiyasi+'!')
salomlashgich('Yunus','Qurbonniyozov')
salomlashgich('Maqsud',familiyasi='Ismoilov')
def baho_yozuv(baho):
    if baho==5:
        baho_suz='A`lo'
    elif baho==4:
        baho_suz='Yaxshi'
    elif baho==3:
        baho_suz='Qoniqarli'
    elif baho==2:
        baho_suz='Qoniqarsiz'
    else:
        baho_suz='Bahoni noto`g`ri kritdingiz'
    return baho_suz
alini_bahosi=int(input())
print(baho_yozuv(alini_bahosi))
# 2.		Ihtiyoriy n ta sonning yigindisini hisoblash funktsiasi tuzilsin.
n=int(input('n='))
def yigindi(N):
    s=0
    for i in range(1,N+1):
        s+=i
    return s
print(yigindi(n))'''
ismi = "Sardor"
def Salom():
    #global ismi
    ismi='Yusufjon'
    print("Salom", ismi)
def Xayr():
    print("Xayr", ismi)
    '''
Xayr()
print(ismi)
Salom()
print(ismi)
def tanishtiruvchi_funksiya(FISH, kursi, yunalishi, universiteti='O`zMU'):
    satr='Men, '+FISH+' '+universiteti+'da '+str(kursi)+'-kursda '+yunalishi+'yo`nalishida o`qiyman'
    return satr
print(tanishtiruvchi_funksiya(universiteti='O`zMU', yunalishi='AX',
#                              FISH='Ibragimov Yusufjon',kursi=3))
#print(tanishtiruvchi_funksiya('Ibragimov Yusufjon',3,'AX','TDTYU'))
#print(tanishtiruvchi_funksiya(yunalishi='AX',
#                             FISH='Ibragimov Yusufjon',kursi=3))
