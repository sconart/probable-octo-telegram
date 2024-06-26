class Node:
    def __init__(self, element, next_node=None):
        self.element = element
        self.next_node = next_node


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def first(self):
        if self.is_empty():
            return None
        return self.head.element

    def last(self):
        if self.is_empty():
            return None
        return self.tail.element

    def add_first(self, e):
        newest = Node(e, next_node=self.head)
        self.head = newest
        if self.is_empty():
            self.tail = self.head
        self.size += 1

    def add_last(self, e):
        newest = Node(e)
        if self.is_empty():
            self.head = newest
        else:
            self.tail.next_node = newest
        self.tail = newest
        self.size += 1

    def remove_first(self):
        if self.is_empty():
            return None
        answer = self.head.element
        self.head = self.head.next_node
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return answer

    def __eq__(self, other):
        if not isinstance(other, SinglyLinkedList) or self.size != len(other):
            return False

        node1, node2 = self.head, other.head
        while node1 is not None:
            if node1.element != node2.element:
                return False
            node1, node2 = node1.next_node, node2.next_node

        return True

    def __str__(self):
        result = []
        node = self.head
        while node is not None:
            result.append(str(node.element))
            node = node.next_node
        return "(" + ", ".join(result) + ")"

    def clone(self):
        new_list = SinglyLinkedList()
        current = self.head
        while current is not None:
            new_list.add_last(current.element)
            current = current.next_node
        return new_list

    def concatenate(self, list2):
        if self.is_empty():
            self.head = list2.head
            self.tail = list2.tail
        elif not list2.is_empty():
            self.tail.next_node = list2.head
            self.tail = list2.tail
        self.size += list2.size


if __name__ == "__main__":
    L1 = SinglyLinkedList()
    L1.add_first("MSP")
    L1.add_last("ATL")
    L1.add_last("BOS")
    L1.add_first("LAX")
    print(L1)

    L2 = SinglyLinkedList()
    L2.add_first("YYZ")
    L2.add_first("YVR")
    print(L2)

    L = L1.clone()
    L.concatenate(L2)
    print(L1)
    print(L2)
    print(L)
