class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = {}
        # Brute Force : O(N*N*K) where K = length of string
        def is_anagram(str1:str, str2:str):

            if len(str1) != len(str2):
                return False
            
            elements = {}
            for char in str1:
                elements[char] = elements.get(char,0) + 1

            for char in str2:
                elements[char] = elements.get(char,0) - 1

            for value in elements.values():
                if value != 0:
                    return False
            
            return True
        
        size = len(strs)
        for i in range(size):

            if strs[i] == None:
                continue
            temp = [strs[i]]
            for j in range(i+1, size):
                if strs[j] == None:
                    continue
                if is_anagram(strs[i], strs[j]):
                    temp.append(strs[j])
                    strs[j] = None
                
            ans.update({i: temp})
        
        return list(ans.values())

