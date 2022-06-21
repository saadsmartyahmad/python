print("cretating empty list in python syntax")

l=[]
print(l)
print(type(l))

print("create dynamic list")

a=eval(input("enter the value"))
print(a)
print(type(a))

print("list funtion")

l=list(range(1,11))
print(l)

a=int(input("enter the value"))
l=[]

for x in range(a):
	l.append(input("enter the value"))

print(l)