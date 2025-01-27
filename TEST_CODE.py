##### Global color variables #####
from colorama import Fore

R = Fore.RED
G = Fore.GREEN
B = Fore.BLUE
W = Fore.RESET
P = Fore.CYAN

'''IF COLORAMA NOT FOUND - ENTER INTO TERMINAL:
pip install colorama'''


##################################

def result(flag):
    if flag:
        return f"{G}PASSED{W}"

    return f"{R}FAILED{W}"


def test_sequence(SinglyLinkedList, corr_sequ):
    try:
        walk = SinglyLinkedList.head
        for el in corr_sequ:
            if el != walk.value:
                return False

            walk = walk.next
        return True

    except:
        return False


def TEST_new_SinglyLinkedList(SinglyLinkedList):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: New SinglyLinkedList Creation{W}\n")

    test = SinglyLinkedList.head == None
    print(f"New SinglyLinkedList head pointer is set to None: {result(test)}")

    test = SinglyLinkedList.tail == None
    print(f"New SinglyLinkedList tail pointer is set to None: {result(test)}")

    sz = SinglyLinkedList._SinglyLinkedList__size
    print(f"New SinglyLinkedList size attribute is private: {result(True)}")

    test = sz == 0
    print(f"Size of new SinglyLinkedList is zero: {result(test)}")

    print("~" * 50, "\n\n")


def TEST_singly_node(SinglyLinkedList):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: The SinglyNode class{W}\n")

    try:
        node1 = SinglyLinkedList().SinglyNode("A")
        print(f"{B}A temporary test node was created: {node1}{W}\n")
        print(f"SinglyNode class is nested within SinglyLinkedList: {result(True)}")

        test = node1.value == "A"
        print(f"SinglyNode value is set properly: {result(test)}")

        test = node1.next == None
        print(f"New SinglyNode next is set to None: {result(test)}\n")

        try:
            node1.set_next("B")
            print(f"SinglyNode next must be of type SinglyNode: {result(False)}")
        except:
            print(f"SinglyNode next must be of type SinglyNode: {result(True)}")

        node2 = SinglyLinkedList().SinglyNode("B")
        node1.set_next(node2)
        test = node1.next == node2 and node1.next.value == "B"
        print(f"SinglyNode set_next works correctly: {result(test)}")

    except:
        print(f"SinglyNode class is nested within SinglyLinkedList: {result(False)}")

    print("~" * 50, "\n\n")


def TEST_head_insert(SinglyLinkedList, class_ref):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: The SinglyLinkedList head_insert{W}\n")

    temp_node = class_ref().SinglyNode("temp")

    SinglyLinkedList.head_insert("A")
    print(f"{B}A node was inserted: {SinglyLinkedList}{W}\n")

    test = type(SinglyLinkedList.head) == type(temp_node)
    print(f"SinglyLinkedList head_insert inserts new SinglyNode object: {result(test)}")

    test = SinglyLinkedList.head.value == "A" and SinglyLinkedList.tail.value == "A"
    print(f"Insert into an empty SinglyLinkedList updates head and tail pointers: {result(test)}")

    test = type(SinglyLinkedList.head) == type(SinglyLinkedList.tail) == type(temp_node)
    print(f"SinglyLinkedList head and tail pointers reference SinglyNode objects: {result(test)}")

    test = len(SinglyLinkedList) == 1
    print(f"SinglyLinkedList head_insert increases size attribute: {result(test)}")

    SinglyLinkedList.head_insert("B")
    print(f"\n{B}A second node was inserted: {SinglyLinkedList}{W}\n")

    test = SinglyLinkedList.head.value == "B" and SinglyLinkedList.tail.value == "A"
    print(f"SinglyLinkedList head_insert into non-empty list updates head pointer only: {result(test)}")

    test = SinglyLinkedList.head.next.value == "A" and SinglyLinkedList.tail.value == "A"
    print(f"Node connections between new head and next element are preserved: {result(test)}")

    for el in "CDE":
        SinglyLinkedList.head_insert(el)

    print(f"\n{B}Many new nodes were inserted: {SinglyLinkedList}{W}\n")

    test = test_sequence(SinglyLinkedList, "EDCBA")
    print(f"Node sequencing is correct, all pointers validated: {result(test)}")

    test = SinglyLinkedList.tail.value == "A" and SinglyLinkedList.tail.next == None
    print(f"SinglyLinkedList head_insert does not impact tail pointer: {result(test)}")

    test = len(SinglyLinkedList) == 5
    print(f"SinglyLinkedList head_insert properly impacts size attribute: {result(test)}")

    print("~" * 50, "\n\n")


def TEST_head_remove(SinglyLinkedList):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: The SinglyLinkedList head_remove{W}\n")

    print(f"{B}Current state of SinglyLinkedList: {SinglyLinkedList}{W}\n")

    val = SinglyLinkedList.head_remove()
    print(f"{B}Head element |{val}| was removed: {SinglyLinkedList}{W}\n")

    test = type(val) == str
    print(f"SinglyLinkedList head_remove returns node value, not SinglyNode object: {result(test)}")

    test = val == "E"
    print(f"SinglyLinkedList head_remove returns correct value: {result(test)}")

    test = SinglyLinkedList.head.value == "D"
    print(f"SinglyLinkedList head_remove affects SinglyLinkedList head pointer: {result(test)}")

    test = len(SinglyLinkedList) == 4
    print(f"SinglyLinkedList head_remove decreases list size: {result(test)}")

    test = test_sequence(SinglyLinkedList, "DCBA")
    print(f"Node sequencing is correct, all pointers validated: {result(test)}")

    for i in range(4):
        SinglyLinkedList.head_remove()

    print(f"\n{B}SinglyLinkedList emptied with head_remove: {SinglyLinkedList}{W}\n")

    try:
        SinglyLinkedList.head_remove()
        print(f"Remove from empty SinglyLinkedList raises exception: {result(False)}")
    except:
        print(f"Remove from empty SinglyLinkedList raises exception: {result(True)}")

    test = len(SinglyLinkedList) == 0 and SinglyLinkedList.head == None and SinglyLinkedList.tail == None
    print(f"Emptied SinglyLinkedList resets head and tail pointers to None: {result(test)}")

    print("~" * 50, "\n\n")


def TEST_tail_insert(SinglyLinkedList, class_ref):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: The SinglyLinkedList tail_insert{W}\n")

    print(f"{B}Current state of SinglyLinkedList: {SinglyLinkedList}{W}\n")

    temp_node = class_ref().SinglyNode("temp")

    SinglyLinkedList.tail_insert("A")
    print(f"{B}A node was inserted: {SinglyLinkedList}{W}\n")

    test = type(SinglyLinkedList.head) == type(temp_node)
    print(f"SinglyLinkedList tail_insert inserts new SinglyNode object: {result(test)}")

    test = SinglyLinkedList.head.value == "A" and SinglyLinkedList.tail.value == "A"
    print(f"Insert into an empty SinglyLinkedList updates head and tail pointers: {result(test)}")

    test = type(SinglyLinkedList.head) == type(SinglyLinkedList.tail) == type(temp_node)
    print(f"SinglyLinkedList head and tail pointers reference SinglyNode objects: {result(test)}")

    test = len(SinglyLinkedList) == 1
    print(f"SinglyLinkedList tail_insert increases size attribute: {result(test)}")

    SinglyLinkedList.tail_insert("B")
    print(f"\n{B}A second node was inserted: {SinglyLinkedList}{W}\n")

    test = SinglyLinkedList.tail.value == "B" and SinglyLinkedList.head.value == "A"
    print(f"SinglyLinkedList tail_insert into non-empty list updates tail pointer only: {result(test)}")

    test = SinglyLinkedList.head.next.value == "B" and SinglyLinkedList.tail.value == "B"
    print(f"Node connections between new head and next element are preserved: {result(test)}")

    for el in "CDE":
        SinglyLinkedList.tail_insert(el)

    print(f"\n{B}Many new nodes were inserted: {SinglyLinkedList}{W}\n")

    test = test_sequence(SinglyLinkedList, "ABCDE")
    print(f"Node sequencing is correct, all pointers validated: {result(test)}")

    test = SinglyLinkedList.tail.next == None
    print(f"SinglyLinkedList tail_insert does not set_next for new node: {result(test)}")

    test = len(SinglyLinkedList) == 5
    print(f"SinglyLinkedList tail_insert properly impacts size attribute: {result(test)}")

    print("~" * 50, "\n\n")


def TEST_head_tail_insert(SinglyLinkedList, class_ref):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: The SinglyLinkedList head_insert & tail_insert{W}\n")

    temp_node = class_ref().SinglyNode("temp")
    for el in range(len(SinglyLinkedList)):
        SinglyLinkedList.head_remove()

    print(f"{B}SinglyLinkedList has been emptied: {SinglyLinkedList}{W}\n")

    for i, let in enumerate("ABCDEF"):
        if i % 2 == 0:
            SinglyLinkedList.head_insert(let)
        else:
            SinglyLinkedList.tail_insert(let)

    print(f"{B}Elements added to SinglyLinkedList with both insert methods: {SinglyLinkedList}{W}\n")

    test = type(SinglyLinkedList.head) == type(SinglyLinkedList.tail) == type(temp_node)
    print(f"SinglyLinkedList was populated with SinglyNode objects: {result(test)}")

    test = SinglyLinkedList.head.value == "E" and SinglyLinkedList.tail.value == "F"
    print(f"Head and tail values are correct: {result(test)}")

    test = len(SinglyLinkedList) == 6
    print(f"Insert methods affect size correctly: {result(test)}")

    test = SinglyLinkedList.tail.next == None
    print(f"Tail node has no next: {result(test)}")

    test = test_sequence(SinglyLinkedList, "ECABDF")
    print(f"Node sequencing is correct, all pointers validated: {result(test)}")

    print("~" * 50, "\n\n")


def TEST_docs(SinglyLinkedList, class_ref):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Docstrings{W}\n")

    print("SinglyNode Class Docstrings:\n")
    doc = class_ref.SinglyNode.set_next.__doc__
    if doc != None:
        print(f"{B}set_next() Documentation:{W} {doc}\n")
    else:
        print(f"{R}set_next() Documentation Missing{W}\n")

    doc = class_ref.SinglyNode.__str__.__doc__
    if doc != None:
        print(f"{B}str() Documentation:{W} {doc}\n")
    else:
        print(f"{R}str() Documentation Missing{W}\n")

    print("\n\nSinglyLinkedList Class Docstrings:\n")
    doc = SinglyLinkedList.head_insert.__doc__
    if doc != None:
        print(f"{B}head_insert() Documentation:{W} {doc}\n")
    else:
        print(f"{R}head_insert() Documentation Missing{W}\n")

    doc = SinglyLinkedList.tail_insert.__doc__
    if doc != None:
        print(f"{B}tail_insert() Documentation:{W} {doc}\n")
    else:
        print(f"{R}tail_insert() Documentation Missing{W}\n")

    doc = SinglyLinkedList.head_remove.__doc__
    if doc != None:
        print(f"{B}head_remove() Documentation:{W} {doc}\n")
    else:
        print(f"{R}head_remove() Documentation Missing{W}\n")

    doc = SinglyLinkedList._SinglyLinkedList__is_empty.__doc__
    if doc != None:
        print(f"{B}is_empty() Documentation:{W} {doc}\n")
    else:
        print(f"{R}is_empty() Documentation Missing{W}\n")

    doc = SinglyLinkedList.__len__.__doc__
    if doc != None:
        print(f"{B}len() Documentation:{W} {doc}\n")
    else:
        print(f"{R}len() Documentation Missing{W}\n")

    doc = SinglyLinkedList.__str__.__doc__
    if doc != None:
        print(f"{B}str() Documentation:{W} {doc}\n")
    else:
        print(f"{R}str() Documentation Missing{W}\n")

    print("~" * 50, "\n\n")