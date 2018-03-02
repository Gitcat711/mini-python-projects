#Import Files.
from urllib.request import urlopen

# 1. Reading the text from documents.
def read_text():
    quotes  = open("/Users/prathmeshpathak/mini-python-projects/2.Curse_Editor/lines.md")
    content_of_file = quotes.read()
    print(content_of_file)
    quotes.close()
    check_profane(content_of_file)


# 2. Checking for Curse Words.
def check_profane(text_to_check):
    connection = urlopen(" http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    connection.close()
    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("This Document has no curse words!!")

read_text()
