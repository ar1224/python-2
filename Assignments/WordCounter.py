class WordCounter:

    def __init__(self, sentence):
        self.sentence = sentence
        self.count = 0
    
    def count_words(self):
        list = self.sentence.split()
        self.count = len(list)

    def get_word_count(self):
        return self.count
    
    def get_shortest_word(self):
        list = self.sentence.split()
        min = len(list[0])
        for x in list:
            if len(x) < min:
                min = len(x)
        return min
    
    def get_longest_word(self):
        list = self.sentence.split()
        max = len(list[0])
        for x in list:
            if len(x) > max:
                max = len(x)
        return max