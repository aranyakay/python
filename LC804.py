def lc804(self):
    mosi = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..",
    "--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    out = []
    for x in self:
        X = list(x)
        for n,i in enumerate(X):
            X[n] = mosi[ord(i)-97]
        out.append("".join(X))
    return(len(set(out)))
