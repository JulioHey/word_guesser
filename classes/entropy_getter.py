import pandas as pd
import math
from classes.create_pattern import CreatePattern


class EntropyGetter:
    def __init__(self, word ,possible_word_list):
        self.word = word
        self.possible_word_list = possible_word_list
        self.total = len(possible_word_list)
    
    def entropy(self):
        self.get_df()
        self.manipulate_dataframe()
        return self.get_entropy()

    def get_entropy(self):
        sum = 0

        for row in self.entropy_df.iterrows():
            sum += (row[1].Total * row[1].Entropia)

        return float(sum) / self.total
    
    def manipulate_dataframe(self):
        self.manipulate_columns()
        self.add_percentage_to_df()
        self.add_entropy_to_df()
    
    def manipulate_columns(self):
        self.entropy_df = self.entropy_df.T
        self.entropy_df.rename(columns={0: 'Total'}, inplace=True)

    def add_entropy_to_df(self):
        self.entropy_df['Entropia'] = self.entropy_df['Porcentagem'].apply(lambda percentage: math.log2( 100 / (percentage)))

    def add_percentage_to_df(self):
        self.entropy_df['Porcentagem'] = self.entropy_df['Total'].apply(lambda e: e * 100.0 / self.total)

    def get_df(self):
        padroes = []
        for word in self.possible_word_list:
            padroes.append(CreatePattern(word, self.word).definy_pattern())

        self.padroes_series = pd.Series(padroes)
        self.entropy_df = pd.DataFrame([self.padroes_series.value_counts()])