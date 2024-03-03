from Stack import Stack

s1 = Stack(capacity=6)

s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.push(50)
s1.push(60)
s1.printStack()
print(s1.pop())
s1.printStack()
print(s1.get_length())
print(s1.pop())
print(s1.pop())
print(s1.pop())
s1.printStack()
print(s1.get_length())
