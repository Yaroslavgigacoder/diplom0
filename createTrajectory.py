import math
from createPoints import x, y
listpoint = [44.333332, 46.36667]
Hd = 200
Ha = 200
v = 10
Slist = []
Alist = []
AHlist = []
alpha = 1/298.3
a = 6378136
b = 6356863
lymbdaA = 5435435
phiA = 134
# extrecitet = 2 * alpha - alpha ** 2
extrecitet = (a**2 - b**2)/a**2
(x, y)
def Trajectory(lymbdaA, phiA):

    Nd = a / (1 - extrecitet * (math.sin(y[i]))**2)**0.5
    Na = a / (1 - extrecitet * (math.sin(phiA)) ** 2) ** 0.5

    Xd = (Nd + Hd) * math.cos(y[i]) * math.cos(x[i] - lymbdaA)
    Yd = (Nd + Hd) * math.cos(y[i]) * math.sin(x[i] - lymbdaA)
    Zd = (Nd * (1-extrecitet) + Hd) * math.sin(y[i])

    Xst = -Xd*math.sin(phiA) + Zd * math.cos(phiA) + extrecitet * Na * math.cos(phiA) * math.sin(phiA)
    Yst = Xd*math.cos(phiA) + Zd * math.sin(phiA) + extrecitet * Na*(math.sin(phiA))**2 - (Na +Ha)
    Zst = Yd

    A = math.atan(Zst/Xst)
    Ah = math.atan(((Xst**2 + Yst**2)**0.5)/Yst)
    S = (Xst**2 + Yst**2 + Zst**2)**0.5

    Alist.append(A)
    AHlist.append(Ah)
    Slist.append(S)
    return AHlist, Alist, Slist


