# List

list1 = [1, 2, 3]
list2 = ["apple", "orange"]

list3 = list2

print (list3[-1][-1])

if "orange" in list3:
    print (list3.index("orange"))
else:
    print("not found")

list2.append("grape")
print(list2)
list2.insert(1,"kiwi")
print(list2)
list2.remove("apple")
print(list2)
list2.sort()
print (list2)
list2.insert(0,"apple")
print (list2)
