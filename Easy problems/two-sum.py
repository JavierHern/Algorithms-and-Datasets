#### TODO: Two Sum
# Difficulty: Easy

# Problem Statement:

# Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to the target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Examples:

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] = 2 + 7 = 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Explanation: Because nums[1] + nums[2] = 2 + 4 = 6, we return [1, 2].

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

# Constraints:

# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.

###


def two_sum(nums, target):
    p1 = 0
    p2 = len(nums) - 1
    
    while p1 < p2:
        actual_sum = nums[p1] + nums[p2]
    
        if actual_sum == target:
            return [p1, p2]
        if target > actual_sum:
            p1 += 1
        if target < actual_sum:
            p2 -= 1


def main():
    nums = [1, 2, 3, 4, 5]
    target = 9
    result = two_sum(nums, target)
    print("resultado (indices): " + str(result))

main()