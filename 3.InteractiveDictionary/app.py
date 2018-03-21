import json
from difflib import get_close_matches
data =  json.load(open("data.json"))

def convert(w):
    w = w.lower()
    if w in data:
         return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn =  input("Did you mean {} instead? Y for Yes, N for No:  " .format(get_close_matches(w, data.keys())[0]))
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        else:
            return "Good luck with other words and we will help you with typo"
    else:
        return "Pardon, but the word you entered doesn't exist"

word = input("Enter a word: " )
output = convert(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
    
