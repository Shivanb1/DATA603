


#importing libraries 
import requests
import collections
import re 
#Reading the text from url 
url = 'https://www.gutenberg.org/files/2600/2600-0.txt'
r = requests.get(url, allow_redirects=True)
textdataBytes  = r.content
#decoding
textdata = textdataBytes.decode("utf-8") 
ListOfWords = re.split("[^a-zA-Z_\',-]+", textdata)
out = collections.Counter(ListOfWords)
print({k: v for k, v in sorted(out.items(), key=lambda item: item[1])})
print("Length of unique words",len(out))







