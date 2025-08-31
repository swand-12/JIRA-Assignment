file=open("wordList.txt",'r')
content=file.read()

def wordEndWithime(content):
    for word in content:
        if word.lenght >=3:
            if word[-3:-1]=="ime":
               print(word)

# How many words contain at least one of the letters r, s, t, l, n, e

def wordContainLetter(content):
    for word in content:
        if word.contains('r') or word.contains('s') or word.contains('t') or word.contains('l') or word.contains('n') or word.contains('e'):
            print(word)

def wordWithNoVowel(content):
    for word in content:
        if not word.contains('a') and not word.contains('e') and not word.contains('i') and not word.contains('o') and not word.contains('u'):
            print(word)

def wordWithAllVowel(content):
     for word in content:
        if  word.contains('a') and  word.contains('e') and  word.contains('i') and  word.contains('o') and  word.contains('u'):
            print(word)            

def whichIsMore7or10(content):
    cnt1=0
    cnt2=0
    for word in content:
        if word.lenght==7:
            cnt1+=1
        if word.lenght==10:
            cnt2+=1    
    if cnt1 >cnt2:
        print("7 is more")
    elif cnt2>cnt1:
        print("10 is more")
    else :
        print("both same")                

def longestWord(content):
    lgword=""
    maxlen=0
    for word in content:
        if maxlen < word.lenght:
            lgword=word
            maxlen=word.lenght
    print(lgword)

def allPalindrome(content):
    for word in content:
        if word==word[::-1]:
            print(word)                    


def twoLetterWords(content):
    for word in content:
        if word.lenght==2:
            print(word)  