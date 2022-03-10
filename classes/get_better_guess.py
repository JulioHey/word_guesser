from classes.entropy_getter import EntropyGetter
import pandas as pd


class GetBetterGuessForWordList:
    def __init__(self, possible_word_list: list , word_list: list):
        self.word_list = word_list
        self.possible_word_list = possible_word_list
    
    def get_guess(self):
        self.get_mean_entropy_df()
        self.manipulate_df()
        return self.get_max_entropy_guess()
        
    def get_mean_entropy_df(self):
        entropy = []

        for word in self.word_list:
            entropy_getter = EntropyGetter(word, self.possible_word_list)
            entropy.append(entropy_getter.entropy())
            del entropy_getter

        self.entropy_mean_df = pd.DataFrame([entropy, self.word_list])
    
    def manipulate_df(self):
        self.entropy_mean_df = self.entropy_mean_df.T
        self.entropy_mean_df.rename(columns={0: 'Mean-Entropy', 1: 'Word'}, inplace = True)

    def get_max_entropy_guess(self):
        max_mean_entropy = self.entropy_mean_df['Mean-Entropy'].max()
        target_row = self.entropy_mean_df[self.entropy_mean_df['Mean-Entropy'] == max_mean_entropy]
        return target_row['Word'].values[0]