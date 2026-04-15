class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in hashmap:
                return [hashmap[complement], i]

            hashmap[num] = i


    def singleNumber(self, nums):
        hashmap = {}
        for i in nums:
            hashmap[i]=hashmap.get(i,0)+1
        for key,value in hashmap.items():
            if value==1:
                return key
        return -1