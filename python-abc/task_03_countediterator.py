#!/usr/bin/python3


class CountedIterator:
    def __init__(self, iterable):
        self.__iterator = iter(iterable)
        self.__counter = 0

    def get_count(self):
        return self.__counter

    def __next__(self):
        item = next(self.__iterator)
        self.__counter += 1
        return item

    def __iter__(self):
        return self
