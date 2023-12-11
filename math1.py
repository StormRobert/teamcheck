def addition(x):
    return lambda y: y + x

soln = addition(30)
print(soln(24))

