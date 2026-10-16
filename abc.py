import random
a=[]
b={}
c=int(input("Enter number of players"))
for i in range(i>0,i<=c):
	for j in range(j>=65,j<=91):
		a.append(char(j))
for j in a:
	b[j]=0
while (1):
	for k in b:
		if b[k]<100:
			b[k]+=random.randint(1,6)
		else:
			print("Player named: ",k," won the match")

