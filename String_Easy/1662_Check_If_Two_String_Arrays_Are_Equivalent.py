 """
 ╔═════════════════════════════════════════════════════════════╗
 ║  LeetCode #1662                                             ║
 ║  Check If Two String Arrays are Equivalent                  ║
 ╠═════════════════════════════════════════════════════════════╣
 ║ Difficulty : Easy                                           ║
 ║ Topic      : Strings                                        ║
 ║ Language   : Python                                         ║
 ║ Date       : 21 July 2026                                   ║
 ╠═════════════════════════════════════════════════════════════╣
 ║ Approach:                                                   ║
 ║ • Concatenate both string arrays.                           ║
 ║ • Compare the resulting strings.                            ║
 ║                                                             ║
 ║ Time  : O(n + m)                                            ║
 ║ Space : O(n + m)                                            ║
 ╚═════════════════════════════════════════════════════════════╝
 """

class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        s1 = ""
        for k in word1:
            s1 += k

        s2 = ""
        for j in word2:
            s2 += j

        return s1 == s2
