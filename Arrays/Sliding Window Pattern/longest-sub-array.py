# ## **Longest Substring Without Repeating Characters**

# Dado un string `s`, encuentra la longitud de la subcadena más larga que no contiene caracteres repetidos.

# ### **Ejemplos:**
# - **Input:** `"abcabcbb"`  
#   **Output:** `3`  
#   **Explicación:** La respuesta es `"abc"`, con longitud 3.

# - **Input:** `"bbbbb"`  
#   **Output:** `1`  
#   **Explicación:** La respuesta es `"b"`, con longitud 1.

# - **Input:** `"pwwkew"`  
#   **Output:** `3`  
#   **Explicación:** La respuesta es `"wke"`, con longitud 3. `"pwke"` también es válido.

# ---

# **Pista:** Usa dos punteros para mantener una ventana válida y una estructura para saber si un carácter ya está en la ventana.

def longest_sub_array(s):
    char_set = set()
    left = 0
    max_length = 0
    window = ''

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        if right - left + 1 > max_length:
            max_length = right - left + 1
            window = s[left:right + 1] 
    return max_length, window



def main():
    strings = [
        "abcabcbb",
        "bbbbb",
        "pwwkew"
    ]
    
    for s in strings:
        n, w = longest_sub_array(s)
        print(f"The longest substring in '{s}': {n} ('{w}')")
    
if __name__ == "__main__":
    main()

