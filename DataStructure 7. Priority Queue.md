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
