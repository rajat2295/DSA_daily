import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        test = s.lower()
        pattern = re.compile('[\W_]+')
        test = (pattern.sub('', test) )
        l=0 
        r = len(test)-1
        while l<=r:
            if(test[l]!=test[r]):
                return False
            l+=1
            r-=1
        return True
