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

class Solution(object):
    def topKFrequent(self, nums, k):
        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        # sort by frequency
        sorted_items = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)

        result = []
        for i in range(k):
            result.append(sorted_items[i][0])

        return result
# this is much better code clean and logical
'''but this line was new to me and a unique concept in python
    here lambda is anonymum function gerator and key is a anonymus function which takes x as an argument and return x[1]
    
    here x argument recives the tuple item i.e x=(key,value) fromt he hashmap and hence return x[1] that is values 
        based on which the sorting is done
        
        ⚔️ Mental Model

        Think:

        for x in hashmap.items():
            use x[1] to compare
            
            '''
#there is much better way to solve this top k elemnt problem using heap tree i.e heapq (lib from pyhton) or bucket sort