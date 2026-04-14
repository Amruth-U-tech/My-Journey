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

#solved the anagram problem easy version

    def isAnagram(self, s, t):
        list1 = [[0]*26,[0]*26]

        for letter in s:
            index1 = ord(letter)-ord('a')
            list1[0][index1]+=1
        for letter in t:
            index1 = ord(letter)-ord('a')
            list1[1][index1]+=1
        return list1[0]==list1[1]
#solved the above problem by removing the redundant time complexity
    def isAnagram(self, s, t):
        count_s = [0]*26
        count_t = [0]*26

        for c in s:
            count_s[ord(c)-ord('a')] += 1

        for c in t:
            count_t[ord(c)-ord('a')] += 1

        return count_s == count_t