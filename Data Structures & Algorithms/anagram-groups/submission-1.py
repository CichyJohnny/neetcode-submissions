class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = dict()
        for n in strs:
            bag_of_words = self.bagify(n)
            if bag_of_words in results:
                results[bag_of_words].append(n)
            else:
                results[bag_of_words] = [n]

        return list(results.values())

    def bagify(self, s):
        bag = [0 for _ in range(26)]
        for n in s:
            bag[ord(n) - ord("a")] += 1

        return  tuple(bag)

