import string

vowel = 'aeyuioAEYUIO'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
First_key=[7,16]

def cmptind(word):
    x=0
    for beta in alphabet:
        if word == beta:
            return x
        x +=1

def Search_Dekey():
    a=0
    for b in range(26):
        if(b*First_key[0])%26 == 1:
          a = b
          break
    keyD =(a,-a*First_key[1])
    return keyD

def Decrypt_letter(letter):
    DFirst_key=Search_Dekey()
    x=DFirst_key[0]*cmptind(letter)+DFirst_key[1]
    x%=26
    return alphabet[x]

def Decrypt_Word(word):
    Initial_word =''
    for letter in word:
        if letter in alphabet:
            Initial_word +=Decrypt_letter(letter)
        else:
            Initial_word+=letter
    return Initial_word

def SearchKey(word):

    key=len(word)//2
    return key
def Decrypt(word):

    wordIn=''
    key = SearchKey(word)
    for letter in word:
        val = ord(letter) - key
        wordIn = wordIn + chr(val)

    return wordIn

def SuperDecrypt(word):
    In_word=Decrypt(word)
    In_word=Decrypt_Word(In_word)

    return In_word



