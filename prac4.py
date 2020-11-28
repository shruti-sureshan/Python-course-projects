l=[]
n=int(input('enter no of elements\n'))
print 'enter name, rollno, m1, m2, m3\n'
for i in range(n):
	c=input()
	l.append(c)
print l
for i in range(n):
	if(l[i][0]=='python'):
		print 'rollno=',l[i][1]	
		print 'marks1=',l[i][2]
		print 'marks2=',l[i][3]
		print 'marks3=',l[i][4]
t1=tuple(l)
print 'nested tuple=',t1
m=sorted(t1)
print 'sorted=',m
	

