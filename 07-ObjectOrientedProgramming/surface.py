import point
import math

p1 = point.Point(2, 6)
p2 = point.Point(3, 4)

if p1==p2:
    print('Odległość pomiędzy punktami wynosi 0.')
else:
    print('Odległość między punktami wynosi: ',math.sqrt((p2.x-p1.x)^2-(p2.y-p1.y)^2))