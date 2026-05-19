class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter

        cnt_dict = Counter(s)
        for l in t:
            if l in cnt_dict and cnt_dict[l]>0:
                cnt_dict[l] -= 1
            elif l in cnt_dict and cnt_dict[l] == 0:
                del cnt_dict[l]
            else:
                return False
            
        return all(c == 0 for c in cnt_dict.values())