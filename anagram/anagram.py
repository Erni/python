def detect_anagrams(word, candidates):
    response = []

    lword = word.lower()

    anagram = True
    for w in candidates:
        if len(w) != len(lword) or lword == w.lower():
            continue
        lw = w.lower()
        for c in lword:
            if c not in lw:
                anagram = False
                break
            else:
                lw = lw.replace(c,'',1)
        if anagram == True and w.lower() not in response:
            response.append(w)
        anagram = True

    return response