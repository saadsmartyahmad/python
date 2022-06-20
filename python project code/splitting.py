print("splitting method in python")
a=input("enter the character").split()

print(a)
print("it will return list of character in python")


a="python software solution"
b=a.split()

print(a)

print(b)

a="software solution"
print(len(a))

for x in a.split():
	print(x)

print("by default it take space as argument for example")

a="python is very easy to learn".split()
print(a)

b="it-very-easy-when-u-practice".split("-")
print(b)

print("we take another way")
b="it-very-easy-when-u-practice"
c=b.split()
print(c)