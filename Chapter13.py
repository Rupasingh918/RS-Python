"""Read a File ,remove the puntuation,convert to lowercase,total number of words, freq of each word. """
import re
import string
word_in_book =dict()
total_word =0
header =True

fbook = open ("A Little Journey.txt", 'r')
fwordlist = open("words.txt", 'r')


for line in fbook :
    if re.search(r'^\*\*\*', line):
        header =False
    if header == False:
        """Change everything to lower. """
        line_lower =line.lower()
        """Remove the punctuation from the line. """
        line_lower = re.sub('['+string.punctuation+']', ' ', line_lower)
        words = line_lower.split()
        for word in words:
            total_word = total_word +1
            word_in_book[word]= word_in_book.get(word,0)+1
print ("#################################################")
print ("The total word in the Book :",total_word)
print ("#################################################")
print (word_in_book)

"""Iterate over the list of tuples sorted by 0th index i.e. value in reverse order"""
t_book = []
for key, value in word_in_book.items():
    t_book.append((value,key))

t_book.sort(reverse=True)
print ("#################################################")
print("The most common words are :")
print ("#################################################")
for freq , word in t_book[:20]:
    print (word , freq, sep ='\t')


"""print all the words in the book that are not in the words lists. """
print ("#########################################################")
print ("The unique words in the BOOK which is not in word list")
print ("##########################################################")
t_wordlist =[]
for line_word in fwordlist:
    words = line_word.strip()
    t_wordlist.append(words)

for i in word_in_book.keys():
    if i not in t_wordlist:
        print (i)
print ("#################################################")
