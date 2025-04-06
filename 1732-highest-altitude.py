class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0]
        highest = altitudes[0]
        left = 0
        for right in range(len(gain)):
            cur_alt = gain[right] + altitudes[left]
            altitudes.append(cur_alt)
            if cur_alt > highest:
                highest = cur_alt
            left += 1
        return highest
        