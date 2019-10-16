厲彥伯的GitHub
=====
# 目錄
>* [Python語法](#Python語法)  
>   * [list語法](#list語法)
>   * [for迴圈語法](#for迴圈語法)
>   * [zip用法](#zip用法)
>   * [Numpy套件](#Numpy套件)
>* [Esclipse(Java)語法](#Esclipse(Java)語法)
>* [R語言](#R語言)
>* [C++環境視窗程式設計](#C++環境視窗程式設計)
>* [GitHub使用方法](#GitHub使用方法)
>* [LeeCode練習筆記](#LeeCode練習筆記)
>* [HomeWork](#HomeWork)
>   * [快速排序法](#快速排序法)
>     * [Quick Sort](#QuickSort)
>     * [Quick Sort Inplace](#QuickSort_Inplace)

---------------
## Python語法
### list語法 

remove用法
```python
a = [1, 3, 5, 3, 7]
a.remove(3) #remove只會刪除括號內第一個出現的指定的數值
a
```
回傳結果a會變成[1, 5, 3, 7]

pop用法
```python
b = [1, 2, 3, 1, 2, 3]
b.pop(2) #pop會回傳位於括號內的數值，並且刪除該數值，如果括號內為空，刪除並回傳最後一個數值
```
回傳結果b會變成[1, 2, 1, 2, 3],並且回傳2

list小技巧：<br>
[::-1]可將list & str反轉, 反轉list之後為原始list副本, 反轉str之後覆蓋原始檔案<br>

### for迴圈語法

for用法一
```python
val = 3
nums = [3, 2, 2, 3]
for i in range((len(nums) - 1), -1, -1):  #此時i是序號，第一個-1代表結尾數字且不包含，最後一個-1代表每次增加-1
  if nums[i] == val:   #跑出結果為nums[3] [2] [1] [0] (3, 2, 2, 3)
    nums.remove(val)
print(len(nums))
```
回傳結果為 2

for用法二
```python
val = 3
nums = [3, 2, 2, 3]
for i in nums:  #此時的i是[3, 2, 2, 3]
  if i == val:
    nums.remove(val)
print(len(nums))
```
回傳結果為 2

### zip用法
```python
#zip會將對應元素打包成一個元組
a = [1, 2, 3]
b = [4, 5, 6]
x = list(zip(a,b)) #zip回傳的是一個對象所以要把它轉成list輸出
x
```
回傳結果為[(1, 4), (2, 5), (3, 6)]

```python
#解壓縮zip(*)
a1, b1 = zip(*)
print(list(a1))
print(list(b1))
```
回傳結果為  
[1, 2, 3]  
[4, 5, 6]  

### Numpy套件
陣列 VS 清單


| |Numpy|List|
|:---:|:---:|:---:|
|尺寸|更改物件尺寸就是`陣列`|無需指定大小|
|元素資料型態|必須相同|可以不同|
|效率|較高|較低|



-----
## Esclipse(Java)語法

-----
## R語言

-----
## C++環境視窗程式設計

-----
## GitHub使用方法
### 表格製作
|原始語法|顯示效果|
|:---:|:---:|
|":---:"|居中對齊|


-----
## LeeCode練習筆記

-----
## HomeWork

### 快速排序法

快速排序法使用分治法策略來把一個序列分為較小和較大的2個子序列，然後遞迴地排序兩個子序列。<br>
步驟為：<br>
1. 挑選基準值：從數列中挑出一個元素，稱為「基準」（pivot）<br>
2. 分割：重新排序數列，所有比基準值小的元素擺放在基準前面，所有比基準值大的元素擺在基準後面（與基準值相等的數可以到任何一邊）。在這個分割結束之後，對基準值的排序就已經完成<br>
3. 遞迴排序子序列：遞迴地將小於基準值元素的子序列和大於基準值元素的子序列排序。<br>
#### QuickSort

這種方式思路清晰簡單，銷量數據運行速度較快，缺點是會佔用到外部空間
```python
def quicksort(list):
    #長度不足2默認是已有順序的list
    if len(list) <= 1:
        return list
    else:
        #指定第一個數值為基準點
        pivot = list[0]
        #預留左側欄位
        left = []
        #預留右側欄位
        right = []
        #留出基準點的空間
        pivot_list = []
        
        #小於基準點的放在左側，大於基準點的放在右側，相同的就放在基準點
        for i in list:
            if i < pivot:
                left.append(i)
            elif i > pivot:
                right.append(i)
            else:
                pivot_list.append(i)
        
        #合併整合基左側、基準點、右側，並且重複呼叫quicksort循環進行
        return quicksort(left) + pivot_list + quicksort(right)
```

#### QuickSort_Inplace

這種方法不會用到外部空間，會在內部直接完成元素互換位置，大量數據運算的時候會比較實用
```python
def partition(array, begining, end):
    #如果資料長度不足2，認為已經是有序排列
    if len(array) <= 1:
        return array
    
    else:
        #宣告一個開頭節點，及其數值
        pivot_index = begining
        pivot = array[begining]
        
        #給出左右兩個指針
        left = pivot_index + 1
        right = end - 1
        
        #保證兩個迴圈的運行
        while True:
            
            #左側指針不斷進行到下一個直到第一個大於基準點的值
            while left <= right and array[left] < pivot:
                left += 1
            
            #右側指針不斷進行到上一個直到第一個小於基準點的值
            while right >= left and array[right] > pivot:
                right -= 1
            
            #運行到左側指針超過右側指針也就是說指針所在數值已經是left<right的時候打破迴圈
            if left > right:
                break
            
            #把左側指針指向的數值和右側指針指向的數值位置互換
            else:
                array[left], array[right] = array[right], array[left]
    
    #完成一次排序之後把基準點放置到指定位置
    array[pivot_index], array[right] = array[right], array[pivot_index]
    
    return right, pivot

def qs(array, begining, end):
    
    #只要沒有切分到開頭就是結尾（也就是說只有最後一個元素）就循環進行上述過程
    if begining < end:
        right, pivot = partition(array, begining, end)
        
        #運行左側部分
        qs(array, begining, right)
        
        #運行右側部分
        qs(array, right + 1,end)
    return array
list_example = [20, 3, 0, 35, 8, 23, 15, 28, 7, 32]
qs(list_example, 0, 10)
```

