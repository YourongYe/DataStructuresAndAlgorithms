# Linked-list simple implementation 
## C++ implementation
## Python implementation

# Recursion 
## Stack (extra memory)
## Iteration (in-place)
## Recursion (stack)
## Recursion (iteration)

# Linked-list simple implementation 

## C++ version
```cpp
#include <iostream>
#include <string>

int main()
{
    struct Node{
        int data;
        Node* link;
    }; 
    
    Node* temp = new Node();
    Node* A = temp;
    
    for(int i=1; i<=5; i++)
    {
        temp->data = i;
        temp->link = new Node();
        temp = temp->link;
    }
    
    Node* temp1 = A;
    while(temp1->link!=NULL)
    {
        std::cout<<temp1->data<<std::endl;
        temp1 = temp1->link;
    }
    
}
```

## Result
```cpp
1
2
3
4
5
```

## Python version
因为python中没有pointer的概念，所以指向head的pointer会用一个空的node来代替，也就是说每次循环的时候都是从空的node开始

```py
class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        cur = self.head 
        while cur.next != None: # 注意这里的cur是current node，不是pointer，和C++不同，所以一定要判断成cur.next是否为空，而不是cur本身
            cur = cur.next
        cur.next = new_node

    def traverse(self):
        cur = self.head
        while cur.next != None:
            cur = cur.next
            print(cur.data)

    def get(self, index):
        cur = self.head
        while index:
            cur = cur.next
            index -= 1
        return cur.data

    def erase(self, index):
        cur = self.head
        while index + 1:
            last_node = cur
            cur = cur.next
            index -= 1
        last_node.next = cur.next
```
## Result
```py
1
2
5
4
2
1
2
4
```
# Reverse Linked List
## using stack
```py
def reverseList(self, head: ListNode) -> ListNode:
    l1 = []
    temp = head
    while temp != None:
        l1.append(temp.val)
        temp = temp.next
    temp = head
    while temp != None:
        temp.val = l1.pop()
        temp = temp.next
    return head
        
```

## using pointers and in-place reverse
```py
def reverseList(self, head: ListNode) -> ListNode:
    curr = head
    next = curr
    prev = None
    while curr != None:
        next = next.next
        curr.next = prev
        prev = curr
        curr = next
    head = prev
    return head
```

## recursion (stack思路)
```py
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            newhead = head
            return newhead
        newhead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newhead
```

## recursion (iteration类似思路)
```py

```
        
