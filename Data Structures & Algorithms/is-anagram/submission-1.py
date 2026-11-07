class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_bag_of_words = {}
        t_bag_of_words = {}

        for n in s:
            s_bag_of_words[n] = s_bag_of_words.get(n, 0) + 1
        for n in t:
            t_bag_of_words[n] = t_bag_of_words.get(n, 0) + 1

        return s_bag_of_words == t_bag_of_words

