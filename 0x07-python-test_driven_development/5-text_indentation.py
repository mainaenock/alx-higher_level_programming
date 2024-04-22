#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    clean = text.strip()
    results = ""
    for words in clean:
        results += words
        if words in "?.:":
            results += "\n\n"
    print("{}".format(results))
