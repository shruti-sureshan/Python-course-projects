l1=[]
n=int(input("enter no of elements:\t"))
print("enter the elements:\n")
for i in range(n):
	c=input()
	l1.append(c)
print l1
print 'max=',max(l1)
print 'min=',min(l1)
