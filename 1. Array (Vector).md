# Array 基本写法
```cpp

#include <iostream>
#include <string>


int main()
{
    int A[6]; // initialisation
    for (int i=1; i<=6; i++){
        A[i-1]=i;
        }

    double B[] = {1.2,2.3,3.4}; // initialisation without specifying size, it'll allocate the exact size to the array
    A[2] = 100; // modify the third element

    std::cout<<B[2]<<std::endl;

    int i = 0;
    while (i<6){
        std::cout<<A[i]<<',';
        i++;
        }
}
```

注意：array是C++里非常原始的一种数据结构，初始化之后size不能改，没有insert和push_back，也没有remove。  
但可以修改元素，可以比vector更快速访问元素
