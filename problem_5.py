class TrieNode:
    def __init__(self):
        """ Initialize the node """
        self.children = {}
        self.is_word = False
        self.sub_word = False

    def insert(self, char):
        """
        Insert into the node

        Args:
            char(string): character to insert 
        Return:
            inserted node
        """
        new_node = TrieNode()
        self.children[char] = new_node
        return new_node

    def suffixes(self, suffix = ''):
        """
        Recursive function that collects the suffix for
        all complete words below this point

        Args:
            suffix(string): suffix 
        Return:
            list of suffixes
        """
        if self.is_word:                  # base case
            return [""]

        result = []
        if self.sub_word:
            result.append("")

        for char in self.children:
            word_list = self.children[char].suffixes()
            for word in word_list:
                result.append(char + word)

        return result


class Trie:
    def __init__(self):
        """ Initialize the trie """
        self.root = TrieNode()

    def insert(self, word):
        """
        Insert a word into the trie 

        Args:
            word(string): path to insert
        """
        current = self.root
        for char in word:
            if char in current.children:
                if current.children[char].is_word:
                    current.children[char].sub_word = True
                    current.children[char].is_word = False
                current = current.children[char]
            else:
                current = current.insert(char)
        current.is_word = True
        current.sub_word = False

    def find(self, prefix):
        """
        Navigate the Trie to find a match for this prefix

        Args:
            prefix(string): prefix to find 
        Return:
            node for a match, or None for no match
        """
        current = self.root
        for char in prefix:
            if char not in current.children:
                return None
            current = current.children[char]
        return current


# ------------------------------------------------ #
# Test Cases                                       #
# ------------------------------------------------ #

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

from sys import prefix
from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')

# Test 1
interact(f,prefix='a')
# nt
# nthology
# ntagonist
# ntonym

# Test 2
interact(f, prefix='t')
# rie
# rigger
# rigonometry
# ripod

# Test 3
interact(f, prefix='g')
# g not found
