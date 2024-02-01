def import_words():
    words = []
    with open("words.txt", "r") as fp:
        for line in fp:
            words.append(line.lower().strip())
    return words


class Is:
    def __init__(self, pos, ch):
        self.pos = pos - 1
        self.ch = ch.lower()

    def match(self, word):
        return self.pos < len(word) and word[self.pos] == self.ch

class IsNot:
    def __init__(self, pos, ch):
        self.pos = pos - 1
        self.ch = ch.lower()

    def match(self, word):
        return self.pos < len(word) and word[self.pos] != self.ch

class Contains:
    def __init__(self, chars):
        self.chars = [ch.lower() for ch in chars]

    def match(self, word):
        for ch in self.chars:
            if ch not in word:
                return False
        return True

class NotContains:
    def __init__(self, chars):
        self.chars = [ch.lower() for ch in chars]

    def match(self, word):
        for ch in self.chars:
            if ch in word:
                return False
        return True

class Length:
    def __init__(self, length):
        self.length = length

    def match(self, word):
        return len(word) == self.length

class NoRepeat:
    def match(self, word):
        return len(word) == len(set(word))

def filter_words(words, constraints):
    matches = []
    for word in words:
        is_match = True
        for c in constraints:
            if not c.match(word):
                is_match = False
                break
        if is_match:
            matches.append(word)
    return matches
            

words = import_words()
constraints = [
    Length(5),
    NotContains("AZUHYMSVBOK"),
    IsNot(4, "R"),
    IsNot(1, "R"),
    IsNot(3, "R"),
    Is(2, "R"),
    Is(5, "E"),
    Is(3, "I"),
    Contains("RET")
    
]

matches = filter_words(words, constraints)
for m in matches:
    print(m)
