x=input("enter 1st string\n")
y=input("enter 2nd string\n")
print "concat=",x+y
print "repeat=",x*3
print "slicing=",x[::-1]
print "length=",len(x)
print "reverse=",(''.join(reversed(x)))
print "split=",x.split('l')
print "join=",':'.join(x)
s='HI shr'
n=s.replace('hi','hello')
print n


L1=[59,91,23,67,90]
L2=[7,6,1,8,6]
print 'concatenation=',L1+L2
print 'repeat=',L1*2
print 'L1[1:3]=',L1[1:3]
print 'L1[:3]=',L1[:3]
print 'L1[1:5:2]=',L1[1:5:2]
print 'L1[2:]=',L1[2:]
print 'L1[-1:-3]=',L1[-1:-3]
print 'L1[::-1]=',L1[::-1]
L1.append(15)
print 'append=',L1
L1.extend([49,78,'s'])
print 'extend=',L1
L3=[5,2,['Shruti','anushree'],[1,9,7]]
print 'nested list=',L3[2][0][0]
L3.insert(1,'Sita')
print L3
L1.pop(2)
print 'POP AT 2=',L1
L1.pop()
print 'pop=',L1
L1.remove(91)
print 'remove=',L1
L3.sort()
print 'sort=',L3
print 'max=',max(L3)
print 'min=',min(L3)
print 'length=',len(L3)
print 5 in L3


t=(6,9,2,1)
print '[1:3]=',t[1:3]
print '[::-1]=',t[::-1]
t1=(1,'abc','edu')
(rollno,name,profile)=t1
print rollno
print name
print profile
a=(4,5)
b=(6,2)
print 'a>b=',a>b
print 'a<b=',a<b
l=list(t1)
print 'list=',l
m=sorted(t)
print 'sort=',m


d={'abc':54,'xyz':65}
print d
d.update({'lmn':90})
print 'update=',d
del d['xyz']
print 'delete=',d
print d.keys()
print d.values()


s1={}
s2={}
s1=set()
s2=set()
n=input("enter the no of elements for set1\n")
print "enter the elements"
for i in range(n):
	c=input()
	s1.add(c)
print s1
m=input("enter the no of elements for set2\n")
print "enter the elements";
for i in range(m):
	c=input()
	s2.add(c)
print s2
print "UNION:",s1.union(s2)
print "INTERSECTION:",s1&s2
print "DIFFERENCE:",s1-s2
print "SYMM. DIFFERENCE:",s1^s2
print "LENGTH:",len(s1)
print "SUBSET:",s1<=s2
print "SUPERSET:",s1>=s2


