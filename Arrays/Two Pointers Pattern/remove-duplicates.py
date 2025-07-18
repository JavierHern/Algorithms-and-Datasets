# Remove Duplicates from Sorted Array

# Difficulty: Easy

# Problem Statement:

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.

# Examples:

# Example 1:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Constraints:

# 1 <= nums.length <= 3 * 10^4
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order.

def remove_duplicates(nums):
    if not nums:
        return 0
    
    #Posición en donde colocar el siguiente elemento único
    slow = 0
    
    #Explorar el array en busca de elementos únicos
    for fast in range(1, len(nums)):
        # Si encontramos un elemento diferente
        if nums[slow] != nums[fast]:
            # Avanzar el puentero lento y colocar el nuevo elemento único
            slow += 1
            nums[slow] = nums[fast]
    
    # retornar la cantidad de elementos únicos
    return slow + 1
    

def main():
    arrs = [[0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [1, 1, 2], [3, 3, 8, 9, 9, 9, 10, 20, 21, 21]]
    expected_arrs = [[0,1,2,3,4], [1, 2], [3, 8, 9, 10, 20, 21]]
    
    for i in range(len(arrs)):
        nums = arrs[i]
        expected_nums = expected_arrs[i]
        
        k = remove_duplicates(nums)
        print(k, nums)
        
        assert k == len(expected_nums)
        for i in range(k):
            assert nums[i] == expected_nums[i]
    
    
if __name__ == "__main__":
    main()
    
    
# Ventajas de esta implementación:

# Tiempo: O(n) en lugar de O(n²)
# Espacio: O(1), igual que tu solución
# Simplicidad: Menos código, más legible
# Cumple con los requisitos: Modifica el array in-place y retorna k


# El Patrón "Two Pointers" para Modificación In-Place

# Esta variante del patrón "Two Pointers" es particularmente útil para:

# Modificar arrays in-place sin necesitar espacio adicional
# Mantener un subconjunto de elementos que cumplen cierta condición
# Filtrar elementos mientras se preserva el orden relativo
