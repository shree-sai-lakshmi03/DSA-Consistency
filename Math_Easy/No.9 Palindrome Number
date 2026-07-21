"""
╔════════════════════════════════════════════════════════════╗
║  LeetCode #9                                               ║
║  Palindrome Number                                         ║
╠══════════════════════════════════════════════════=═════════╣
║ Difficulty : Easy                                          ║
║ Topic      : Math, String                                  ║
║ Language   : Python                                        ║
║ Date       : 21 July 2026                                  ║
╠════════════════════════════════════════════════════════════╣
║ Approach:                                                  ║
║ • Negative numbers cannot be palindromes.                  ║
║ • Convert the integer to a string.                         ║
║ • Compare the string with its reverse using slicing.       ║
║                                                            ║
║ Time  : O(n)                                               ║
║ Space : O(n)                                               ║
╚════════════════════════════════════════════════════════════╝"""
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False

        x = str(x)

        return x == x[::-1]

"""
Notes:
- Used Python string slicing ([::-1]) to reverse the string.
- Negative numbers are never palindromes because of the '-' sign.
- This is an easy and readable solution, though it uses extra space.
"""

        return x == x[::-1]
