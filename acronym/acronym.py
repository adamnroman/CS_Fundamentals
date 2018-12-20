def abbreviate(words):
    acronym = []
    #list of characters that marks when a letter should be used in the acronym.
    spec_chars = [" ", "-"]
    #the first letter of each string will be the first letter of the acronym.
    acronym.append(words[0])
    for x in range(len(words)):
        if words[x] in spec_chars:
            #if a space or a hyphen appears then return the next character to list. Uppercase.
            if words[x+1].isalpha():
                #Only add the next character if it's a letter.
                acronym.append(words[x+1].upper())
    return "".join(acronym)

