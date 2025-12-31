# a = 25
# list1 = (1, 2, 3, 4, True, 5.3, "Helo", [1,2,[a],4])

# list1[1] = 650


# print(type(list1))
# print(type(list1[3]))
# print(list1[-1][-2][0], list1[-1])
# print(list1[-1])

# for i in range(0, len(list1)):
#     print(list1[i])

# for i in list1:
#     print(i)

# List Methods

list1 = [1, 2, 3, 4, 4, 5]

# append(element)

list1.append(255)
print("Append : ", list1)

# insert(pos, element)
list1.insert(1, "Hello")
print("Insert :", list1)

# extend
listA = [1, 2, 3, 4, 5]
listB = [6, 7, 8, 9, 10]
listA.extend(listB)
print("Extend :", listA)

# Removing items
list1 = [1, 4, 2, 3, 4, 4, 5, "Hellow"]

list1.remove("Hellow")

print("Remove :", list1)

# Pop

list1.pop()

print("Pop : ", list1)

# Length

print("Length of the List :", len(list1))


list1 = [1, 4, 2, 3, 4, 4, 5]
print("Index :", list1.index(5))


# Reverse
list1.reverse()
print("Reversed List :", list1)

# Sort

list1.sort(reverse=True)
print("Sorted List :", list1)
