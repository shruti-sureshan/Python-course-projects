import math
l1=[]
n=int(input("enter no of elements:\t"))
print("enter the elements:\n")
for i in range(n):
	c=input()
	l1.append(c)
print l1
sum=0
s=0
for i in range(n):
  	sum=sum+l1[i]
avg=sum/n
for i in range(n):
  	s=s+(l1[i]-avg)*(l1[i]-avg)
var=s/n
std=math.sqrt(var)
print "mean=",avg
print "variance=",var
print "std dev=",std
