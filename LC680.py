#lc 680
#this solution is
#out of github time limit

def validPalindrome(s):
    def checkPalindrome(S):
        if len(S) % 2 ==0:
            cut = int(len(S)/2)
            start = S[0:cut]
            end = S[cut:len(S)]
            end = end[::-1]
        else:
            cut = int((len(S)-1)/2)
            start = S[0:cut]
            end = S[cut+1:len(S)]
            end = end[::-1]
        return(start==end)
    result = False
    if checkPalindrome(s):
        result = True
    for i in range(len(s)):
        S = s[0:i] + s[i+1:]
        if checkPalindrome(S):
            result = True
    return(result)


#modify and improve 
#and this one also out of time limit
def validPalindrome(s):
    result = False
    if s == s[::-1]:
        result = True
    for i in range(len(s)):
        S = s[0:i] + s[i+1:]
        if S == S[::-1]:
            result = True
    return(result)


#modify more
#loop might cost too much
#shrink loop, double check methods from start and end
class Solution:
    def validPalindrome(self, s):
        result = False
        if s == s[::-1]:
            return(True)
        for i in range(len(s)):
            if i == 0:
                S = s[1:]
                if S == S[::-1]:
                    return(True)
            if i == len(s):
                S = s[:i-1]
                if S == S[::-1]:
                    return(True)
            cut = min(i+1, int(len(S)/2))
            start = s[0:cut]
            end = s[len(s)-cut:]
            if start == end[::-1] and i != len(s)/2 +0.5:
                mid = s[cut+1:len(s)-cut-1]
                if mid == mid[::-1]:
                    result = True
        return(result)


#something so fast

class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n=len(s)
        left=0
        right=n-1
        while left<right:
            if s[left]!=s[right]:
                return self.comp(s,left+1,right) or self.comp(s,left,right-1)
            left+=1
            right-=1
        return True
        
        
    def comp(self,s,left,right):
        while left<right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1

            
