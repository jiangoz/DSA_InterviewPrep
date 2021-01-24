# Uses chaining
class HashTableC:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def add(self, key, val):
        h = self.get_hash(key)

        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                return
        self.arr[h].append((key, val))
    __setitem__ = add

    def get(self, key):
        h = self.get_hash(key)
        for e in self.arr[h]:
            if e[0] == key:
                return e[1]
    __getitem__ = get

    def delete(self, key):
        h = self.get_hash(key)

        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]
    __delitem__ = delete

# Uses linear probing (NOT WORKING)
# See: https://github.com/codebasics/py/blob/master/DataStructures/4_HashTable_2_Collisions/Solution/exercise_hash_table_linear_probing.ipynb


class HashTableLP:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def add(self, key, val):
        h = self.get_hash(key)

        if self.arr[h] is None:
            self.arr[h] = (key, val)
            return

        for e in self.arr:
            if e is None:
                e = (key, val)

    __setitem__ = add

    def get(self, key):
        h = self.get_hash(key)

        if self.arr[h][0] == key:
            return self.arr[h]
        for e in self.arr:
            if e is None:
                continue
            if e[0] == key:
                return e
    __getitem__ = get

    def delete(self, key):
        h = self.get_hash(key)

        if self.arr[h][0] == key:
            self.arr[h] = None
            return
        for e in self.arr:
            if e is None:
                continue
            if e[0] == key:
                e = None
    __delitem__ = delete


if __name__ == "__main__":
    t = HashTableC()
    t["march 6"] = 120
    t["march 6"] = 60
    t["dec 2"] = 5
    t["march 17"] = 459
    print(t.arr)
    print(t["march 17"])
    print(t["march 6"])
    del t["march 17"]
    print(t.arr)
    del t["march 6"]
    print(t.arr)

    print("===SEPARATION OF CHAINING AND LINEAR PROBING===")

    t2 = HashTableLP()
    t2["march 6"] = 120
    t2["march 6"] = 60
    t2["dec 2"] = 5
    t2["march 17"] = 459
    print(t2.arr)
    print(t2["march 17"])
    print(t2["march 6"])
    del t2["march 17"]
    print(t2.arr)
    del t2["march 6"]
    print(t2.arr)
