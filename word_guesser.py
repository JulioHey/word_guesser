import pandas as pd
from classes.get_possible_word_list import GetPossibleWordList
from classes.get_better_guess import GetBetterGuessForWordList


class WordGuesser:
    def __init__(self, word_list, possible_word_list, better_guess) -> None:
        self.word_list = word_list
        self.possible_word_list = possible_word_list
        self.guesses = 1
        self.guess = better_guess

    def start(self):
        while len(self.possible_word_list) != 1:
            if self.guesses != 1:
                self.guess = self.get_better_guess()
            self.start_message()
            pattern_received = input('Digite o input recebido: ')
            self.possible_word_list = GetPossibleWordList(self.possible_word_list, pattern_received, self.guess).get_new_word_list()
            self.guesses += 1
        self.finish()

    def start_message(self):
        print(f'O melhor para essa lista de palavras é {self.guess}')

    def get_better_guess(self):
        print('Calculando melhor chute para a lista de palavras recebida...')
        guess = GetBetterGuessForWordList(self.possible_word_list, self.word_list).get_guess()
        return guess
    
    def finish(self):
        print(f'A palavra é {self.possible_word_list[0]}')
        print(f'Foram necessarios {self.guesses} chutes')

def list_from_path(path):
    data = pd.read_csv(path, header=None)
    data.rename(columns={0: "Palavra"}, inplace=True)
    word_df = data
    word_df.set_index('Palavra')
    word_list = list(word_df['Palavra'])
    return word_list

def game_input():
    print("No caso do jogo ser:\n Termo ou Letreco digite 1\n Wordle digite 2\n")
    return input("Digite: ")

class GameStart:
    def start(self):
        jogo = self.user_input()
        self.get_path(jogo)
        better_guess = self.better_guess(jogo)
        word_list, possible_word_list = self.get_word_lists()
        return word_list, possible_word_list, better_guess

    def user_input(self):
        jogo = self.game_input()
    
        while jogo != '1' and jogo != '2':
            print("Opa! Você digitou um valor inválido")
            jogo = game_input()

        return jogo

    def get_path(self, jogo):
        if jogo == '1':
            self.word_list_path = self.possible_word_list_path = 'lista_de_palavras/clean_words.csv'
        else:
            self.word_list_path = 'lista_de_palavras/wordle.txt'
            self.possible_word_list_path = 'lista_de_palavras/wordleA.txt'

    def better_guess(self, jogo):
        if jogo == '1':
            return 'serao'
        else:
            return 'soare'

    def get_word_lists(self):
        word_list = list_from_path(self.word_list_path)
        possible_word_list = list_from_path(self.possible_word_list_path)

        return word_list, possible_word_list

    def list_from_path(self, path):
        data = pd.read_csv(path, header=None)
        data.rename(columns={0: "Palavra"}, inplace=True)
        word_df = data
        word_df.set_index('Palavra')
        word_list = list(word_df['Palavra'])
        return word_list

    def game_input(self):
        print("No caso do jogo ser:\n Termo ou Letreco digite 1\n Wordle digite 2")
        return input("Digite: ")

if __name__ == '__main__':
    word_list, possible_word_list, better_guess = GameStart().start()

    guesser = WordGuesser(word_list, possible_word_list, better_guess)

    guesser.start()