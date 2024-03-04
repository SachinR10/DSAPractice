from queueDS import QueueDS

Q1 = QueueDS()

Q1.push(10)
Q1.push(20)
Q1.push(30)
Q1.push(40)

print(Q1.get_length())
print(Q1.pop())
print(Q1.get_length())
