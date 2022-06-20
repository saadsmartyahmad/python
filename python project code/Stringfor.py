print("print string from forward direction and backword direction ")

s="software"


for x in s:
	print(x)

for x in range(len(s)-1,-1,-1):
	print(s[x])


print(s[::])

print(s[::-1])