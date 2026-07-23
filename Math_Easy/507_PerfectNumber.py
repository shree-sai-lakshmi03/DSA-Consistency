class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return False

        s = 1

        for k in range(2, int(num**0.5) + 1):
            if num % k == 0:
                s += k
                if k != num // k:
                    s += num // k

        return s == num

  """A perfect number is a number equal to the sum of its proper divisors (excluding itself).
We start with s = 1 because 1 is a proper divisor of every number greater than 1.

Instead of checking every number up to num, we only check up to √num.
Whenever k is a divisor of num, its paired divisor num // k is also a divisor.

Example: For 28, if 2 is a divisor, then 14 is also a divisor.
We add both divisors to the sum.
If k == num // k (which happens for perfect squares),
we add it only once to avoid double-counting.
Finally, if the sum of all proper divisors equals num, we return True; otherwise, False.

Time Complexity
O(√n), because we only iterate up to the square root of the number.

Space Complexity
O(1), since only a few variables are used."""
