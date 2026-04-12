class Solution(object):
    def moveZeroes(self, nums):
        index1 = 0

        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[index1]=nums[index1],nums[i]
                index1+=1
        return nums
    
    def minCostToMoveChips(self, position):
        hashmap = {}
        for i in position:
            if i in hashmap:
                continue
            cost = 0
            for j in position:
                diff = abs(j-i)
                if diff%2!=0:
                    cost+=1
            hashmap[i]=cost
        return min(hashmap.values())
    
    def minCostToMoveChips(self, position):
        hashmap = {"even":0,"odd":0}

        for i in position:
            if i%2==0:
                hashmap["even"]+=1
            else:
                hashmap["odd"]+=1
        return min(hashmap.values())    
