# Link list

# define Node object
class Node:
    def __init__(self, d=None, next_node=None):
        self.data = d
        self.next = next_node #next is of type Node
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_next(self, new_node):
        self.next = new_node


# Define LinkedList object
class LinkedList:
    def __init__(self, head=None): # LinkedList requires a head node
        self.head = head # LL can init by a node or None as its head
    def insert_first(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
    def traverse(self):
        current_node = self.head
        while (current_node != None):
            print (current_node.get_data())
            current_node = current_node.get_next()
    def insert_last(self, data):
        new_node = Node(data)
        current = self.head
        if (current == None):
            self.head = new_node
        else:
            while (current.get_next() != None):
                current = current.get_next()
            current.set_next(new_node)
    def search(self, data):
        current = self.head
        if (current == None):
            raise ValueError("Searching an Empty list")
        else:
            position = 0
            while (current != None):
                if (current.get_data() == data):
                    print("FOUND AT " + str(position))
                    return
                else:
                    current = current.get_next()
                    position = position + 1
            print ("Not Found")
    def delete(self, data): # 3 cases to consider:
        current = self.head
        if (current == None): ## 1. list empty
            raise ValueError("Deleting from empty list")
        elif (current.get_data() == data): ## 2. first emement matched
            self.head = current.get_next()   ## just replace it with next
        else:
            while (current.get_next() != None): ## 3. element after mathced
                if (current.get_next().get_data() == data):
                    current.set_next(current.get_next().get_next())
                    return
                else:
                    current = current.get_next()
            raise ValueError("Data does not exist in LinkedList")

#remove duplicates using dictionary
    def remove_dup(self):
        els = []
        node = self.head
        previous = None
        while node != None:
            if node.get_data() in els:
                previous.set_next(node.get_next())
            else:
                els.append(node.get_data())
            previous = node
            node = node.get_next()
    def count(self):
        current = self.head
        count = 0
        while (current != None):
            count += 1
            current = current.get_next()
        return count
    def pick(self, num):
        current = self.head
        if num == 1:
            return current.get_data()
        while (num != 1):
            num -= 1
            current = current.get_next()
        return current.get_data()







############# Testbench
N1 = Node(10)
L1 = LinkedList(N1)
L1.insert_first(10)
L1.insert_first(20)
L1.insert_last(30)
L1.insert_last(40)
L1.insert_last(50)

#L1.traverse()

#L1.search(59)

#L1.delete(40)
#L1.delete(69)

L1.traverse()
#L1.remove_dup()
#L1.traverse()
cnt = L1.count()
print("\n\n")

mydata = L1.pick(cnt-4)
print(str(mydata))
