nums,k = [1,1,1,2,2,3,3,3,4,4,4,4],2
hashmap = {}

for num in nums:
    hashmap[num] = hashmap.get(num, 0) + 1
print(hashmap)
print("\n")

# sort by frequency
sorted_items = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
print(key=lambda x:x[1])
print(sorted_items