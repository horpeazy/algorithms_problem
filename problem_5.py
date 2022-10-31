## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.next_word = False
    
    def insert(self, char):
        new_node = TrieNode()
        self.children[char] = new_node
        return new_node
    
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        result = []
        if self.next_word:
            result.append("")
        elif self.is_word and not self.next_word:
            return [""]
        
        for char in self.children:
            children = self.children[char].suffixes()
            for child in children:
                result.append(char + child)
                
        return result
        
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current = self.root
        for char in word:
            if char in current.children:
                if current.children[char].is_word:
                    current.next_word = True
                    new_node = current.insert(char)
                    current = new_node
                    continue
                current = current.children[char]
            else:
                current.insert(char)
                current = current.children[char]
        current.is_word = True
        current.next_word = False

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current = self.root
        for char in prefix:
            if char not in current.children:
                return None
            current = current.children[char]
        return current


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

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
interact(f,prefix='')