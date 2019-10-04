# Linked-list simple implementation 

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
