#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
       
    
class MyHashSet:
    def __init__(self, capacity = 5):
        self.capacity = capacity
        self.data = [None] * capacity
        
    def add(self, key):
        key_MD5 = self.MyCrtoMD5(key)
        key_bucket = key_MD5 % (self.capacity)
        if self.data[key_bucket] is None:
            self.data[key_bucket] = ListNode(key_MD5)
        
        elif self.data[key_bucket].val != key_MD5:
           
            current = self.data[key_bucket]
            while current.next is not None:
                if current.next.val == key_MD5:
                    print("This key is duplicated.")
                else:
                    current = current.next
            current.next = ListNode(key_MD5)
            
        else:
            print("This key is duplicated.")   
            
    
    def remove(self, key):
        key_MD5 = self.MyCrtoMD5(key)
        key_bucket = key_MD5 % (self.capacity)
        current = self.data[key_bucket]
        pre = None
        while current is not None:
            if current.val == key_MD5:
                if pre is None:
                    self.data[key_bucket] = current.next
                    break
                else:
                    pre.next = current.next
                    del(current)
                    print(current)
            else:
                pre = current
                current = current.next
                    
            
        
    def contains(self, key):
        key_MD5 = self.MyCrtoMD5(key)
        key_bucket = key_MD5 % (self.capacity)
        current = self.data[key_bucket]
        while current is not None:
            if current.val == key_MD5:
                return True
            else:
                current = current.next
        return False
        
        
    def MyCrtoMD5(self, key):
        h = MD5.new()
        h.update(key.encode("utf-8"))
        h.hexdigest()
        int(h.hexdigest(), 16)
        return int(h.hexdigest(), 16)


# In[15]:


hashSet = MyHashSet()
hashSet.add("dog")
hashSet.add("pig")
rel = hashSet.contains("dog")
print(rel)
rel = hashSet.contains("pig")
print(rel)
rel = hashSet.contains("cat")
print(rel)
hashSet.add("bird")
rel = hashSet.contains("bird")
print(rel)
hashSet.remove("pig")
rel = hashSet.contains("pig")
print(rel)


# In[ ]:





# In[ ]:




