class Solution(object):
    def pivotIndex(self, nums):
        l_p = 0
        r_p = len(nums)-1
        left_sum = nums[l_p]
        right_sum = nums[r_p]
        for i in range(len(nums)):
            if l_p==r_p and left_sum==right_sum:
                return l_p
            elif left_sum<right_sum:
                l_p+=1
                left_sum+=nums[l_p]
            elif right_sum<left_sum:
                r_p-=1
                right_sum+=nums[r_p]
            elif l_p+2==r_p and left_sum==right_sum:
                return l_p+1
            else:
                continue
        return -1
            