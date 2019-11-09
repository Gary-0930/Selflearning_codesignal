#!/usr/bin/env python
# coding: utf-8

# In[5]:


class Solution(object):
    def mergesort(self, arr):  
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]
            Solution().mergesort(left)  ##重複分解左右兩側
            Solution().mergesort(right)
        
            index = 0
            i = 0
            j = 0
            while i < len(left) and j < len(right):  ##兩側都還沒有合併完
                if left[i] < right[j]:  ##把最小的值改為arr的第0個值
                    arr[index] = left[i]
                    i += 1
                else:
                    arr[index] = right[j]
                    j += 1
                index += 1
            while i < len(left):  ##當一方完全合併完畢的時候直接把剩餘的按順序加入到裡面
                arr[index] = left[i]
                i += 1
                index += 1
            while j < len(right):
                arr[index] = right[j]
                j += 1
                index += 1
                
        return arr


# In[ ]:




