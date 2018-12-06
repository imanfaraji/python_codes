# File objects

# older way
f = open('test.txt', 'r')
#print (f.mode)
f.close()

# recommended way using context manager -- takes care of closing
with open('test.txt', 'r') as f:
    #f_contents = f.read()
    #print(f_contents)
    #f_contents = f.readlines()
    #print(f_contents)

    #f_content = f.readline()
    #print(f_content)
    #f_content = f.readline()
    #print(f_content)

    #for line in f:
    #    print(line)
    f_content = f.read(10)
    print(f_content)
    #f.seek(5)
    #f_content = f.read(10)
    #print(f.tell())

    #writing  to file

with open('test2.txt', 'w') as f2:
    f2.write("Line1")
    f2.write("Line2")
