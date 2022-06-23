def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')


print("Start")
greet_user(first_name = "John", last_name="Smith")
print("Finish")

#first_name = "John" is keyword argument, position doesn't matter if we put keyword arguments
#keyword arguments always come after positional arguments