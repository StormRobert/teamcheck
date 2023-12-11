def addition(x):
    return lambda y: y + x

soln = addition(20)
print(soln(12))