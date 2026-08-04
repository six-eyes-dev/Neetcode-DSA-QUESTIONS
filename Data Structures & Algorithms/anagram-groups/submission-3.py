class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Little optimized
        # IDEA:
        #  - Need to group all anagrams.
        #  - so we require something 'central' so that all similar anagrams can be compared to that form
        #  - What if we sort them before comparing? and putting accordingly in suitable bucket.
        #  - Every time sort, a 'central' anagram is created, i.e. common form to all Anagrams.

        ans = {}

        for string in strs:
            key = "".join(sorted(string))
            ans[key] = ans.get(key, [])
            ans[key].append(string)
        
        return list(ans.values())