class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtFront(self, val):
        new_node = Node(val)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node
        return self.head

    def insertAtBack(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def insertAfter(self, val, loc):
        if loc is None:
            return

        new_node = Node(val)
        new_node.next = loc.next
        loc.next = new_node
        new_node.prev = loc

        if new_node.next is not None:
            new_node.next.prev = new_node

    def deleteFront(self):
        if self.head is None:
            return None

        new_head = self.head.next
        if new_head is not None:
            new_head.prev = None
        deleted_node = self.head
        self.head = new_head
        return deleted_node

    def deleteBack(self):
        if self.head is None:
            return

        current = self.head
        while current.next is not None:
            current = current.next
        if current.prev is not None:
            current.prev.next = None

    def deleteNode(self, loc):
        if loc is None or self.head is None:
            return None

        if loc.prev is not None:
            loc.prev.next = loc.next
        else:
            self.head = loc.next

        if loc.next is not None:
            loc.next.prev = loc.prev

    def length(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def reverseIterative(self):
        prev_node = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = prev_node
            current.prev = next_node
            prev_node = current
            current = next_node

        self.head = prev_node

    # def reverseRecursive(self)
