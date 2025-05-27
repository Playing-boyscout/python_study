from ast import Add, Set, comprehension


numbers=(11,12,13,14,15)
numbers=list(numbers)
numbers.append(16)
print(numbers)
numbers[2]=19
print(numbers)
numbers=tuple(numbers)
print(numbers)

#Arrange in ascending order
values=(15,5,30,25,10)
values=list(values)
values.sort()
print(values)
values.sort(reverse=True)
values=tuple(values)
print(values)

#count and removing occurences of banana
fruits=("apple","banana","cherry","banana","mango","banana",)
banana_count=fruits.count("banana")
print(banana_count)
fruits=list(fruits)
fruits.remove("banana")
print(fruits)
fruits.remove("banana")
print(fruits)
fruits.remove("banana")
print(tuple(fruits))

#method 2 of the above process
fruits=("apple","banana","cherry","banana","mango","banana",)
banana_count=fruits.count("banana")
print(banana_count)
fruits=list(fruits)
filter_banana=list(filter(lambda fruits: fruits !="banana",fruits))
print(filter_banana)

#reversing the order
names=("Alice","Bob","Charlie","David")
names=list(names)
print(names)
names=names[::-1]
print(tuple(names))

#adding and extending
colors=("red","blue","green")
colors=list(colors)
colors.insert(1, "yell0w")
print(colors)
colors.extend(["purple","orange"])
print(colors)