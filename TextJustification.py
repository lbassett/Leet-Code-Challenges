# Challenge: Text Justification --Not Completed--

# Given a list of words, and a linewidth, return a list of the lines for
# a justified block of text, with spaces distributed as evenly as possible, except on the last line.

# Note, my solution will not work if there is a word whose length is longer than the maxwidth


def fullJustify(self, words, maxWidth):
    """
    :type words: List[str]
    :type maxWidth: int
    :rtype: List[str]
    """

    for x in words:
        assert(len(x) <= maxWidth)
    
    retlist = []
    
    currline = []
    spaces = []
    currcount = 0
    
    numwords = len(words)
    counter = 0
    
    while counter < numwords:
        word = words[counter]
        wordleng = len(word)
        
        if (currcount + wordleng) <= maxWidth:
            currline += [word]
            currcount += wordleng
            if currcount < maxWidth:
                currline += [" "]
                currcount += 1
            else:
                retlist += self.mergeline(currline)
                currcount = 0
                currline = []
        else:
            spaces = maxWidth+1 - currcount
            num_spaces = len(currline)//2 -1
            if num_spaces == 0:
                currline[1] += (spaces-1)*" "
                retlist += self.mergeline(currline)
                currline = [word]
                currcount = wordleng
                if currcount < maxWidth:
                    currcount+= 1
                    currline += [" "]
                elif currcount == maxWidth:
                    retlist += self.mergeline(currline)
                    currcount= 0
                    currline = []
            else:
                eachspace = spaces // num_spaces
                extraspaces = spaces % num_spaces
                if num_spaces == 0:
                    currline[1] += (eachspace-1)*" "
                else:
                    currline = currline[:-1]
                    spacecounter = 0
                    while spacecounter < num_spaces:
                        index = spacecounter*2 +1
                        currline[index] += " "*eachspace
                        if extraspaces >0:
                            currline[index] += " "
                            extraspaces -= 1
                        spacecounter += 1
                retlist += self.mergeline(currline)
                currline = [word]
                currcount = wordleng
                if currcount < maxWidth:
                    currcount+= 1
                    currline += [" "]
        counter += 1
    
    if currcount >0:
        lastline = self.mergeline(currline[:-1])
        spaces = maxWidth - currcount +1
        lastline[0]+= spaces*" "
        retlist += lastline
    
    return(retlist)

def mergeline(self, line):
    string = ""
    for x in line:
        string += x
    
    return([string])
