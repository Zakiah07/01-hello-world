from pathlib import Path

#Absolute path - start from the root of our hardisk like c drive, backslash \
#Relative path - a path starting from current directory

#from the ecommerce directory, 
# path = Path("ecommerce")
# print(path.exists()) , to check if the path is exist, return True

# path = Path("emails")
# print(path.mkdir()) , return None #mkdir is make directory
# rmdir is remove directory, return the None
# glob('*'), glob method

# path = Path()
# print(path.glob('*.*'))
# *, get the files in current directory...put *. for the extension
# '*.py' or '*.xls' to find excel file

path = Path()
for file in path.glob('*.py'):
    print(file)