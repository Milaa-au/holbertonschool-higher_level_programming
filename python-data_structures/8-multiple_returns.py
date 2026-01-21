#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        tuple = (len(sentence), sentence[0])
        print("Length: {} - First character: {}".format(tuple[0], tuple[1]))
