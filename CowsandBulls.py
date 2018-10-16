# Challenge: Cows and Bulls

# You are playing the following Bulls and Cows game with your friend:
# You write down a number and ask your friend to guess what the number is.
# Each time your friend makes a guess, you provide a hint that indicates how
# many digits in said guess match your secret number exactly in both digit and
# position (called "bulls") and how many digits match the secret number but
# locate in the wrong position (called "cows"). Your friend will use
# successive guesses and hints to eventually derive the secret number.

# Write a function to return a hint according to the secret
# number and friend's guess, use B to indicate the bulls and C to indicate the cows. 

# Please note that both secret number and friend's guess may contain duplicate digits.

# You may assume that their lengths are always equal.

def getHint(self, secret, guess):
    """
    :type secret: str
    :type guess: str
    :rtype: str
    """
    
    pasts = {}
    pastg = {}
    
    bulls = 0
    cows = 0
    
    index = 0
    leng = len(secret)
    
    while index< leng:
        s = secret[index]
        g = guess[index]
        if s == g:
            bulls+=1
        else:
            if s in pastg:
                if pastg[s] > 0:
                    pastg[s] -= 1
                    cows +=1
                else:
                    if s in pasts:
                        pasts[s] += 1
                    else:
                        pasts[s] = 1
            else:
                if s in pasts:
                    pasts[s] += 1
                else:
                    pasts[s] = 1     
            if g in pasts:
                if pasts[g] > 0:
                    pasts[g] -= 1
                    cows +=1
                else:
                    if g in pastg:
                        pastg[g] += 1
                    else:
                        pastg[g] = 1
            else:
                if g in pastg:
                    pastg[g] += 1
                else:
                    pastg[g] = 1 
        index += 1
    return(str(bulls) + "B" + str(cows) + "C")
