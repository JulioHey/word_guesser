class CreatePattern:
    def __init__(self, correct, attempt) -> None:
        self.correct = list(correct)
        self.attempt = list(attempt)
        self.pattern = list('CCCCC')
        self.correct_indexes = []

    def definy_pattern(self):
        try:
            self.find_green()
            self.find_yellow()
            return ''.join(self.pattern)
        except Exception:
            print(f'Palavra que deu erro {self.attempt} com {self.correct}')

    def find_green(self):
        for index in range(5):
            if self.attempt[index] == self.correct[index]:
                self.pattern[index] = 'G'
                self.correct_indexes.append(index)
                self.correct[index] = '1'
    
    def find_yellow(self):
        for index in range(5):
            if self.attempt[index] in self.correct and index not in self.correct_indexes:
                index_achado = self.correct.index(self.attempt[index])
                if index_achado not in self.correct_indexes:
                    self.pattern[index] = 'Y'
                del self.correct[index_achado]