import os
import random

class Word():
    # - Class handling the words inside of the homework_writer
    def __init__(self, word, ok_ltrs, need_ltr):
        self.word = word
        self.ok_ltrs = ok_ltrs
        self.need_ltr = need_ltr

    @property
    def has_ok_ltrs(self):
        for letter in self.word:
            if letter not in self.ok_ltrs:
                return False
        return True
    
    @property
    def has_need_ltr(self):
        if self.need_ltr not in self.word:
            return False
        return True

    @property
    def get_word_length(self):
        return len(self.word)

    @property
    def is_capital(self):
        if self.word[0].upper():
            return True
        return False

    def longer_than(self, length):
        if self.get_word_length <= int(length):
            return False
        return True


class Homework():
    # - Class handling the homework
    def __init__(self, ok_ltrs, need_ltr, eng, seperator):
        self.ok_ltrs = ok_ltrs
        self.need_ltr = need_ltr
        self.eng = eng
        self.seperator = seperator

        self.ok_words = ""
        self.rsrc = ""
        self.homework = ""

        # Set resources
        plain_rsrc = self.get_rsrc_txt()
        self.rsrc = self.get_rsrc_list(plain_rsrc)

    @classmethod
    def get_rsrc_list(cls, rsrc):
        return rsrc.split()

    def combine_words(self, words):
        txt = ""
        random.shuffle(words)
        for word in words:
            txt = txt + word.word + self.seperator
        return txt[:-1]

    def get_rsrc_txt(self):
        # Get text for each file in resources
        rsrc_text = ""
        rsrc_folder_cs = os.listdir("./rsrc/cs")
        for src in rsrc_folder_cs:
            rsrc_text = rsrc_text + open("./rsrc/cs/"+src, "r", encoding="utf-8").read()

        if self.eng:
            rsrc_folder_eng = os.listdir("./rsrc/eng")
            for src in rsrc_folder_eng:
                rsrc_text = rsrc_text + open("./rsrc/eng/"+src, "r", encoding="utf-8").read()
        return rsrc_text


    def get_ok_words(self):
        words = []
        for word in self.rsrc:
            w = Word(word, self.ok_ltrs, self.need_ltr)

            if w.has_ok_ltrs and w.has_need_ltr:
                words.append(w)
                continue

        return words

    def get_unique_words(self, words):
        new_words = []
        new_words_text = []

        for word in words:
            if word.word not in new_words_text:
                new_words.append(word)
                new_words_text.append(word.word)

        return new_words   

    def get_capital_words(self, words):
        new_words = []
        for word in words:
            if word.is_capital:
                new_words.append(word)

        return new_words

    def get_words_with_min_length(self, words, min_length):
        new_words = []
        for word in words:
            if word.longer_than(min_length):
                new_words.append(word)

        return new_words

class HomeworkWriter():
    def __init__(self, ok_ltrs, need_ltr, eng, only_capitals, unique_words, seperator, min_length_word, max_length):
        # Define parameters
        self.only_capitals = only_capitals
        self.min_length_word = min_length_word
        self.max_length = max_length
        self.unique_words = unique_words

        # Create an instance of homework
        hw = Homework(ok_ltrs, need_ltr, eng, seperator)
        self.hw_words = hw.get_ok_words()

        # Get the required words
        if self.only_capitals:
            self.hw_words = hw.get_capital_words(self.hw_words)

        if self.min_length_word:
            self.hw_words = hw.get_words_with_min_length(self.hw_words, self.min_length_word)

        if self.unique_words:
            self.hw_words = hw.get_unique_words(self.hw_words)

        if self.max_length:
            self.adjust_word_size()

        # Set the final homework text
        self.text = hw.combine_words(self.hw_words)

    @classmethod
    def get_length(cls, words):
        length = 0
        for word in words:
            length += len(word.word)

        return length

    def adjust_word_size(self):
        words = []
        length = 0

        for word in self.hw_words:
            if length > (len(word.word) + int(self.max_length)):
                break
            words.append(word)
            length += len(word.word)

        self.hw_words = words
