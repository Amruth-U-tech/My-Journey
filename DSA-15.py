class Solution(object):
    from collections import defaultdict
    def groupAnagrams(self, strs):
        hashmap = defaultdict(list) 
        #this tell that by default the values of each key is list

        for word in strs:
            encoder = [0]*26
            for letter in word:
                index = ord(letter)-ord('a')
                encoder[index]+=1
            key = tuple(encoder) #key must be immutable
            hashmap[key].append(word) #as default is list u can append directly
        return list(hashmap.values())              