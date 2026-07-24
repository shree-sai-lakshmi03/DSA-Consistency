class Solution(object):
    def secondHighest(self, s):
        l = []

        for k in s:
            if k.isdigit():
                l.append(int(k))

        l = list(set(l))
        l.sort()

        if len(l) < 2:
            return -1

        return l[-2]

  """Traversing a string
isdigit()
Converting characters to integers
set() to remove duplicates
Sorting
Edge-case handling (len(l) < 2)"""
