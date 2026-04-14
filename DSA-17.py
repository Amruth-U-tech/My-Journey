class Solution(object):
    def majorityElement(self, nums):
        hashmap = {}
    
        for i in nums:
            hashmap[i] = hashmap.get(i,0)+1

        for i in hashmap.keys():
            if hashmap[i]>len(nums)//2:
                return i
        return -1   