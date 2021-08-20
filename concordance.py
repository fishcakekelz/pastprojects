from hash_quad import *
import string


class Concordance:

    def __init__(self):
        self.stop_table = None  # hash table for stop words
        self.concordance_table = None  # hash table for concordance

    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        self.stop_table = HashTable(191)

        try:
            new_file = open(filename, "r")
            words = new_file.read()
            new_file.close()

            words = words.split("\n")

            for word in words:
                self.stop_table.insert(word, 0)
        except:
            raise FileNotFoundError

    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        Process of adding new line numbers for a word (key) in the concordance:
            If word is in table, get current value (list of line numbers), append new line number, insert (key, value)
            If word is not in table, insert (key, value), where value is a Python List with the line number
        If file does not exist, raise FileNotFoundError"""
        
        try:
            in_file = open(filename)
            self.concordance_table = HashTable(191)
            count = 0
            
            for line in in_file:
                count += 1
                line = line.lower()
                line = line.strip()
                line = line.translate(str.maketrans("", "", "0123456789"))
                line = line.replace("'", "")
                line = line.translate(str.maketrans(string.punctuation, " " * len(string.punctuation)))

                words = line.split(' ')
                words = set(words)
                words = list(words)

                for i in range(len(words)):
                    if self.concordance_table.in_table(words[i]):
                        if str(count) not in str(self.concordance_table.get_value(words[i])):
                            self.concordance_table.insert(words[i], (
                                    (str(self.concordance_table.get_value(words[i]))) + ' ' + str(count)))
                    elif not self.stop_table.in_table(words[i]) and words[i] is not '':
                        self.concordance_table.insert(words[i], str(count))

            in_file.close()

        except FileNotFoundError:
            raise FileNotFoundError

    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""
        
        out_file = open(filename, 'w')
        concordance = []
        for i in range(self.concordance_table.table_size):
            if self.concordance_table.hash_table[i] is not None:
                concordance.append(str(self.concordance_table.hash_table[i].key))

        concordance.sort()

        for i in range(len(concordance)):
            if concordance[i] is not None:
                out_file.write(concordance[i] + ': ' + self.concordance_table.get_value(concordance[i]) + '\n')
            elif concordance[i] is not '' and (i == len(concordance) - 1):
                out_file.write(concordance[i] + ': ' + self.concordance_table.get_value(concordance[i]))

        out_file.close()

