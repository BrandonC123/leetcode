class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ans = []
        for left in range(len(nums)):
            cur_num = nums[left]
            if cur_num != 0:
                ans.append(cur_num)

        diff = len(nums) - len(ans)
        for i in range(diff):
            ans.append(0)
        
        for i in range(len(ans)):
            nums[i] = ans[i]
        