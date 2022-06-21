print("negative index value printing")

a=['a','b','c','d']

print(len(a))

i=0
print("negative index")
for x in a:
	print("value is {} and negative index is {} ".format(x,-len(a)+i))
	i+=1
