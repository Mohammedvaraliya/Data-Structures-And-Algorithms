class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def hasCycle(self, pos):
        slow, fast = self.head, self.head

        node = self.head
        for _ in range(pos):
            node = node.next

        # Connect the last node to the pos node
        last_node = llist.head
        while last_node.next:
            last_node = last_node.next
        
        last_node.next = node

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False



if __name__ == "__main__":

    llist = SinglyLinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(0)
    llist.append(-4)

    llist.print_list()
    print("\n")

    print(llist.hasCycle(1))
    

    