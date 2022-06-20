a=input("enter the value")

i=0
for x in a:
	print("value is {} and index found is {}".format(x,-len(a)+i))
	i+=1