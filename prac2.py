x=int(input("enter 1st name\n"))
y=int(input("enter 2nd name\n"))
print "1.SWAPPING\n2.SIGNS\n3.PALINDROME\n4.FACTORIAL\n"
z=int(input("enter your choice\n"))

if(z==1):
	print "before swapping"
	print x
	print y
	print "after swapping"
	t=x
	x=y
	y=t
	print x
	print y

elif(z==2):
	if(x>0):
		print "POSITIVE"
	elif(x<0):
		print "NEGATIVE"
	else:
		print "ZERO"

elif(z==4):
	p=1
	for i in range(1,x+1,1):
		p=p*i
	print p

elif(z==3):
	n=x
	sum=0
	while(n!=0):
		r=n%10
		sum=(sum*10)+r
		n=n/10
	if(sum==x):
		print "palindrome"
	else:
		print "not palindrome"		
		

else:
	print "WRONG CHOICE"

