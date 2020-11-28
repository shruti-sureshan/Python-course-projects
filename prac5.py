d={}
n=int(input("enter the no of elemnts\n"))
for i in range(n):
	c=input()
	d.update(c)
print d
m=input('enter a key')
if(m in d.keys()):
	print 'value=',d[m]
d.update({'lmn':90})
print 'update=',d
s=input("enter a value to delete\n")
del d[s]
print 'delete=',d
l1=[70,30,20]
l2=[10,40,50]
d=dict(zip(l1,l2))
print 'map=',d	


