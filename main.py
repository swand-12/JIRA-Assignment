# Read the file and split into words
with open("wordList.txt", 'r') as file:
    content = file.read().splitlines()  # split by whitespace

# 1. Words ending with 'ime'
def wordEndWithime(words):
    return [word for word in words if word.endswith('ime')]

# 2. Words containing at least one of r, s, t, l, n, e
def wordContainLetter(words):
    letters = set('rstlne')
    return [word for word in words if any(char in letters for char in word)]

# 3. Words with no vowels
def wordWithNoVowel(words):
    vowels = set('aeiou')
    return [word for word in words if not any(v in word for v in vowels)]

# 4. Words with all vowels (a, e, i, o, u)
def wordWithAllVowel(words):
    vowels = set('aeiou')
    return [word for word in words if vowels.issubset(set(word))]

# 5. Which is more: words of length 7 or 10
def whichIsMore7or10(words):
    cnt7 = sum(1 for word in words if len(word) == 7)
    cnt10 = sum(1 for word in words if len(word) == 10)

    if cnt7 > cnt10:
        return "7 is more"
    elif cnt10 > cnt7:
        return "10 is more"
    else:
        return "both same"

# 6. Longest word
def longestWord(words):
    return max(words, key=len)

# 7. All palindromes
def allPalindrome(words):
    return [word for word in words if word == word[::-1]]

# 8. Two-letter words
def twoLetterWords(words):
    return [word for word in words if len(word) == 2]


# Example usage:
print("Words ending with 'ime':", wordEndWithime(content))
print("Words containing r,s,t,l,n,e:", wordContainLetter(content))
print("Words with no vowels:", wordWithNoVowel(content))
print("Words with all vowels:", wordWithAllVowel(content))
print("Which is more, 7 or 10 letters:", whichIsMore7or10(content))
print("Longest word:", longestWord(content))
print("All palindromes:", allPalindrome(content))
print("Two-letter words:", twoLetterWords(content))
