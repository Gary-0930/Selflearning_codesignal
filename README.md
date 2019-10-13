厲彥伯的GitHub
====
# 目錄
>* [Python語法](#Python語法)  
>   * [list語法](#list語法)
>   * [for迴圈語法](#for迴圈語法)
>   * [zip用法](#zip用法)
>   * [](#)
>* [Esclipse(Java)語法](#Esclipse(Java)語法)
>* [R語言](#R語言)
>* [C++環境視窗程式設計](#C++環境視窗程式設計)
>* [GitHub使用方法](#GitHub使用方法)
>* [LeeCode練習筆記](#LeeCode練習筆記)

---------------
## Python語法
### list語法 <br>

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
|:---:|:---|
|":---"|右側對齊|


-----
## LeeCode練習筆記

