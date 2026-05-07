class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        l_dict = dict(zip(letters, range(26)))
        def get_key(word):
            l_d = [0]*26
            for w in word:
                if w in l_dict:
                    l_d[l_dict[w]] += 1
            return tuple(l_d)

        ana_dict = defaultdict(list)
        for word in strs:
            word_key = get_key(word)
            ana_dict[word_key].append(word)
        
        return list(ana_dict.values())