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

head = Node(4,(Node(2, Node(1, Node(5, Node(3))))))

def reverse_linked_list(head, tail = None):
    while head:
        head.next, tail, head = tail, head, head.next
    return tail

def bub_sort(head):
    head2 = head
    cur = head.value
    main = head.next # скорее всего здесь ошибка, не понимаю как исправить
    main2 = main.value
    while head2 is not None:
        if cur > main2:
            cur, main2 = main2, cur
            cur = main


bub_sort(head)
print_linked_list(head)
print('---')
print_linked_list(reverse_linked_list(head))
