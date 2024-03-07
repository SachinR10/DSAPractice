from DoublyLinkedList import DoublyLinkedList

DLL1 = DoublyLinkedList()

DLL1.insert_at_begining(10)
DLL1.insert_at_end(20)
DLL1.insert_at_begining(5)
DLL1.insert_at_end(25)
DLL1.insert_at_end(30)
DLL1.print()
print(DLL1.Length)

DLL1.remove_value(5)
DLL1.remove_value(30)
DLL1.remove_value(20)
DLL1.remove_value(10)
DLL1.remove_value(25)
DLL1.print()
print(DLL1.Length)

