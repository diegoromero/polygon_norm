from math import sin, cos, tan, pi, atan2, floor
from random import randint, choice

error_range = 1 / float(pow(10, 10))

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
    global error_range
    X_Y = X[0] + Y[0], X[1] + Y[1]
    left = polygon_norm(X_Y, n)
    right = polygon_norm(X, n) + polygon_norm(Y, n)
    if not left <= right:
        approx_equal = abs(left - right)
        if approx_equal > error_range:
            return False
    return True

def inequality_test(tries, min_range, max_range):
    for i in xrange(tries):
        x = randint(min_range, max_range), randint(min_range, max_range)
        y = randint(min_range, max_range), randint(min_range, max_range)
        n = choice([4, 6])
        if not inequality(x, y, n):
            print "Inequality failed for: x = %s, y = %s, with n = %s" % (x, y, n)
            print "||x + y|| = %s, ||x|| + ||y|| = %s" % (polygon_norm((x[0]+y[0], x[1]+y[1]), n), polygon_norm(x,n) + polygon_norm(y,n))
    return "Success"
