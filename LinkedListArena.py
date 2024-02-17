from LinkedList import LinkedList

L = LinkedList()

L.insert_at_begining(10)
L.insert_at_begining(20)
L.insert_at_end(30)
L.insert_at_end(40)
print(L.Length)
L.print()

L.remove_by_value(20)
L.remove_by_value(40)
L.remove_by_value(10)
print(L.Length)
L.print()
