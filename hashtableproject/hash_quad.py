class Hash:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:

    def __init__(self, table_size):         # can add additional attributes
        self.table_size = table_size        # initial table size
        self.hash_table = [None]*table_size # hash table
        self.num_items = 0                  # empty hash table

    def insert(self, key, value):
        """ Inserts an entry into the hash table (using Horner hash function to determine index, 
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is any object (e.g. Python List).
        If the key is not already in the table, the key is inserted along with the associated value
        If the key is is in the table, the new value replaces the existing value.
        When used with the concordance, value is a Python List of line numbers.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1)."""
        hash_val = Hash(key, value)
        self.hash_table[self.horner_hash(key)] = hash_val
        self.num_items += 1

        if self.get_load_factor() > 0.5:
            prev = HashTable(self.table_size)
            prev.num_items = self.num_items
            prev.hash_table = self.hash_table
            prev.table_size = self.table_size

            self.table_size = self.table_size * 2 + 1
            self.num_items = 0
            self.hash_table = [None] * self.table_size

            for i in range(prev.table_size):
                if prev.hash_table[i] is not None:
                    self.insert(prev.hash_table[i].key, prev.hash_table[i].value)

    def horner_hash(self, key):
        """ Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification."""
        k = 0
        counter = 1
        n = len(key)
        if n > 8:
            n = 8
        for i in range(n):
            k += ord(str(key[i])) * (31 ** (n - 1 - i))
        ind = k % self.table_size

        first = ind

        while self.hash_table[ind] is not None:
            if self.hash_table[ind].key == key:
                break

            ind = counter ** 2 + first
            counter += 1
            if ind >= self.table_size:
                ind = ind % self.table_size

        return ind

    def in_table(self, key):
        """ Returns True if key is in an entry of the hash table, False otherwise. Must be O(1)."""
        index = self.horner_hash(key)
        if self.hash_table[index] is not None:
            if key == self.hash_table[index].key:
                return True
        return False

    def get_index(self, key):
        """ Returns the index of the hash table entry containing the provided key.
                If there is not an entry with the provided key, returns None. Must be O(1)."""
        if self.hash_table[self.horner_hash(key)] is None:
            return None
        if self.hash_table[self.horner_hash(key)].key is key:
            return self.horner_hash(key)

    def get_all_keys(self):
        """ Returns a Python list of all keys in the hash table."""
        all_keys = []
        for i in range(len(self.hash_table)):
            if self.hash_table[i] is not None:
                all_keys.append(self.hash_table[i].key)
        return all_keys

    def get_value(self, key):
        """ Returns the value (for concordance, list of line numbers) associated with the key.
        If key is not in hash table, returns None. Must be O(1)."""
        if self.hash_table[self.horner_hash(key)] is not None:
            if self.hash_table[self.horner_hash(key)].key == key:
                return self.hash_table[self.horner_hash(key)].value
        else:
            return None

    def get_num_items(self):
        """ Returns the number of entries (words) in the table. Must be O(1)."""
        return self.num_items

    def get_table_size(self):
        """ Returns the size of the hash table."""
        return self.table_size

    def get_load_factor(self):
        """ Returns the load factor of the hash table (entries / table_size)."""
        return self.num_items / self.table_size

