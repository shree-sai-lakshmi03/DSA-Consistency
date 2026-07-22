class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        c=0
        for k in details:
            if int(k[11:13])>60:
                c+=1
            else:
                c+=0
        return c
