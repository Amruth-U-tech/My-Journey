class Solution(object):
    def findErrorNums(self, nums):
        seen = set()
        dup = -1
        
        for num in nums:
            if num in seen:
                dup = num
            seen.add(num)

        for i in range(1, len(nums) + 1):
            if i not in seen:
                return [dup, i]
    def smallerNumbersThanCurrent(self, nums):
        greater = []
        for i in nums:
            counter = 0
            for j in nums:
                if j<i:
                    counter+=1
            greater.append(counter)
        return greater
         