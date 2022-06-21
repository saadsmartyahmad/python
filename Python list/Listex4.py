print("by using slice we can access the element of list for example")

a=[1,2,3,4,5]

print(a[::])

print(a[-1:-(len(a)+1):-1])

print(a[0:len(a):1])

print(a[1:3])

print(a[4:1:-1])

print("and the main important point is list is mutable in nature we can performe any change in list object")

print("for example")

a=[1,2,3,4,5]
print(a)
a[0]=3
print(a)
a[1]=33
print(a)
a[2]=333
print(a)
a[3]=3333
print(a)
a[4]=33333
print(a)

print()

print("there are two way to trverse emlemt of list")

print('first way by using while loop')

a=['a','b','c','d']

i=0
while i<len(a):
	print(a[i])
	i+=1


print('second way by using for loop')

for x in a:
	print(x)