class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Optimal

        # Idea: 
        # This time instead of sorting, we'll create another "common form", previously this "common form" was being created by sorting.
        ans = {}

        def common_form(string):
            count = [0]*26
            for char in string:
                count[ord(char)- ord('a')] += 1
            
            # now we need to create 'key' so that independent of different anagrams
            key = []
            for i in range(26):
                if count[i] > 0:
                    char = chr(i + ord('a'))
                    key.append( char + str(count[i]) )
            return "".join(key)
        
        for string in strs:
            key = common_form(string)
            ans[key] = ans.get(key, [])
            ans[key].append(string)

        return list(ans.values())



