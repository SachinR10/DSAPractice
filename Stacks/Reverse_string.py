from Stack import Stack

inputString = "sachin"
s = Stack(capacity=len(inputString))
for i in inputString:
    s.push(i)

revString = ""
while s.get_length()!=0:
    revString +=s.pop()

print(inputString)
print(revString)
