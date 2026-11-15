class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        estimated = []
        for p, s in sorted(zip(position, speed)):
            estimated.append((target - p) / s)
        
        for i in reversed(range(len(estimated) - 1)):
            if estimated[i + 1] > estimated[i]:
                estimated[i] = estimated[i + 1]
        
        return len(set(estimated))

# target=10
# position=[4,1,0,7]
# speed=[2,2,1,1]
# estimated = [(10-4)/2, (10-1)/2, (10-0)/1, (10-7)/1]
# estimated = [3, 4.5, 10, 3]
