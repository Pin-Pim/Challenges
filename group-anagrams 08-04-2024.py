
def groupAnagrams(strs):
  hashmap = {}
  groups = []
  index = 0
  for i in range(len(strs)):
    if sorted(strs[i]) in hashmap:
      groups[hashmap[sorted(strs[i])]].append(strs[i])
    elif sorted(strs[i]) not in hashmap:
      index += 1
      hashmap[sorted(strs[i])] = index
      groups.append([strs[i]])
  return groups
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

