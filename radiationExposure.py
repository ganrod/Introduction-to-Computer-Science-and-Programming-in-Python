def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)


def radiationExposure(start, stop, step):
    radiation = 0
    current = start
    while current < stop:
        radiation += f(current) * step
        current += step
    return radiation


print radiationExposure(5, 11, 1)