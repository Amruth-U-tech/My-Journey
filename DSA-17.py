class Solution(object):
    def majorityElement(self, nums):
        hashmap = {}
    
        for i in nums:
            hashmap[i] = hashmap.get(i,0)+1

        for i in hashmap.keys():
            if hashmap[i]>len(nums)//2:
                return i
        return -1   
#more proffesional code for same above problem
    def majorityElement(self, nums):
        hashmap = {}
    
        for i in nums:
            hashmap[i] = hashmap.get(i,0)+1

        for keys,count in hashmap.items():
            if count>len(nums)//2:
                return i
        return -1           
