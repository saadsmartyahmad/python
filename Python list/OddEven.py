print('odd even program')

a=[1,2,3,4,5]

for x in a:
	if x%2==0:
		print('even')
	else:
		print('odd')


print("by using while loop odd even program")

i=0
while i<len(a):
	if a[i]%2==0:
		print("even number")
	else:
		print('odd number')
	i+=1



print("by using function")

def m1(a):
	if a%2==0:
		print('even')
	else:
		print('odd')

a=[1,2,3,4]
for x in a:
	m1(x)