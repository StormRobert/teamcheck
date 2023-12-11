def addition(x):
    return lambda y: y + x

soln = addition(30)
print(soln(24))

def multiply(z):
    return lambda x:x * z
answer = multiply(20)
print(answer(10))