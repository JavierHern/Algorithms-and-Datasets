# ## **Maximum Sum Subarray of Size K**

# **Enunciado:**  
# Dado un arreglo de números enteros `nums` y un entero positivo `k`, encuentra la suma máxima de cualquier subarreglo (subarray) de tamaño exactamente `k`.

# ---

# ### **Ejemplo 1**
# - **Input:** `nums = [2, 1, 5, 1, 3, 2]`, `k = 3`
# - **Output:** `9`
# - **Explicación:** El subarreglo con suma máxima de tamaño 3 es `[5, 1, 3]` (5 + 1 + 3 = 9)

# ### **Ejemplo 2**
# - **Input:** `nums = [1, 9, 8, 2, 6, 5, 3]`, `k = 4`
# - **Output:** `25`
# - **Explicación:** El subarreglo con suma máxima es `[9, 8, 2, 6]` (9 + 8 + 2 + 6 = 25)

# ---

# ### **Pista Sliding Window**
# - Usa una suma acumulada de la ventana de tamaño `k`
# - Cuando la ventana se “llena”, ve desplazando el inicio y el final, actualizando la suma eficientemente (restando el valor que sale, sumando el valor que entra)


def maximum_sum_subarray(nums, k):
    left = 0
    max_sum = 0
    sum = 0
    for right in range(len(nums)):
        sum += nums[right]
        if right - left + 1 == k:
            max_sum = max(max_sum, sum)
            sum -= nums[left]
            left += 1
    return max_sum


    
def main():
    arrs = [2,1,5,1,3,2], [1,9,8,2,6,5,3]
    ks = [3, 4]
    
    for i in range(len(arrs)):
        result = maximum_sum_subarray(arrs[i], ks[i])
        print(result)
        
    
if __name__ == "__main__":
    main()
