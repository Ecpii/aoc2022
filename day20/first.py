with open("input.txt") as inp:
    numbers = list(map(int, inp.read().split('\n')[:-1]))


class Node:
    def __init__(self, datum):
        self.next = None
        self.prev = None
        self.datum = datum


class CircList:
    def __init__(self, input_list):
        self.head = Node(input_list[0])
        self.tail = Node(input_list[1])
        self.tail.prev = self.head
        self.head.next = self.tail
        self.original_order = [self.head, self.tail]

        for number in input_list[2:]:
            inductee = Node(number)
            self.tail.next = inductee
            inductee.prev = self.tail
            self.tail = inductee
            self.original_order.append(self.tail)

        self.head.prev = self.tail
        self.tail.next = self.head

    def __str__(self):
        res = ""
        curr = self.head
        while curr != self.tail:
            res += str(curr.datum) + ", "
            curr = curr.next
        res += str(self.tail.datum)
        return res

    def __len__(self):
        return len(self.original_order)

    def find(self, value):
        curr = self.head
        while curr.datum != value:
            curr = curr.next
        return curr

    def get_node_from(self, node, dist):
        dist %= len(self)
        target = node
        for _ in range(dist):
            target = target.next
        return target

    def move(self, node):
        num_places = node.datum % (len(self) - 1)
        if not num_places:
            return

        node.prev.next = node.next
        node.next.prev = node.prev
        target_node = node
        if self.head == node:
            self.head = node.next
            if num_places == 1:
                node.next = self.head.next
                self.head.next.prev = node
                node.prev = self.head
                self.head.next = node
                return

        elif self.tail == node:
            self.tail = self.head
            self.head = self.head.next
            if num_places == 1:
                node.next = self.tail.next
                self.tail.next.prev = node
                node.prev = self.tail
                self.tail.next = node
                self.head = node
                return

        for _ in range(num_places):
            target_node = target_node.next

        node.next = target_node.next
        target_node.next.prev = node
        node.prev = target_node
        target_node.next = node
        if target_node == self.head:
            self.head = node
            self.tail = target_node
        elif target_node == self.tail:
            self.tail = node

    def apply_key(self, key):
        curr = self.head
        while curr != self.tail:
            curr.datum *= key
            curr = curr.next
        curr.datum *= key

    def mix(self):
        for orig_node in self.original_order:
            self.move(orig_node)


file = CircList(numbers)
file.apply_key(811589153)
for _ in range(10):
    file.mix()

print(sum((
    file.get_node_from(file.find(0), 1000).datum,
    file.get_node_from(file.find(0), 2000).datum,
    file.get_node_from(file.find(0), 3000).datum
)))
