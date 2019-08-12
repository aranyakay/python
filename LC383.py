

class Solution:
    def canConstruct(self, ransomNote, magazine) :
        freq_dict = {}
        for i in magazine:
            if i in freq_dict:
                freq_dict[i] = freq_dict[i] + 1
            else:
                freq_dict[i] = 1
        for j in ransomNote:
            if j in freq_dict:
                if freq_dict[j] == 0:
                    return(False)
                freq_dict[j] = freq_dict[j] - 1
            else:
                return(False)
        return(True)
