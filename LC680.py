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



