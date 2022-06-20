a="aabbaa"
b="a"
pos=0
while True:
	pos=a.find(b,pos,len(a))
	if(pos==-1):
		break
	else:
		print(b,"found at index",pos)
	pos+=1
