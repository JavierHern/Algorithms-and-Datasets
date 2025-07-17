# TODO: Longest Palindromic Substring

# Difficulty: Medium

# Problem Statement:

# Given a string s, return the longest palindromic substring in s.

# A substring is a contiguous sequence of characters within a string. A palindrome is a string that reads the same forward and backward.

# Examples:

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"
    
# Example 3:
# Input: s = "a"
# Output: "a"

# Example 4:
# Input: s = "ac"
# Output: "a"
# Explanation: "a" and "c" are both valid answers.

# Constraints:

# 1 <= s.length <= 1000
# s consists of only lowercase English letters.

def expand_around_centers(s, left, right):
    """
    Expands from a central position until the characters remain the same.
    Returns the indexes of the beggining and end of the palindrome found.
    """
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    
    # Returns the palindrome indexes (excluding the breaking condition positions)
    return left + 1, right -1
    

def longest_palindrome(s):
    if not s:
        return ""
    
    # Initialize the indexes of the longest palindrome found
    start, end = 0, 0
    
    # Iterate each position in the array
    for i in range(len(s)):
        # Case 1: Expands from an odd center (a single character)
        left1, right1 = expand_around_centers(s, i, i)
        # Case 2: Expands from an even center (between two characters)
        left2, right2 = expand_around_centers(s, i, i + 1)
        
        # Update the longest palindrome (odd case)
        if right1 - left1 > end - start:
            start, end = left1, right1
        
        # Update the longest palindrome (even case)
        if right2 - left2 > end - start:
            start, end = left2, right2
    
    # Return the longest palindrome
    return s[start:end + 1]


def main():
    test_cases = ["babad", "cbbd", "a", "ac", "racecar", "bananas"]
    
    for s in test_cases:
        result = longest_palindrome(s)
        print(f"Input: '{s}', Longest palindrome: '{result}'")

if __name__ == "__main__":
    main()
    
# Complejidad Temporal: O(n²) donde n es la longitud de la cadena

# Para cada posición en la cadena (O(n)), expandimos hasta O(n) caracteres
# Complejidad Espacial: O(1) constante

# Solo almacenamos índices, sin crear estructuras adicionales que escalen con el tamaño de entrada
# Dos Punteros Expandiéndose: Has implementado correctamente la variante donde los punteros se alejan entre sí, en lugar de moverse hacia el centro como en el problema anterior.