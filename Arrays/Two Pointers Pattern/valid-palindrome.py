# TODO: Valid Palindrome

# Difficulty: Easy

# Problem Statement:

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Examples:

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

# Constraints:
# 1 <= s.length <= 2 * 10^5
# s consists only of printable ASCII characters.

def valid_palindrome(string):
    # Clear the string of non-alfanumeric characters
    clean_string = ''.join(char for char in string if char.isalnum()).lower()
    
    # Declare the pointers at the beginning and at the end
    p1 = 0
    p2 = len(clean_string) - 1
    
    # Pass the array only once until the condition is met, or the Fase is return
    while p1 < p2:
        if clean_string[p1] != clean_string[p2]:
            return False
        p1 += 1
        p2 -= 1
    
    return True



def main():
    s = "A man, a plan, a canal: Panama"
    result = valid_palindrome(s)
    print("resultado : " + str(result))
    
    s = "race a car"
    result = valid_palindrome(s)
    print("resultado : " + str(result))
    
    s = " "
    result = valid_palindrome(s)
    print("resultado : " + str(result))

    s = "Anita lava la tina"
    result = valid_palindrome(s)
    print("resultado : " + str(result))

main()

# Complejidad:

# Tiempo: O(n) donde n es la longitud de la cadena
# Espacio: O(n) para almacenar la cadena limpia