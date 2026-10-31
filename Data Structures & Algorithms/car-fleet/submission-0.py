class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positions_and_arrivals = []
        for p, s in zip(position, speed):
            positions_and_arrivals.append((p, (target - p) / s))
        positions_and_arrivals.sort()
        arrivals = [n[1] for n in positions_and_arrivals]

        for i in reversed(range(len(arrivals))):
            if i + 1 < len(arrivals) and arrivals[i] < arrivals[i + 1]:
                arrivals[i] = arrivals[i + 1]
        
        return len(set(arrivals))

# target=10, position=[4,1,0,7], speed=[2,2,5,1]
# planned_arrivals=[(0,2),(1,4.5),(4,3),(7,3)]
# planned_arrivals=[(0,2),(1,3),(4,3),(7,3)]
# len({2,3}) = 2
