# 20. Valid Parentheses
# 
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.
# 
# An input string is valid if:
#   
#   Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
# 
# Example 1:
#   
#   Input: "()"
# Output: true
# Example 2:
#   
#   Input: "()[]{}"
# Output: true
# Example 3:
#   
#   Input: "(]"
# Output: false
# Example 4:
#   
#   Input: "([)]"
# Output: false
# Example 5:
#   
#   Input: "{[]}"
# Output: true

def LC20(X):
    start = ["(", "[", "{"]
    end = [")", "]", "}"]
    jug = []
    x = list(X)
    for i in x:
        if i in start:
            jug.append(i)
        if i in end:
            if len(jug)>0 and start[end.index(i)] == jug[-1]:
                del jug[-1]
            else:
                jug.append(i)
    return(len(jug) == 0)

LC20("{}][")

LC20("{{[]}}()()(())()(){()()(){([()][()]()){[[()]]}{()}}}(())")   
    
