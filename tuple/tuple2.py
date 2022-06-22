print("access elemet of tuple by index same as list data type")
a=(1,2,3,4,5,6,7,8,9,10)

print(a[0])
print("by using slice opertaor")

print(a[::])

print(a[-1:-(len(a)+1):-1])


print("concatenation in tuple")

a=(1,2,3)
b="software"
print(a+tuple(b))

c=(1,2,3)
print(a+c)
print("multiplication and repetation operatotr for example")

t=(1,2,3,4,5)
print(t*2)
print(t*3)
print(t*4)