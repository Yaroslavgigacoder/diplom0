import math
import matplotlib.pyplot as plt
points = [44.333332, 46.36667]
x = [46.36667]
y = [44.333332]
V = 100
firstPoint = [44.333332, 46.36667]
Ha = 200
alpha = 1/298.3
a = 6378136
b = 6356863
extrecitet = (a**2 - b**2)/a**2
extrecitet2 = (a**2 - b**2)/b**2

def CreatePoint(S, Ah, A):
    Ah = Ah*math.pi/180
    A = A*math.pi/180
    firstPoint[0] = firstPoint[0] * math.pi / 180
    firstPoint[1] = firstPoint[1] * math.pi / 180
    Xst = S * math.sin(Ah) * math.cos(A)
    Zst = S * math.sin(Ah) * math.sin(A)
    Yst = S * math.cos(Ah)
    Na = a / (1 - extrecitet * (math.sin(firstPoint[0])) ** 2) ** 0.5
    Xd = (Yst + Na + Ha) * math.cos(firstPoint[0]) - Xst * math.sin(firstPoint[0])
    Yd = Zst
    Zd = (Yst + Na + Ha) * math.sin(firstPoint[0]) + Xst * math.cos(firstPoint[0]) - extrecitet * Na * math.sin(firstPoint[0])
    P = (Xd ** 2 + Yd ** 2) ** 0.5
    teta = math.atan(a * Zd / b * P)
    if Xd != 0:
        LyamdaD = firstPoint[1] + math.atan(Yd / Xd)
    else:
        LyamdaD = firstPoint[1] + math.sign(Yd) * math.pi / 2
    Phid = math.atan((Zd + b * extrecitet2 * (math.sin(teta))**3)/(P - extrecitet * a * (math.cos(teta))**3))
    LyamdaD = LyamdaD*180/math.pi
    Phid = Phid * 180 / math.pi
    y.append(Phid)
    x.append(LyamdaD)
    points.append(LyamdaD)
    points.append(Phid)

    firstPoint[0] = Phid
    firstPoint[1] = LyamdaD
    print(firstPoint[0], firstPoint[1], '\n')
    plt.plot(x, y, 'go')
    # plt.show()
    return points, x, y