import random
"""Word Finder: finds random words from a dictionary."""


class WordFinder:

    def __init__(self, doc):
        """open given file and parse text in file"""
        docfile = open(doc)
        self.words = self.edit(docfile)
        print(f'{len(self.words)} words read')
    
    def edit(self, docfile):
        return [n.strip() for n in docfile]

    def random(self):
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):

    def edit(self, docfile):
        return [n.strip() for n in docfile if n.strip() and '#' not in n]


    
