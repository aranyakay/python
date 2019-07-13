def numJewelsInStones(self, J, S):
    s = list(S)
    total = 0
    for i in s:
        if i in J:
            total += 1
    return total;
    
J = "aAc"
S = "aAAbbbp"
jewStone(J, S)
