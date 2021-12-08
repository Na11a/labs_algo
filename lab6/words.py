class Words:

    def __init__(self, list_word, count):
        self.list_words = sorted(list_word, key=len)
        self.chain_words = {}
        self.example = {}
        self.max_chain = 0

    def counter(self, visible=False):
        if visible:
            print('-----------------------CHAIN-----------------------')

        for word in self.list_words:
            len_chain = self.count_chain(word, visible)
            if len_chain > self.max_chain:
                self.max_chain = len_chain
        if visible:
            print('---------------------------------------------------')

    def count_chain(self, word, visible):
        len_chain = 1
        past_word = ''

        for index in range(0, len(word)):
            possible_word = word[:index] + word[index + 1:]
            if possible_word in self.chain_words:
                if len_chain < self.chain_words[possible_word]:
                    len_chain = self.chain_words[possible_word]
                    past_word = possible_word

        self.example[word] = past_word

        if visible: self.visible(word)
        self.chain_words[word] = len_chain + 1
        return len_chain

    def get_max_chain(self, visiable=False):
        if visiable: print(f'max chain: {self.max_chain}')
        return self.max_chain

    def visible(self, word):

        new_chain = word
        string = new_chain
        while True:
            new_chain = self.example[new_chain]
            if new_chain == '':
                break
            else:
                string += ' -> ' + new_chain
        print(string)
