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
    #Map to store numbers we've seen and their indices
    seen = {}
    
    # Iterate and enumerate all the numbs array
    for i, num in enumerate(nums):
        # Define the complement
        complement = target - num
        
        # if the complement is in seen, then the pairs are already found
        if complement in seen:
            return [seen[complement], i]
        
        #set the number with it's index
        seen[num] = i
        
    # return none if the complements were not found
    return None


def main():
    nums = [1, 2, 3, 4, 5]
    target = 9
    result = two_sum(nums, target)
    print("resultado (indices): " + str(result))

    nums = [1, 10, 2, 8, 5]
    target = 9
    result = two_sum(nums, target)
    print("resultado (indices): " + str(result))

    nums = [30, 5, 3, 4, 10]
    target = 40
    result = two_sum(nums, target)
    print("resultado (indices): " + str(result))


main()