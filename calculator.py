a=int(input('enter 1st no\n'))
b=int(input('enter 2nd no\n'))
print '1.add\n2.sub\n3.mul\4.div\5.mod\n'
c=int(input('enter a choice\n'))
if(c==1):
    print ‘result=’,a+b
elif(c==2):
    print ‘result=’,a-b
elif(c==3):
    print ‘result=’,a*b
elif(c==4):
    print ‘result=’,a/b
elif(c==5):
    print ‘result=’,a%b
else:
    print 'wrong choice' 


