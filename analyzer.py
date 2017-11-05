import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""

        self.positives = []
        self.negatives = []

        pos = open('positive-words.txt', 'r')
        neg = open('negative-words.txt', 'r')

        for line in pos:
            if line and line[0].isalpha():
                self.positives.append(line.strip("\n"))

        for line in neg:
            if line and line[0].isalpha():
                self.negatives.append(line.strip("\n"))
        
    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        
        score = 0
        texttok = nltk.wordpunct_tokenize(text)
    
        for i in range(len(texttok)):
            for j in range(len(self.positives)):
                pick = self.positives[j]
                if pick == texttok[i]:
                    score += 1
            for j in range(len(self.negatives)):
                pick = self.negatives[j]
                if pick == texttok[i]:
                    score -= 1
        return score

