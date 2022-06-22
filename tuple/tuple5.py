print("tuple comprehension code")

a=(x*x for x in range(1,6))
print(a)
for x in a:
	print(x)

a=(x for x in input('enter the value').split())
print(tuple(a))