l1=[]
l=[]
e=[]
o=[]
n=int(input("enter no of elements:\t"))
print("enter the elements:\n")
for i in range(n):
	c=input()
	l1.append(c)
print l1
print '1.even and odd\n2.merge and sort\n3.update\n4.max and min\n5.names\nenter your choice:\n'
a=int(input())
if(a==1):
	for i in range(len(l1)):
		if(l1[i]%2==0):
			e.append(l1[i])
		else:
			o.append(l1[i])
	print 'even=',e
	print 'odd=',o
elif(a==2):
	for i in range(len(l1)):
		if(l1[i]%2==0):
			e.append(l1[i])
		else:
			o.append(l1[i])
	print 'merge=',e+o
	s=e+o
	s.sort()
	print 'sort=',s
elif(a==3):
	l1.extend(input('enter value\n').split(','))
	print 'update=',l1
	m=len(l1)/2
	l1.pop(m)
	print 'delete=',l1
elif(a==4):
	print 'max=',max(l1)
	print 'min=',min(l1)
elif(a==5):
        m=int(input('enter no of elements\n'))
        for i in range(m):
                t=input('enter element\n')
                l.append(t)
        print l
        l1.extend(l)
        print l1
        if 'python' in l1:
                print 'Word python is present in the list'
        else:
                print 'Word python is not present in the list'

