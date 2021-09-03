import wordfreq #importerar biblotekt
import sys
import urllib.request

def main():
    
    response = urllib.request.urlopen(sys.argv[2]) #laddar in en lista ifrån webben
    lines = response.read().decode("utf8").splitlines() #läser igenom alla rader
    print(lines)

    stopwordsfile = open(sys.argv[1], encoding="utf-8") #öppnar filen för stopwords
    # stopwords = wordfreq.tokenize(stopwordsfile) #smartare lösning men efterfrågas inte i denna lab
    stopwords = []
    for line in stopwordsfile:
        stopwords.append(line.strip()) #tar bort alla whitespaces som annars tokenize gör
    stopwordsfile.close() #stänger filen för stopwords

    words= wordfreq.tokenize(lines) # ta in orden från en fil (webben)
    count = wordfreq.countWords(words,stopwords) #Räknar antalet ord, samt filtrerar mha stopwords
    wordfreq.printTopMost(count, int(sys.argv[3])) 

    #file = open(sys.argv[2], encoding="utf-8") #Laddar fil från labben såsom article1 osv
    #words = wordfreq.tokenize(file)
    #count = wordfreq.countWords(words,stopwords)
    #wordfreq.printTopMost(count, int(sys.argv[3]))
    #file.close()

main()

#python3 topmost.py eng_stopwords.txt examples/article1.txt 20