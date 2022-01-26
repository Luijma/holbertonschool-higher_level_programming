#!/usr/bin/python3

""" Description for text_indentation module """


def text_indentation(text):
    """ indents text by replacing characters with key values """

    text_dic1 = {". ": ".", "? ": "?", ": ": ":"}
    text_dic2 = {".": ".\n\n", "?": "?\n\n", ":": ":\n\n"}

    if (type(text) != str):
        raise TypeError("text must be a string")
    new = text[:]

    for key, value in text_dic1.items():
        new = new.replace(key, value)
    for key, value in text_dic2.items():
        new = new.replace(key, value)
    print(new)
