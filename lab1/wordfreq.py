def tokenize(lines): #Input är rader text som delas upp i enskilda ord
    words = [] # tom lista med ord
    for line in lines:
        print(line)
        start = 0
        while start < len(line):
            while start < len(line) and line[start].isspace(): #While-satsen kollar om det finns whitespaces och hoppar över dem.
                start = start+1
            if start >= len(line):
                break
            end=start               #Ta reda på slutet av ordet
            if line[end].isalpha():
                while end < len(line) and line[end].isalpha(): #Ta reda på om "tecknet" är en bokstav och så länge det är efterföljade bokstäver fortsätter while-satsen tills de inte finns efterföljande bokstäver.  
                    end+=1
            elif line[end].isdigit() :
                while end < len(line) and line[end].isdigit(): #Ta reda på om "tecknet" är en siffra och så länge det är efterföljande siffror fortsätter whilesatsen tills de inte finns efterföljande siffror. 
                    end+=1
            else:
                end+=1
            #print(line[start:end]) 
            words.append(line[start:end].lower()) # sätter ihop början och slutet av ett ord så det bildar ett ord
            
            start = end # börjar om på nytt ord
    return words    # En lista med ord

def countWords(words, stopWords): #Räknar antalet ord dyker upp
    counts={} # Skapa en dictionary
    for word in words: 
        if word not in stopWords: # ifall ordet inte är med i stopwords så körs if-satsen. Stopwords fungerar som ett filter
            if word in counts.keys():#Räknar upp ett om ordet existerar i words
                counts[word] += 1
            else:
                counts[word] = 1 #Skapar ett nytt ord som inte exiterar i words och ger ordet värdet ett. 
    return counts # en dictionary med keys (nycklar) och values(värden). 

def printTopMost(frequencies,n): # skriver ut de n vanligaste orden som dyker upp 
    i = 0
    sorted_freq=sorted(frequencies.items(), key=lambda x: -x[1]) #Sorterar från vanligaste till ovanligaste förekommande ordet. 
    for word,freq in sorted_freq:
        if n<=i:
            break
        else:
            i+=1
        print(word.ljust(20) + str(freq).rjust(5)) # printar ordet och hur vanligt det är att ordet förekommer.


