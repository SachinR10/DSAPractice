from Stack import Stack

paranString = "((("

s = Stack(capacity=len(paranString))

for i in paranString:
    if s.get_length()==0:
        s.push(i)
        continue
    if s.peek()==i:
        s.push(i)
    else:
        s.pop()
    
if s.get_length()==0:
    print("paranthesis is perfect!")
else:
    print("Prarnthesis is mismatched!!")


