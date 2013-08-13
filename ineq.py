from math import sin, cos, tan, pi, atan2, floor
from random import randint, choice

def rotate(x1, y1, n):
    quadrant = (2 * pi) / float(n)
    k = floor(atan2(y1, x1) / quadrant)
    phi = k * quadrant
    x = x1 * cos(phi) + y1 * sin(phi)
    y = -x1 * sin(phi) + y1 * cos(phi)
    return x, y

def polygon_norm(X, n):
    x , y = rotate(X[0], X[1], n)
    return x + y * tan(pi / float(n))

def inequality(X, Y, n):
    X_Y = X[0] + Y[0], X[1] + Y[1]
    left = round(polygon_norm(X_Y, n), 10)
    right = round(polygon_norm(X, n) + polygon_norm(Y, n), 10)
    return left <= right

def inequality_test(tries, min_range, max_range):
    for i in xrange(tries):
        x = randint(min_range, max_range), randint(min_range, max_range)
        y = randint(min_range, max_range), randint(min_range, max_range)
        n = choice([4, 6])
        if not inequality(x, y, n):
            print "Inequality failed for: x = %s, y = %s, with n = %s" % (x, y, n)
    return "Success"
