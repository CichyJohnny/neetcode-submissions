class Solution:
    def trap(self, height: List[int]) -> int:
        topl = [0]
        topr = [0]

        for i in range(1, len(height)):
            topl.append(max(topl[-1], height[i - 1]))

        for i in reversed(range(len(height) - 1)):
            topr.append(max(topr[-1], height[i + 1]))
        topr = list(reversed(topr))

        result = 0
        for i in range(len(height)):
            result += max(min(topl[i], topr[i]) - height[i], 0)
        return result
