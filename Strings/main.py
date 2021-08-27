class Solution:
    def groupAnagrams(self, strs):

       grouped = {}

       for word in strs:
           key = "".join(sorted(word))

           if key in grouped:
               grouped[key].append(word)
           else:
               grouped[key] = [word]

       return list(grouped.values())