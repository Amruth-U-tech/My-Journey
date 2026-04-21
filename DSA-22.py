class Solution(object):
    def topKFrequent(self, nums, k):
        hashmap = {}
        list2 = []
        for num in nums:
            hashmap[num] = hashmap.get(num,0)+1
        list1 = hashmap.values()
        for i in range(k):
            list2.append(max(list1))
            list1.remove(list2[i])
        for key,value in hashmap.items():
            if value in list2[0:k]:
                list2.append(key)
        return list2[k:]
    
#while solving the above problem there is no issue in calculating the frequency by hashmap but getting top k frequent elements from hashmap 
#directly becomes bit messy