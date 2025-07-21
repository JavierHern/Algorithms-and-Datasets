# Container With Most Water

# Difficulty: Medium

# Problem Statement:

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# Examples:

# Example 1: Container With Most Water Example
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
# In this case, the max area of water (blue section) the container can contain is 49.
# The container is formed between heights at indices 1 and 8 (values 8 and 7),
# with a width of 7 and minimum height of 7, giving area = 7 * 7 = 49.

# Example 2:
# Input: height = [1,1]
# Output: 1

# Example 3:
# Input: height = [4,3,2,1,4]
# Output: 16
# Explanation: The container is formed between the first and last heights (both 4),
# with a width of 4, giving area = 4 * 4 = 16.

# Example 4:
# Input: height = [1,2,1]
# Output: 2

# Constraints:
# n == height.length
# 2 <= n <= 10^5
# 0 <= height[i] <= 10^4

def container_most_water(height):
    h1, h2 = 0, len(height) - 1
    max_area = 0
    
    while h1 < h2:
        vertical =  min(height[h1], height[h2])
        area = vertical * (h2 - h1)
        if area > max_area:
            max_area = area

        if height[h1] < height[h2]:
            h1 += 1
        else:
            h2 -= 1
    return max_area


def main():
    arrs = [
        [1,1], 
        [1,8,6,2,5,4,8,3,7], 
        [4,3,2,1,4]
    ]
    
    for arr in arrs:
        k = container_most_water(arr)
        print("The maximum water contained: ", k)
    
if __name__ == "__main__":
    main()


# Complejidad

# Tiempo: O(n)
# Espacio: O(1)