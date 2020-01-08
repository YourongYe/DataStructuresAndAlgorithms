# Hash Table vs List
hash table is built based on a list.   
他们都是属于单边映射，hashtable 是从key->value, 而list是从 index->value  
本质上来讲，hashtable属于特殊的list，因为他的key不需要从0开始，也可以不连贯，甚至可以不是数字。  
从这点看，hashtable其实就是一种可以随意定义index的list。

另外，hashtable是无序的，而list是有序的。其实如果hashtable的index是数字，我们是可以通过sort keys来让它有序的。  
但由于hashtable的特殊性，keys可以设定成任何一个immutable的value，所以如果有的key是数字，有的是字母则没法排序。

# 常见题型
hashtable有一种常见题型就是，先count或者统计，然后需要以value来排序。由于hashtable的单边映射性质，这样的题一个hashtable理论上是  
没法做出来的（当然现在有一些python built-in library是可以的）。所以这个时候我们需要借助另一个data structure来辅助实现hashtable的 value sort  
和双边映射。

要想达到双边映射的效果，最简单的方式就是，再来一个hashtable，把原来的key和value进行对调。  
当然还有其他的方式，如果是要sort value，可以用bucket sort。

bucket sort的本质是用一个空的list，根据elements的某种属性来放置，然后再依次把list 里的值提出来。
