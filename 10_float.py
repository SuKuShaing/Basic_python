x = 3.3
print('x =', x)
y = 1.1 + 2.2
print('y =', y)
print(x == y)

y_str = format(y, ".3g")
print(y_str)
print(y_str == str(x)) #True

print('*' * 10)

tolerancia = 0.00001
print(abs(x-y) < tolerancia) #True