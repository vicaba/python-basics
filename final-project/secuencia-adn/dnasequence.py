from collections import Counter

class DNASequence:
    def __init__(self, sequence, name):
        self.sequence = sequence
        self.name = name
        self.base_count = self.analyzeSecuence()

    def analyzeSecuence(self):
        return Counter(self.sequence)
