numbers= [5, 2, 1, 7, 4]
numbers.append(20)
print(numbers)

numbers= [5, 2, 1, 7, 4]
numbers.insert(0, 10)
print(numbers)

numbers= [5, 2, 1, 7, 4]
numbers.remove(5)
print(numbers)

numbers= [5, 2, 1, 7, 4]
numbers.clear()
print(numbers)

numbers= [5, 2, 1, 7, 4]
numbers.pop() #to remove the end of our list
print(numbers)

numbers= [5, 2, 1, 7, 4]
print(numbers.index(5))

numbers= [5, 2, 1, 7, 4]
print(50 in numbers) #to check the existence of 50 in the list

numbers= [5, 2, 1, 5, 7, 4]
print(numbers.count(5))

numbers= [5, 2, 1, 5, 7, 4]
numbers.sort() #ascending order
numbers.reverse() #descending order
print(numbers)

numbers= [5, 2, 1, 5, 7, 4]
numbers2 = numbers.copy()
numbers.append(10)
print(numbers2)