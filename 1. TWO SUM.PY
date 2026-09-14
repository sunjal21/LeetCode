# # You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?


class Solution(object):
    def twoSum(self, nums, target):
        left, right=0,len(nums)-1
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == target:
                return[left,right]
            elif current_sum < target:
                left+=1

# *This code requires the array to be sorted. so the solution does not satisfy all test cases *#

# Advantages:

# Very fast: O(n)
# Uses very little extra memory: O(1)
# Excellent for large sorted arrays.

# Disadvantages:

# Requires the array to be sorted.
# If the array is unsorted, the left/right movement logic doesn't work. #