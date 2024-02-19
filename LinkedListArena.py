from LinkedList import LinkedList

L = LinkedList()

print(L.Length)
L.print()

L2 = LinkedList()

L2.extend(L)
print(L2.Length)
L2.print()

L2.revese()
L2.print()
