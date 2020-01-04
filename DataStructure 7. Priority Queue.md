# Definition
1. Every item has a priority associated with it.  
2. An element with high priority is dequeued before an element with low priority.  
3. If two elements have the same priority, they are served according to their order in the queue.  


# Example
在python的built-in library中提供的heap queue，类似一个list  
但是这个list每次append之后都会自动排序，让top priority的element排在第0位，方便下一次pop  
**官方说明：**  
这个API与教材的堆算法实现有所不同，具体区别有两方面：  
（a）我们使用了从零开始的索引。这使得节点和其孩子节点索引之间的关系不太直观但更加适合，因为 Python 使用从零开始的索引。   
（b）我们的 pop 方法返回最小的项而不是最大的项

# Common Operations
先初始化一个list：heap = []

heapq.heappush(heap, item)
将 item 的值加入 heap 中，保持堆的不变性。  

heapq.heappop(heap)
弹出并返回 heap 的最小的元素，保持堆的不变性。如果堆为空，抛出 IndexError 。使用 heap[0] ，可以只访问最小的元素而不弹出它。

heapq.heappushpop(heap, item)
将 item 放入堆中，然后弹出并返回 heap 的最小元素。该组合操作比先调用  heappush() 再调用 heappop() 运行起来更有效率。
