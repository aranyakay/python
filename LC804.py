class Solution:
    def uniqueMorseRepresentations(self, words):
        mosi = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..",
            "--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        out = []
        for x in words:
            X = list(x)
            for n,i in enumerate(X):
                X[n] = mosi[ord(i)-97]
            out.append("".join(X))
        return len(set(out))
