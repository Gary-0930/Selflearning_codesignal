#!/usr/bin/env python
# coding: utf-8

# In[15]:


class Solution(object):
    
    def heap_sort(self, arr):
        
        length = len(arr)
        Solution().heapbuild(arr)  #建立最大堆
    
        while length > 1:  #while迴圈執行的次數取決於len，每次執行的次數都會是len - 1次
            arr[0], arr[length - 1] = arr[length - 1], arr[0]  #把確定好的最大值放到最後的位置，不再進行更改
            length -= 1
            Solution().maxheapify(arr, length, 0)  #每執行一次都會進行一次最大堆排序
        return arr  #最終計算後把更改後的arr回傳
    
    def heapbuild(self, arr):  #建立最大堆
        length = len(arr)
        notleaf_index = int(length / 2 - 1)     #非葉子節點的位置是需要判斷的最後一個位置，其餘都沒有子節點則無需判斷        
        while notleaf_index >= 0:                 
            Solution().maxheapify(arr, length, notleaf_index)
            notleaf_index -= 1
        
    def maxheapify(self,arr,length,current):  #最大堆排序
        left_index = 2 * current + 1  #left代表左下方的位置
        right_index = 2 * current + 2  #right代表右下方的位置
        largest_index = current  #宣告一個largest用來找出三角形內哪一個是最大值
        if left_index < length and arr[largest_index] < arr[left_index]:  
            largest_index = left_index
        if right_index < length and arr[largest_index] < arr[right_index]:
            largest_index = right_index
        if largest_index != current:  #如果發現largest並不是父節點意味著需要進行更換
            arr[largest_index], arr[current] = arr[current], arr[largest_index]
            Solution().maxheapify(arr, length, largest_index)  #遞歸操作


# In[ ]:




