from LinkedListWithHeadAndTail import LinkedList

LL = LinkedList()

LL.append(100)
LL.append("hellow")
LL.append("!@#")
LL.append(200)

LL.printLL()
print(LL.GetLength())
print("_-_"*50)

LL.delete("!@#")
LL.printLL()
print(LL.GetLength())
print("_-_"*50)

LL.delete("1442")
LL.printLL()
print(LL.GetLength())
print("_-_"*50)


