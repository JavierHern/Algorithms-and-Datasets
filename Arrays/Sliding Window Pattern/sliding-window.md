## Sliding Window

---

### **¿Qué es el patrón Sliding Window?**
El patrón **Sliding Window** (“ventana deslizante”) es muy útil para trabajar con subarrays o subcadenas de longitud fija o variable, especialmente para calcular sumas, máximos, mínimos, o contar elementos bajo ciertas condiciones.

En vez de recorrer todas las combinaciones posibles (lo cual suele ser costoso), este patrón mantiene una “ventana” que se mueve por el array, actualizando eficientemente el resultado.

---

### **Ejemplo clásico: Longest Substring Without Repeating Characters**

**Problema:**  
Dado un string, encuentra la longitud de la subcadena más larga que no contiene caracteres repetidos.

**Ejemplo:**  
- Entrada: `"abcabcbb"`
- Salida: `3` (`"abc"` es la subcadena más larga sin caracteres repetidos)

---

### **¿Cómo funciona el Sliding Window aquí?**

1. Usamos dos punteros (`left`, `right`) para marcar el inicio y el final de la ventana.
2. Avanzamos el puntero `right`, añadiendo caracteres a un conjunto o diccionario.
3. Si aparece un carácter repetido, avanzamos el puntero `left` hasta que no haya repetidos.
4. En cada paso, actualizamos la longitud máxima de la ventana.

---

### **Código base en Python**

```python
def length_of_longest_substring(s):
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length
```

---

¿Te gustaría intentar este problema tú mismo?  
¿O prefieres que te presente otro problema clásico usando Sliding Window?