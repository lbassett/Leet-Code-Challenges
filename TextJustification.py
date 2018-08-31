# Challenge: Text Justification --Not Completed--

# Given a list of words, and a linewidth, return a list of the lines for
# a justified block of text, with spaces distributed as evenly as possible, except on the last line.



def fullJustify(self, words, maxWidth):
    """
    :type words: List[str]
    :type maxWidth: int
    :rtype: List[str]
    """
    
    retlist = []
    
    currline = []
    spaces = []
    currcount = 0
    
    numwords = len(words)
    counter = 0
    
    while counter < numwords:
        word = words[counter]
        wordleng = len(word)
        
        if (currcount + wordleng)<maxwidth:
            currline += [word]
            currcount += wordleng
            if currcount != maxwidth:
                currline += [" "]
                currcount += 1
            else:
                retlist += [currline]
                currcount = 0
                currline = ""
        else:
            spaces = maxwidth - currcount
            num_spaces = len(currline)/2 -1
            eachspace = spaces // num_spaces
            extraspaces = spaces % num_spaces
            if num_spaces == 0:
                currline[1] += (eachspace-1)*" "
            else:
                currline = currline[:-1]
                spacecounter = 0
                while spacecounter < num_spaces:
                    index = spacecounter*2 +1
                    currline[index] += " "*(eachspace)
                    if extraspaces >0:
                        currline[index] += " "
                        extraspaces -= 1
                    spacecounter += 1
        counter += 1
