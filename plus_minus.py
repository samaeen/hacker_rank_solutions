from decimal import*
n=Decimal(input())
a=list(map(Decimal, input().split()))
greater=[]
smaller=[]
zero=[]
for i in a:
	if i>0:
		greater.append(i)
	if i<0:
		smaller.append(i)
	if i==0:
		zero.append(i)
print(format((Decimal(len(greater)/len(a))),'.6f'))
print(format((Decimal(len(smaller)/len(a))),'.6f'))
print(format((Decimal(len(zero)/len(a))),'.6f'))