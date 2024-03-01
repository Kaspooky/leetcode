class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


l1 = ListNode()
l1.val = 2
l1.next = ListNode(val=4)
l1.next.next = ListNode(val=3)

l2 = ListNode(val=5)
l2.next = ListNode(val=6)
l2.next.next = ListNode(val=4)

List1 = []
List2 = []

while True:
    List1.append(l1.val)
    l1 = l1.next
    if l1.next == None:
        List1.append(l1.val)
        break

while True:
    List2.append(l2.val)
    l2 = l2.next
    if l2.next == None:
        List2.append(l2.val)
        break

print(List1)
print(List2)
List3 = []
carry = 0
for i in range(min(len(List1), len(List2))):
    value = List1[i] + List2[i] + carry
    carry = 0
    if value >= 10:
        carry = 1
        value %= 10
    List3.append(value)

for i in range(min(len(List1), len(List2)), max(len(List1), len(List2))):
    print()

print(List3)
