s1={}
s2={}
a=input("enter 1st string\n")
b=input("enter 2nd string\n")
s1=set(a)
s2=set(b)
print "COMMON LETTERS IN BOTH THE STRINGS :\n",s1&s2
print "LETTERS PRESENT IN 1ST STRING BUT NOT IN 2ND STRING:\n",s1-s2
print "LETTERS OF BOTH THE STRINGS:\n",s1|s2
print "LETTERS PRESENT IN 2 STRING but not in both :\n",s1^s2
