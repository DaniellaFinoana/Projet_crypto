import string

vowel = 'aeyuioAEYUIO'
alphabet = list(string.ascii_letters + string.digits)
def cmptind(word):
    x=0
    for beta in alphabet:
        if word == beta:
            return x
        x +=1
def SearchKey(word):
    key1=0
    for letter in word:
     ltt=letter
     for letter in vowel:
         if ltt == letter:
             key1+=1
    if key1==0:
        key1=len(word)//2
    wordcrypt=str()
    for letter in word:
        wordcrypt+=chr(ord(letter)+3)

    key2=len(word)-key1;
    key =[key1,key2]
    return key

def FirstFunction(letter,a,b):
    val = a*cmptind(letter)+b
    val%=len(alphabet)
    return alphabet[val]

def firstCrypt(word):
    key = SearchKey(word)
    wordcode=''
    for letter in word:
     wordcode=wordcode+FirstFunction(letter,key[0],key[1])

    return wordcode

def crypt(word):
    key=SearchKey(word)
    k=key[1]
    wordcrypt=firstCrypt(word)+alphabet[k]

    return wordcrypt
mot="finoana"
print(crypt(mot))




