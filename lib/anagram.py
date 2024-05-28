# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self,word_listing):
        matched_words=[]
        for word in word_listing:
            if sorted(word)== sorted(self.word):
                matched_words.append(word)
        return matched_words
        