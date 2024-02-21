from DoublyLinkedList import DoublyLinkedList

DLL1 = DoublyLinkedList()

DLL1.insert_at_begining(10)
DLL1.insert_at_end(20)
DLL1.insert_at_begining(5)
DLL1.insert_at_end(25)
DLL1.insert_at_end(30)
DLL1.print()
print(DLL1.Length)

DLL1.insert_at(3,123)
DLL1.print()
print(DLL1.Length)

