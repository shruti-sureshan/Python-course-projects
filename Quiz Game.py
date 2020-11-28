print ('WELCOME TO THE MULTIPLE CHOICE TEST\n')
name = input('WHAT IS YOUR NAME? ')
print ('\nHI THERE ' + name + '! LET''S PLAY A GAME!\n')
print ('I will ask you 10 questions and give you three choices for each question.\n\nYou select which choice is the correct answer. Eg. A, B,C,D\n')
print ('Important : Please keep your CAPS LOCK on')
print ('\n-----------------------------------------------------------\n')

###########################################################################
#                          SET THE SCORE TO ZERO                          #
###########################################################################

score = 0
score = int(score)  #Convert the 0 into a number so we can add scores


###########################################################################
#                           QUESTION 1                                    #
###########################################################################

print ('QUESTION 1: What is the output of the following program :\nprint "Hello World"[::-1]\n')
print ('A. dlroW olleH')
print ('B. Hello World')
print ('C. dlroW')
print ('D. H')
print ('')

Q1answer = "A"
Q1response= input('Your answer : ')

if (Q1response != Q1answer):
    print ('Sorry, that is incorrect!')
else:
    print ('Well done! ' + Q1response + ' is correct!')
    score = score + 1

print ('Your current score is ' + str(score) + ' out of 10')
print ('\n-----------------------------------------------------------\n')

###########################################################################
#                           QUESTION 2                                    #
###########################################################################

print ('QUESTION 2:What is it called when a function is defined inside a class? \n')
print ('A. Module')
print ('B. Class')
print ('C. Method')
print ('D. Object')
print ('')

Q2answer = "C"
Q2response= input('Your answer : ')

if (Q2response != Q2answer):
    print ('Sorry, that is incorrect!')
else:
    print ('Well done! ' + Q2response + ' is correct!')
    score = score + 1

print ('Your current score is ' + str(score) + ' out of 10') 
print ('\n-----------------------------------------------------------\n')


###########################################################################
#                           QUESTION 3                               #
###########################################################################

print ('QUESTION 3:Which of the following functions will give the total length of a list?\n')
print ('A. Len')
print ('B. len(list)')
print ('C. max(len)')
print ('D. max len(list)')
print ('')

Q3answer = "B"
Q3response= input('Your answer : ')

if (Q3response != Q3answer):
    print ('Sorry, that is incorrect!')
else:
    print ('Well done! ' + Q3response + ' is correct!')
    score = score + 1

print ('Your current score is ' + str(score) + ' out of 10')
print ('\n-----------------------------------------------------------\n')

###########################################################################
#                           QUESTION 4                                 #
###########################################################################

print ('QUESTION 4: Which of the following is defined to catch the exception thrown by the try block?\n')
print ('A. except')
print ('B. import')
print ('C. try')
print('D. None')
print ('')

Q4answer = "A"
Q4response= input('Your answer : ')

if (Q4response != Q4answer):
    print ('Sorry, that is incorrect!')
else:
    print ('Well done! ' + Q4response + ' is correct!')
    score = score + 1

print ('Your current score is ' + str(score) + ' out of 10')
print ('\n-----------------------------------------------------------\n')


###########################################################################
#                           QUESTION 5                                    #
###########################################################################

print ('QUESTION 5: Which of the following is known as an instance of class?\n')
print ('A. Program')
print ('B. Data')
print ('C. Method')
print('D. Object')
print ('')

Q5answer = "D"
Q5response= input('Your answer : ')

if (Q5response != Q5answer):
    print ('Sorry, that is incorrect!')
else:
    print ('Well done! ' + Q5response + ' is correct!')
    score = score + 1

print ('Your current score is ' + str(score) + ' out of 10')
print ('\n-----------------------------------------------------------\n')


###########################################################################
#                           QUESTION 6                                  #
###########################################################################

print ('QUESTION 6: Which core data type in python is an unordered collection of key-value pairs?\n')
print ('A. Tuple')
print ('B. list')
print ('C. Dictionary')
print('D. function')
print ('')

Q6answer = "C"
Q6response= input('Your answer : ')

if (Q6response != Q6answer):
    print ('Sorry, that is incorrect!')
else:
    print ('Well done! ' + Q6response + ' is correct!')
    score = score + 1

print ('Your current score is ' + str(score) + ' out of 10')
print ('\n-----------------------------------------------------------\n')

###########################################################################
#                           QUESTION 7                                  #
###########################################################################

print ('QUESTION 7: Which is the default file access mode?\n')
print ('A. write(w)')
print ('B. append')
print ('C. read(r)')
print('D.none')
print ('')

Q7answer = "C"
Q7response= input('Your answer : ')

if (Q7response != Q7answer):
    print ('Sorry, that is incorrect!')
else:
    print ('Well done! ' + Q7response + ' is correct!')
    score = score + 1

print ('Your current score is ' + str(score) + ' out of 10')
print ('\n-----------------------------------------------------------\n')

###########################################################################
#                           QUESTION 8                                 #
###########################################################################

print ('QUESTION 8: What type of inheritance is illustrated in the following piece of code?\nclass A():\n\tpass\nclass B(A):\n\tpass\nclass C(B):\n\tpass\n')
print ('A. Single inheritance')
print ('B. Multiple inheritance')
print ('C. Hierarchical inheritance')
print('D. Multilevel inheritance')
print ('')

Q8answer = "D"
Q8response= input('Your answer : ')

if (Q8response != Q8answer):
    print ('Sorry, that is incorrect!')
else:
    print ('Well done! ' + Q8response + ' is correct!')
    score = score + 1

print ('Your current score is ' + str(score) + ' out of 10')
print ('\n-----------------------------------------------------------\n')

###########################################################################
#                           QUESTION 9                                #
###########################################################################

print ('QUESTION 9: When is the finally block executed?\n')
print ('A. When there is no exception ')
print ('B. Always')
print ('C. When there is an exception ')
print('D. Only if some condition that has been specified is satisfied')
print ('')

Q9answer = "B"
Q9response= input('Your answer : ')

if (Q9response != Q9answer):
    print ('Sorry, that is incorrect!')
else:
    print ('Well done! ' + Q9response + ' is correct!')
    score = score + 1

print ('Your current score is ' + str(score) + ' out of 10')
print ('\n-----------------------------------------------------------\n')

###########################################################################
#                           QUESTION 10                               #
###########################################################################

print ('QUESTION 10: Which of the following terminates the loop statement and transfers execution to the statement immediately following the loop?\n')
print ('A. break statement ')
print ('B. continue statement ')
print ('C. pass statement')
print('D. None')
print ('')

Q10answer = "A"
Q10response= input('Your answer : ')

if (Q10response != Q10answer):
    print ('Sorry, that is incorrect!')
else:
    print ('Well done! ' + Q10response + ' is correct!')
    score = score + 1

print ('Your current score is ' + str(score) + ' out of 10')
print ('\n-----------------------------------------------------------\n')




print('Total score=' + str(score) + '/15\n')
print('**********************THANK YOU************************')
