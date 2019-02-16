def ReadFile(file):
    """Reads The file, counts the total number of each character that appears in the file
    Returns a dictionary and a list. The dictionary contains each character and the total number
    of times it appears. The list contains every character that appears in the text file"""
    letters = []
    tempDic = {}
    with open(file + ".txt", 'r') as f:
        for line in f:
            letters.extend(line.lower())

    for i in range(len(letters)):
        tempDic[letters[i]] = 0

    with open(file+".txt", 'r') as f:
        for line in f:
            for i in line:
                tempDic[i.lower()] += 1
    return tempDic, letters

def getFrequencies(file):
    """Calculates the frequencies of each character that appears in the file. Returns a list that contains the label and its
    probability of that character appearing in the text file"""
    frequencies = []
    lettersDic, allLetters = ReadFile(file)

    number_frequencies = 0
    symbol_frequencies = 0
    for i in lettersDic:
        if(str(i).isalpha() or str(i).isspace()):
            if(str(i).isspace()):
                frequencies.append(("Spaces" + ", {:0.4f}".format(lettersDic[i] / len(allLetters)), lettersDic[i] / len(allLetters)))
            else:
                frequencies.append((i + ", {:0.4f}".format(lettersDic[i] / len(allLetters)), lettersDic[i] / len(allLetters)))
        elif str(i).isdigit():
            number_frequencies += lettersDic[i]
        else:
            symbol_frequencies += lettersDic[i]
    number_frequencies /= len(allLetters)
    symbol_frequencies /= len(allLetters)
    if number_frequencies > 0:
        frequencies.append(("Numbers" + ", {:0.4f}".format(number_frequencies), number_frequencies))
    if symbol_frequencies > 0:
        frequencies.append(("Symbol" + ", {:0.4f}".format(symbol_frequencies), symbol_frequencies))
    return frequencies