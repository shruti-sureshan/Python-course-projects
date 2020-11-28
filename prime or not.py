x=int(input('enter 1st no\n'))
if(x==2 or x==3 or x==5 or x==7):
    print 'prime'
elif(x%2==0):
    print 'not prime'
elif(x%3==0):
    print 'not prime'
elif(x%5==0):
    print 'not prime'
elif(x%7==0):
    print 'not prime'
else:
    print 'prime'

