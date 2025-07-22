# ## **Longest Subarray with Sum ≤ S**

# **Enunciado:**  
# Dado un arreglo de enteros `nums` y un entero positivo `S`, encuentra la longitud máxima de un subarreglo (subarray) cuya suma sea menor o igual que `S`.

# ---

# ### **Ejemplo 1**
# - **Input:** `nums = [2, 1, 5, 1, 3, 2]`, `S = 7`
# - **Output:** `4`
# - **Explicación:** El subarreglo más largo con suma ≤ 7 es `[2, 1, 5, 1]` (suma 2+1+5+1=9, no válido), pero `[1, 5, 1]` (suma 1+5+1=7) es válido y de longitud 3. Pero si tomas `[2, 1, 5]` (suma 8, no válido). El más largo válido es `[1, 5, 1]` (longitud 3).

# - **Corrección:** En este caso, los subarreglos válidos son `[2,1,5]` (suma 8, no válido), `[1,5,1]` (7, válido), `[5,1,3]` (9, no válido), `[1,3,2]` (6, válido, longitud 3). El más largo válido es `[1,3,2]` de longitud 3.

# ### **Ejemplo 2**
# - **Input:** `nums = [1, 2, 3, 4, 5]`, `S = 11`
# - **Output:** `3`
# - **Explicación:** La subcadena más larga con suma ≤ 11 es `[2, 3, 4]` (suma 9, longitud 3).

# ---

# ### **Pista Sliding Window**
# - Mantén la suma actual de la ventana.
# - Si la suma excede `S`, mueve el inicio de la ventana (`left`) hacia adelante y resta los valores que salen.
# - Actualiza la longitud máxima cada vez que la suma sea válida.

def longest_subarr_sum(nums, s):
    left = 0
    current_sum = 0
    max_length = 0

    for right in range(len(nums)):
        current_sum += nums[right]
        while current_sum > s and left <= right:
            current_sum -= nums[left]
            left += 1
        if current_sum <= s:
            max_length = max(max_length, right - left + 1)

    return max_length

def main():
    nums = [[2,1,5,1,3,2], [1,2,3,4,5]]
    s = [7, 11]

    for i in range(len(nums)):
        result = longest_subarr_sum(nums[i], s[i])
        print(result)
        
    
if __name__ == "__main__":
    main()