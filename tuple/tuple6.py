print("tuple sum and average code")

a=eval(input("enter the value"))

sum=0
i=0

while i<len(a):
	sum=sum+a[i]
	i+=1
print("sum is",sum)
print("average is ",sum/len(a))