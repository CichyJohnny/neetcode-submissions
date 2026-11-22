class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = {}
        for t in tasks:
            counter[t] = counter.get(t, 0) + 1
        
        max_freq = max(counter.values())

        num_max_freq = 0
        for v in counter.values(): 
            if v == max_freq: 
                num_max_freq += 1
        
        chunks = max_freq - 1
        chunk_length = n + 1

        base_length = (chunks * chunk_length) + num_max_freq

        return max(len(tasks), base_length)
    
# ["A","A","A","B","B","B","C","C","C","D","D","E"], n=2
# counter = {A: 3, B:3, C: 3, D:2, E:1}
# max_freq = 3
# num_max_freq = 3
# chunks = 2, chunk_length = 3
# base_length = 2 * 3 + 3 = 9
# return max(12, 9)
