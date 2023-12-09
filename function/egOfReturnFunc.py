#printing 3 hashes  
def hashPattern(n):
    hash = "# " *n
    hash = hash.strip(" ")
    return hash 
n = 3
result = hashPattern(n)
print(result) 

#print rank one 
def rank(score):
    msg = "Rank: " + score
    return msg
#score = "One"
result = rank(score = "One")
print(result)

#return reversed word
def reverseWord(word):
    msg = word[::-1]
    return msg 
result = reverseWord(word = "ognehtog")
print(result)

#muntiply 3 numbers 
def muntiply(n):
    mun = n * n* n
    return mun 
result = muntiply(n = 3)
print(result)




