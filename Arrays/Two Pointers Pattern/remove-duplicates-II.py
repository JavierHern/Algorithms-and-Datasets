# Remove Duplicates from Sorted Array II

# Difficulty: Medium

# Problem Statement:

# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

# Examples:

# Example 1:
# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:
# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]
# Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Constraints:

# 1 <= nums.length <= 3 * 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in non-decreasing order.

def remove_duplicates_ii(nums):
    if not nums:
        return 0
    
    if len(nums) == 1:
        return 1

    slow, num_count = 1, 1
    
    for fast in range(1, len(nums)):
        # Si el elemento actual es igual al anterior
        if nums[fast] == nums[fast - 1]:
            num_count += 1
        else:
            num_count = 1
            
        if num_count <= 2:
            nums[slow] = nums[fast]
            slow += 1
            
    return slow


def main():
    arrs = [[1,1,1,2,2,3], [0,0,1,1,1,1,2,3,3], [3, 3, 8, 9, 9, 9, 10, 20, 21, 21]]
    expected_arrs = [[1,1,2,2,3], [0,0,1,1,2,3,3], [3,3,8,9,9,10,20,21,21]]
    
    for i in range(len(arrs)):
        nums = arrs[i]
        expected_nums = expected_arrs[i]
        
        k = remove_duplicates_ii(nums)
        print(k, nums)
        
        assert k == len(expected_nums)
        for i in range(k):
            assert nums[i] == expected_nums[i]
            
            
    print("todas la pruebas pasaron")
    
    
if __name__ == "__main__":
    main()
    

# Explicación del Enfoque

# La clave de este enfoque mejorado es:

# Contar ocurrencias del valor actual: Incrementamos el contador cuando vemos el mismo valor, reiniciamos cuando cambia.

# Tomar decisiones en cada elemento: Para cada elemento, decidimos si debe ser incluido (hasta 2 ocurrencias) o ignorado (3+ ocurrencias).

# Uso eficiente de punteros:

# slow: Indica dónde colocar el siguiente elemento válido
# fast: Recorre todos los elementos para procesarlos