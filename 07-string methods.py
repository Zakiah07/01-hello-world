course = 'Python for Beginners'
print(len(course)) #len function, general purpose function
print(course.upper()) #method and strings, creates a new string and return it
print(course.lower())
print(course.find('P')) #find method is case sensitive, if put capital O, it will return -1 bcos capital O does not exist in the string above
print(course.replace('Beginners', 'Absolute Beginners')) # replace method, case sensitive
print('Python' in course) #to check if python is in the course variable, case sensitive
#Will produces a boolean value like true or false