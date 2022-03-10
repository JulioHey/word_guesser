from classes.create_pattern import CreatePattern


class GetPossibleWordList:
    def __init__(self, possible_word_list: list , pattern: str, word_input: str):
        self.pattern = pattern
        self.possible_word_list = possible_word_list
        self.word_input = word_input
    
    def get_new_word_list(self):
        self.fill_new_possible_words()
        return self.new_possible_words

    def fill_new_possible_words(self):
        self.new_possible_words = []
        for word in self.possible_word_list:
            self.check_if_word_is_possible(word)
    
    def check_if_word_is_possible(self, word):
        pattern_class = CreatePattern(word, self.word_input)
        patter_received = pattern_class.definy_pattern()
        del pattern_class
        if (patter_received == self.pattern):
            self.new_possible_words.append(word)