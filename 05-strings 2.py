course = 'Python for Beginners'
print(course[0:3]) #square bracket syntax works like below stat
#01234,if -1, it will go to last letter of the sentence
#if 0:3, python interprets up until the index before it.
#if start index is 0: , all the sentence will be interpreted
#if we put 1: , first letter is excluded but not the rest of the sentence
#if put  :5, python will assume first index starts from 0

course = 'Python for Beginners'
another= course[:] #square bracket syntax
print(another)