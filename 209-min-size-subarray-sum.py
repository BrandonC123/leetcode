class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        min_length = float('inf')

        cur_sum = 0

        for right in range(len(nums)):
            if nums[right] == target:
                return 1
            cur_sum += nums[right]
            # Shrink to smallest window
            while cur_sum >= target:
                cur_length = right - left
                cur_sum -= nums[left]
                left += 1
                min_length = min(min_length, cur_length)
        return min_length if min_length != float('inf') else 0
        