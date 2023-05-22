def calcTime(dist, speed):
    t = dist / speed
    t = round(t, 1)
    return t

print(calcTime(500, 100))

print(calcTime(dist=500, speed=100))