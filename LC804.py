#slow and brute force one
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

    
    #a faster solution
    class Solution:
    def uniqueMorseRepresentations(self, words):
        mosi = [".-","-...","-.-.","-..",".","..-.",
                "--.","....","..",".---","-.-",".-..",
                "--","-.","---",".--.","--.-",".-.",
                "...","-","..-","...-",".--","-..-",
                "-.--","--.."]
        dic = {"a" : ".-", "b" : "-...", "c" : "-.-.", "d" : "-..", "e" : ".", "f" : "..-.", 
               "g" : "--.", "h" : "....", "i" : "..", "j" : ".---", "k" : "-.-", "l" : ".-..", 
               "m" : "--", "n" : "-.", "o" : "---", "p" : ".--.", "q" : "--.-", "r" : ".-.", 
               "s" : "...", "t" : "-", "u" : "..-", "v" : "...-", "w" : ".--", "x" : "-..-", 
               "y" : "-.--", "z" : "--.."}
        out = []
        for x in words:
            X = list(x)
            X = [dic.get(n, n) for n in X]
            out.append("".join(X))
        return len(set(out))
        
