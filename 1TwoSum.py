class Solution:
    def twoSum(self, nums, target):
        num_map = {}  # Dictionary to store numbers and their indices
        for i in range(len(nums)):
            complement = target - nums[i]  # The number we need
            if complement in num_map:  # Check if we have seen it before
                return [num_map[complement], i]  # Return their indices
            num_map[nums[i]] = i  # Store the current number and its index
