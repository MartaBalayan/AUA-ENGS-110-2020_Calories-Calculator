        #Test for Single Linked List

        List_Test = SingleLinkedList()
        List_Test.AtBeginning("Jan")
        List_Test.AtEnd("Feb")
        List_Test.AtEnd("March")
        List_Test.AtEnd("May")
        List_Test.InsertAfter(List_Test.HeadValue.NextValue.NextValue, "April")
        List_Test.ListPrint()
        List_Test.RemoveNode("Jan")
        List_Test.ListPrint()
        print("First element: ", List_Test.FirstElement())
        print("Last element: ", List_Test.LastElement())
        print("Size: ", List_Test.Size())

        #Tests for Double Linked List

        double_test = DoubleLinkedList()
        double_test.addFirst("Jan")
        double_test.addLast("Feb")
        double_test.addFirst("March")
        double_test.addLast("April")
        double_test.addFirst("May")
        double_test.addFirst("June")
        double_test.addLast("July")
        double_test.addLast("August")
        double_test.listprint()
        double_test.RemoveFirst()
        double_test.InsertAfter(double_test.HeadVal.NextValue,"Jan")
        double_test.RemoveLast()
        double_test.RemoveNode("March")
        double_test.listprint()

        #Tests for Stack

        stack_test = Stack()
        stack_test.AddElement("Jan")
        stack_test.AddElement("Feb")
        stack_test.AddElement("March")
        stack_test.PrintStack()
        stack_test.RemoveElement()
        stack_test.PrintStack()

        #Tests for Queue

        queue_test = QueueArray(2)
        queue_test.add("Jan")
        queue_test.add("Feb")
        queue_test.add("March")
        queue_test.print_deq()
        queue_test.remove()
        queue_test.print_deq()

        #Tests for Deque

        deque_test = DequeArray(3)
        deque_test.addFirst("Jan")
        deque_test.addFirst("Feb")
        deque_test.addLast("March")
        deque_test.addLast("April")
        deque_test.addLast("May")

        deque_test.print_deque()
        deque_test.removeLast()
        deque_test.removeFirst()
        deque_test.print_deque()
        print("First element: ", deque_test.first())
        print("Last element: ", deque_test.last())
        print("Last non-none index: ", deque_test.last_index())

        #Tests for HashMap

        addressBook = HashMap()
        addressBook.put("Marta", {"fullName": "Marta Balayan",
                                  "phoneNumber": "097777777"})
        addressBook.put("Ani", {"fullName": "Ani Artashesyan",
                                  "phoneNumber": "097777771"})
        addressBook.put("Susanna", {"fullName": "Susanna Harutyunyan",
                                "phoneNumber": "097777772"})
        addressBook.put("Mane", {"fullName": "Mane Stepanyan",
                                  "phoneNumber": "097777773"})
        addressBook.put("Armen", {"fullName": "Armen Gasparyan",
                                  "phoneNumber": "097777774"})
        addressBook.put("Levon", {"fullName": "Levon Malyan",
                                  "phoneNumber": "097777775"})

        print("Address Book")
        for element in addressBook:
            print(element.get("fullName"))

        print()
        addressBook.remove("Movses")
        addressBook.remove("Levon")
        print("")
        print("Updated Address Book")
        for element in addressBook:
            print(element.get("fullName"))

        print()
        print("Checking presence of key")
        addressBook.hasKey("Ani")
        addressBook.hasKey("Mesrop")
        print()
        print("Size of HashMap")
        print(addressBook.size())

        #Tests for HashSet
        HS = HashSet(5)
        print("Hashing of elements")
        HS.add("Monday")
        HS.add("Tuesday")
        HS.add("Wednesday")
        HS.add("Thursday")
        HS.add("Friday")
        print("Elements of HashSet")
        HS.print()
        print("Current size of HashSet current size")
        print(HS.size())
        HS.remove("Friday")
        print("HashSet after removing Friday")
        HS.print()
        print("Current size of HashSet current size")
        print(HS.size())