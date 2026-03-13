class Solution(object):
    def findErrorNums(self, nums):
        dup=[]
        if nums[0]>nums[1]:
            order = nums[0]
            for i in nums:
                if i==order:
                    order-=1
                    continue
                dup.append(i)
                dup.append(order)
                return dup
        else:
            order = 1
            for i in nums:
                if i==order:
                    order+=1
                    continue
                dup.append(i)
                dup.append(order)
                return dup
sol = Solution()
nums = [3,2,2]
print(sol.findErrorNums(nums))          