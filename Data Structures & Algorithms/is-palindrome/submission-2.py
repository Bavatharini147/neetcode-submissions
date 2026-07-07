
class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=""
        t=""
        for i in s:
            if i.isalnum():
                t+=i.lower()
        
        for i in range(len(t)-1,-1,-1):
            a+=t[i]
        if(a==t):
            return True
        else:
            return False
