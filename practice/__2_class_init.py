class Node:
    def __init__ (self, d=None, n=None):
        self.data = d
        self.next = n
    def get_data (self):
        return self.data
    def get_next (self):
        return self.next
    def set_next (self, new_n):
        self.next = new_n



class Linklist(object):
    def __init__ (self, h=None):
        self.head = h
    def insert_first(self, d):
        new_node = Node(d)
        new_node.set_next (self.head)
        self.head = new_node

    def insert_last(self, d):
        current = self.head
        while (current.next != None):
            current = current.get_next()
        new_node = Node(d)
        current.set_next(new_node)

    def traverse(self):
        current = self.head
        while (current != None):
            print (current.get_data())
            current = current.get_next()
    def count(self):
        current = self.head
        count = 0
        while (current != None):
            count += 1
            current = current.get_next()
        print(count)
    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found == False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
    def search(self, val):
        current = self.head
        count = 0
        while (current != None ):
            if (current.get_data() == val):
                print ("Found value: "+ str(val) + " in position: " + str(count) )
                break
            else:
                current = current.get_next()
                count += 1

n1 = Node(10)
L1 = Linklist(n1)
L1.insert_last(20)
L1.insert_last(30)
L1.insert_last(31)
L1.insert_last(32)
L1.insert_last(40)
L1.traverse()
L1.count()
L1.delete(30)
L1.traverse()
L1.search(31)
