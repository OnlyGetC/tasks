class Node(object):
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node

    def __str__(self):
        return f"[Node with value {self.value}]"

def print_linked_list(head):
    cur = head
    while cur is not None:
        print(cur)
        cur = cur.next
head = Node(1,(Node(2, Node(3, Node("внезапно", Node(5))))))

def reverse_linked_list(head, tail = None):
    while head:
        head.next, tail, head = tail, head, head.next
    return tail

print_linked_list(head)
print('---')
print_linked_list(reverse_linked_list(head))
print('ffe')