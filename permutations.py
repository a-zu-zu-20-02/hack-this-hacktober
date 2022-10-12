def permutations(inputstr):
    thearray = []

    def permutations_rec(string, theindex):
        arrayOfLetters = list(string)
       if theindex == len(arrayOfLetters):
            thearray.append(''.join(arrayOfLetters))
        else:
            for i in range(theindex, len(arrayOfLetters)):
                arrayOfLetters[theindex], arrayOfLetters[i] = arrayOfLetters[i], arrayOfLetters[theindex]
                permutations_rec(arrayOfLetters, theindex+1)

    permutations_rec(inputstr, 0)
    out = list(dict.fromkeys(thearray))

    return out

