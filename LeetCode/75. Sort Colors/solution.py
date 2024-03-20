class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = mid = 0
        right = len(nums) - 1

        # 앞에서부터 2를 뒤로 넘기면서 오는 것이기 때문에
        # num[mid] = 0 이라면 num[left] = 0 or 1 이 자명하다.
        # 반면에 뒤에 num[mid] = 2 같은 경우에는 num[right]가 0, 1, 2 셋 다 가능하므로
        # mid += 1을 하지 않는다.
        while mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1
