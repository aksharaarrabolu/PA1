import random
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def count_larger_than_50(self):
        count = 0
        current = self.head
        while current:
            if current.data > 50:
                count += 1
            current = current.next
        return count

    def sort_and_delete_second(self):
        if self.head is None or self.head == self.tail:
            return
        sorted_list = sorted(self.to_list(), reverse=True)
        self.head = self.tail = None
        for item in sorted_list:
            self.insert(item)
        second_node = self.head.next
        if second_node:
            self.head.next = second_node.next
            if second_node.next:
                second_node.next.prev = self.head

    def insert_sorted(self, data):
        current = self.head
        while current and current.data > data:
            current = current.next
        if current is None:
            self.insert(data)
        else:
            new_node = Node(data)
            new_node.prev = current.prev
            new_node.next = current
            if current.prev:
                current.prev.next = new_node
            else:
                self.head = new_node
            current.prev = new_node

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

def main():
    m = int(input("Enter the upper bound 'm': "))
    r = int(input("Enter the number of repetitions 'r': "))
    n_values = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000]

    for n in n_values:
        for _ in range(r):
            linked_list = DoublyLinkedList()
            for _ in range(n):
                linked_list.insert(random.randint(1, m))
            
            count_larger_50 = linked_list.count_larger_than_50()

            if count_larger_50 > 5:
                linked_list.sort_and_delete_second()
            else:
                linked_list.sort_and_delete_second()
                linked_list.sort_and_delete_second()

            linked_list.insert_sorted(10)

        if n <= 100:
            print(f"n={n}: {linked_list.to_list()}")
    
if __name__ == "__main__":
    main()
